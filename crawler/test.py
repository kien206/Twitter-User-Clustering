import logging
from XCrawler import XCrawler
from exceptions.exceptions import *
import time
from kafka import KafkaProducer
from confluent_kafka.serialization import StringSerializer
import json 
queries = [
    'Web3',
    'Decentralized Web',
    'Blockchain',
    'Smart Contract',
    'DApp',
    'DeFi',
    'NFT',
    'Ethereum',
    'Polkadot',
    'Solana',
    'Cardano',
    'Tezos',
    'Solidity',
    'Smart Contract Development',
    'Web3.js',
    'Ethers.js',
    'Rust',
    'SmartPy',
    'Cryptocurrency',
    'Tokenomic',
    'Consensus Algorithm',
    'Decentralization',
    'Wallets',
    'MetaMask',
    'Uniswap',
    'Aave',
    'Chainlink',
    'OpenSea',
    'Blockchain Meetups',
    'Web3 Conferences',
    'Crypto Communities'
]
test = ['NFT', 'ethereum']
def json_serializer(data):
    return json.dumps(data).encode('utf-8')
producer = KafkaProducer(
    bootstrap_servers = ['34.142.194.212:9092'], # server name
    key_serializer = StringSerializer('utf_8'),
    value_serializer = json_serializer
    )
def main():
    for query in queries:
        start = time.time()
        twitter_getter = XCrawler(username='kien20603', 
                            password='Kien.lt20214907', 
                            email_address='kien.lt0620@gmail.com', 
                            query=query, # query to be used
                            num_scrolls=10, # number of scrolls per search
                            mode=1, # 1 if full search 0 if simplified
                            wait_scroll_base = 2,
                            wait_scroll_epsilon = 1,
                            since_time='2023-01-01', # start date
                            until_time='2023-11-13') # end date
        try:
            twitter_getter.login()
        except ElementNotLoaded as e:
            raise e

        print("Setting query in the object")
        print("Start Search, this will input the query and perform the scroll with the selected mode")
        try:
            twitter_getter.search()
        except ElementNotLoaded as e:
            raise e
        except NoTweetsReturned as e:
            print(e)

        print("Printing returned results and going home")
        try:
            twitter_getter.print_results()
        except UnicodeEncodeError:
            continue
        result = twitter_getter.get_results()
        for tweet_id,tweet in result.items():
            producer.send('group07', key = tweet_id, value = tweet)
            producer.flush()
            producer.send('group07_1', key = tweet_id, value = tweet)
            producer.flush()
        twitter_getter.save_to_json()
        twitter_getter.go_home()
        print("Clearing Results")
        twitter_getter.clear_tweets()
        print("quitting browser")
        twitter_getter.quit_browser()
        print(start - time.time())
    twitter_getter.save_to_csv('twitter_2023.csv')
    producer.close()

if __name__=='__main__':
    main()
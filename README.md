# Twitter data
## Prerequisites

Install libraries in requirements.txt
    
    pip install requirments.txt

## Run the program
1. Clone the repository
   ```sh
   git clone https://github.com/IT4043E-IT5384-2023/Group7-Problem1
   ```
   
2. Monitor to test.py file

3. Replace arguments username, password, email_address to your corresponding Twitter account information.
   ```sh
   twitter_getter = XCrawler(username='<YOUR_X_USERNAME>', 
                            password='<YOUR_X_PASSOWRD>', 
                            email_address='<YOUR_X_EMAIL>', 
                            query=query, 
                            num_scrolls=100, 
                            mode=1, 
                            wait_scroll_base = 2, 
                            wait_scroll_epsilon = 1,
                            since_time='2023-01-01',
                            until_time='2023-11-13')
   ```
    
4. Modify the queries (that will be used to search) and other arguments described in class initailizator as needed
    
5. Run the test.py file
    ```sh
    python test.py
    ```

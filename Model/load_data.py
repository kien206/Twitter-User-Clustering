# import pandas as pd
# from elasticsearch import Elasticsearch
# from elasticsearch.helpers import bulk, streaming_bulk

# # Define your Elasticsearch host and port
# es_host = 'http://34.143.255.36'
# es_port = 9200

# # Define Elasticsearch index and document type (adjust as per your requirements)
# index_name = 'group07'

# # Path to your Parquet file
# parquet_file_path = 'data\it4043e_it4043e_group7_problem1_prediction_part-00000-08946240-4d5a-4914-9733-3338083945e2-c000.snappy.parquet'

# # Read Parquet file into a Pandas DataFrame
# df = pd.read_parquet(parquet_file_path)

# # Convert DataFrame to a list of dictionaries (one dictionary per document)
# documents = df.to_dict(orient='records')

# # Create an Elasticsearch client
# es = Elasticsearch("http://34.143.255.36:9200")

# # Function to index documents using the bulk API
# def index_documents(es, index, documents):
#     for success, info in streaming_bulk(es, documents, index=index):
#         if not success:
#             print(f'Failed to index document: {info}')

# # Index documents in Elasticsearch
# index_documents(es, index_name, documents)

# # Optional: Refresh the index to make the data available for search immediately
# es.indices.refresh(index=index_name)

# print(f'Data from Parquet file has been successfully indexed into Elasticsearch.')


import os
import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import streaming_bulk

# Define your Elasticsearch host and port
es_host = 'http://34.143.255.36'
es_port = 9200

# Define Elasticsearch index (adjust as per your requirements)
index_name = 'group07_keyword'

# Function to index documents using the bulk API
def index_documents(es, index, documents):
    for success, info in streaming_bulk(es, documents, index=index):
        if not success:
            print(f'Failed to index document: {info}')

# Create an Elasticsearch client
es = Elasticsearch("http://34.143.255.36:9200")

# Path to the directory containing Parquet files
parquet_dir = 'wordcount'

# Loop through each part file and upload data to Elasticsearch
for part_file in os.listdir(parquet_dir):
    if part_file.endswith('.parquet'):
        # Construct the full path to the Parquet file
        parquet_file_path = os.path.join(parquet_dir, part_file)

        # Read Parquet file into a Pandas DataFrame
        df = pd.read_parquet(parquet_file_path)

        # Convert DataFrame to a list of dictionaries (one dictionary per document)
        documents = df.to_dict(orient='records')

        # Index documents in Elasticsearch
        index_documents(es, index_name, documents)

        # Optional: Refresh the index to make the data available for search immediately
        es.indices.refresh(index=index_name)

        print(f'Data from Parquet file {part_file} has been successfully indexed into Elasticsearch.')


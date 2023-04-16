import requests
import json
from datetime import datetime

# Constants - Airstack
API_URL = "https://api.airstack.xyz/gql"

with open('airstack_credentials.json', 'r') as f:
    config = json.load(f)

# Extract the API key from the JSON file
API_TOKEN = config['api_key']

def run_metadata_query(address, nft_id, blockchain):
    metadata_query = f""" 
    query NFTMetadata {{ 
        TokenNft( 
            input: {{address: "{address}", tokenId: "{nft_id}", blockchain: {blockchain}}} 
        ) {{ 
        id
        rawMetaData 
        tokenId \
        lastTransferTimestamp 
        type 
        }} 
    }} """

    headers = {"Content-Type": "application/json",
            "Authorization": API_TOKEN}  

    response = requests.post(API_URL, json={'query': metadata_query}, headers=headers)

    return response.json()['data']['TokenNft']

def last_transfer(response):
    """
    Returns last transfer time
    """
    
    if 'lastTransferTimestamp' in list(response.keys()):
        # convert the string to a datetime object
        dt_obj = datetime.strptime(response['lastTransferTimestamp'], '%Y-%m-%dT%H:%M:%SZ')

        # format the datetime object into a string in the desired format
        datetime_format = dt_obj.strftime('%Y-%m-%d %H:%M:%S UTC')

        output_str = f"Last Transfer Time: {datetime_format}\n"
        
        return output_str
    
    else:
        return "Last Transfer Time undefined/missing\n"

def process_metadata(response):
    """
    Does the following:
    1. List metadata keys
    2. Check if nested
    3. Check if encoded JSON string or Image (skip if so!)
    
    
    """
    
    if 'rawMetaData' in list(response.keys()):
        # Create list of keys in metadata
        metadata = response['rawMetaData']
        
        metadata_keys = list(metadata.keys())
        
        output_str = ''
        # Loop through keys
        for key in metadata_keys:
            
            # First check: Nested?
            if isinstance(metadata[key], str):
                
                # Second check: Encoded JSON or Image
                img_str = 'data:image'
                json_str = 'data:json'
                
                if img_str in metadata[key]:
                    output_str += f'{key} : (Image Data)\n'
                elif json_str in metadata[key]:
                    output_str += f'{key} : (Bas64 JSON Data)\n'
                else:
                    output_str += f'{key} : {metadata[key]} \n'
            
            else:
                # Just print keys for now
                output_str += str(list(metadata[key].keys()))
            
        return output_str
    
    else:
        return "Raw Metadata undefined/missing"
    
def run_metadata(address, token_id, blockchain):

    response = run_metadata_query(address, token_id, blockchain)
    print(response)
    formatted_str = ''
    formatted_str += f'Token address: {address}\n'
    formatted_str += f'Token ID: {token_id}\n'
    formatted_str += f'Chain: {blockchain}\n'
    formatted_str += last_transfer(response)
    formatted_str += process_metadata(response)

    return formatted_str

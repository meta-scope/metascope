import requests
import json
from datetime import datetime

# Constants - Airstack
API_URL = "https://api.airstack.xyz/gql"

with open('airstack_credentials.json', 'r') as f:
    config = json.load(f)

# Extract the API key from the JSON file
API_TOKEN = config['api_key']


def run_metadata_query(address, nft_id, blockchain='ethereum'):
    metadata_query = f""" 
    query NFTMetadata {{ 
        TokenNft( 
            input: {{address: {address}, tokenId: {nft_id}, blockchain: {blockchain}}} 
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

    response = requests.post(API_URL, json={'query': query}, headers=headers)

    return response.json()

def last_transfer(metadata):
    """
    Returns last transfer time
    """
    
    if 'lastTransferTimestamp' in list(metadata.keys()):
        # convert the string to a datetime object
        dt_obj = datetime.strptime(metadata['lastTransferTimestamp'], '%Y-%m-%dT%H:%M:%SZ')

        # format the datetime object into a string in the desired format
        datetime_format = dt_obj.strftime('%Y-%m-%d %H:%M:%S UTC')

        output_str = f"Last Transfer Time: {datetime_format}"
        
        return output_str
    
    else:
        return "Last Transfer Time undefined/missing"



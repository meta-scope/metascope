import requests
import json

API_URL = "https://api.airstack.xyz/gql"

# Open the JSON file and load its contents
with open('airstack_credentials.json', 'r') as f:
    config = json.load(f)

# Extract the API key from the JSON object
API_TOKEN = config['api_key']

headers = {"Content-Type": "application/json",
            "Authorization": API_TOKEN}     

query = """
query NFTMetadata {
  TokenNft(
    input: {address: "0xc36442b4a4522e871399cd717abdd847ab11fe88", tokenId: "100", blockchain: ethereum}
  ) {
    id
    rawMetaData
    tokenId
    lastTransferTimestamp
    type
  }
}

"""      

response = requests.post(API_URL, json={'query': query})

print(response.text)
import requests

import os

from dotenv import load_dotenv


#import the VAPI_API_KEY from the .env file
load_dotenv()
VAPI_API_KEY = os.getenv("VAPI_API_KEY")


headers = {
    'Authorization': f'Bearer {VAPI_API_KEY}',
}

#Creating knowledge base

data_kb = {
    "provider" : "trieve",
    "name": "vapi",
}

requests.post('https://api.vapi.ai/knowledge-base', headers=headers, json=data_kb)






assistant_id = os.getenv("ASSISTANT_ID")
phone_number_id = os.getenv("PHONE_NUMBER_ID")
customer_number = os.getenv("CUSTOMER_NUMBER")

data = {
    
    "assistant": {


    }
    
    
    
    
    
    
    
    "phoneNumberId": "{phone_number_id}",
    "customer": {
        "number": "{customer_number}"
    },

}

response = requests.post('https://api.vapi.ai/call', headers=headers, json=data)



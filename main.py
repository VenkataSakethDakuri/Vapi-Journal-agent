import requests

import os

from dotenv import load_dotenv

auth_token = VAPI_API_KEY

phone_number_id = ''
customer_number = ""

headers = {
    'Authorization': f'Bearer {auth_token}',
    'Content-Type': 'application/json',
}

# Create the data payload for the API request
data = {
    'assistant': {
        "firstMessage": "Hey, what's up?",
        "model": {
            "provider": "openai",
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": "You are an assistant."
                }
            ]
        },
        "voice": "jennifer-playht"
    },
    'phoneNumberId': phone_number_id,
    'customer': {
        'number': customer_number,
    },
}


response = requests.post(
    'https://api.vapi.ai/call/phone', headers=headers, json=data)


# Check if the request was successful and print the response
if response.status_code == 201:
    print('Call created successfully')
    print(response.json())
else:
    print('Failed to create call')
    print(response.text)


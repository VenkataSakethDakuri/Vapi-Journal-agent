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
    "name": "vapi.ai",
}

knowledge_base = requests.post('https://api.vapi.ai/knowledge-base', headers=headers, json=data_kb)






assistant_id = os.getenv("ASSISTANT_ID")
phone_number_id = os.getenv("PHONE_NUMBER_ID")
customer_number = os.getenv("CUSTOMER_NUMBER")

knowledge_base_id = knowledge_base.json()['id']

data_call = {

    "assistant": {

        "transcriber" : {
            "provider": "deepgram",
            "language": "en",
            "model": "nova-2",
        },

        "model": {
            "provider": "openai",
            "model": "gpt-4o",
            "knowledgeBaseId": "{knowledge_base_id}",

            "messages": [
                {
                    "role": "assistant",
                    "content": """You are a friendly voice agent for journaling purposes. 
                    Talk to your user in a friendly way and record everything that the user says. 
                    Keep the conversation hyper personalized by using the previous conversations as a context. 
                    Use the knowledge base for getting context for hyper personalized conversation."""
                }
            ]           
        },

        "voice":{
            "provider": "openai",
            "voiceId": " alloy",
        }
    },    
    
    "phoneNumberId": "{phone_number_id}",
    "customer": {
        "number": "{customer_number}"
    },
}

create_call = requests.post('https://api.vapi.ai/call', headers=headers, json=data_call)

call_id = create_call.json()['id']

# Fetch call details using call_id
call_details_url = f'https://api.vapi.ai/call/{call_id}'
call_details_response = requests.get(call_details_url, headers=headers)

call_details_response.json()['artifactPlan']['analysis']['summary']





# Update knowledge base
new_data_kb = {

    "provider": "trieve",
    "name": "vapi.ai",


}









update_knowledge_base = requests.patch(f'https://api.vapi.ai/knowledge-base/{knowledge_base_id}', headers=headers, json={})




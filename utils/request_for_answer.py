import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

def send_to_other_api(questions):
    API_URL = os.getenv("APPLICATION_COMMENT_API_URL")
    other_api_token = os.getenv("OTHER_API_TOKEN", "sample_token")
    headers = {
        "Content-Type": "application/json",
        # "Authorization": f"Bearer {other_api_token}"
    }
    print(questions)
    for question in questions:
        payload = {
            "customer_id": question.get("customerId"),
            "product_name": question.get("productName"),
            "content_id": question.get("id"),
            "content": question.get("text"),
            "web_url": question.get("webUrl"),
            "status": question.get("status")
        }
        try:
            response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
            if response.status_code in [200, 201]:
                print(f"Question {payload['content_id']} sent successfully. Response: {response.status_code}")
            else:
                print(f"Question {payload['content_id']} could not be sent. Error code: {response.status_code}")
                print(f"Error message: {response.text}")
        except Exception as e:
            print(f"Error occurred while sending question {payload['content_id']}: {str(e)}")

import requests
import os

from dotenv import load_dotenv

load_dotenv()

def update_status_for_answer(id, status):

    payload = {
        'id': id,
        'status': status
    }

    try:
        API_URL = os.getenv("APPLICATION_ANSWERED_API_URL")
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            print(f"Answer {id} updated to {status}")
        else:
            print(f"API request failed: {response.status_code}")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")

import requests
import base64
import os

from dotenv import load_dotenv

from utils.update_status_for_answer import update_status_for_answer

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
SELLER_ID = os.getenv("SELLER_ID")
API_URL = os.getenv("TRENDYOL_POST_ANSWER_URL")

auth_str = f"{API_KEY}:{API_SECRET}"
auth_bytes = auth_str.encode("utf-8")
auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

headers = {
    "Authorization": f"Basic {auth_base64}",
    "User-Agent": f"{SELLER_ID} - SelfIntegration",
    "Content-Type": "application/json"
}

def post_answer(approved_comments):
    try:
        for comment in approved_comments:
            id = comment.get("id")
            question_id = comment.get("content_id")
            response = comment.get("response")

            url = API_URL.replace("{sellerId}", SELLER_ID).replace("{questionId}", question_id)

            payload = {
                "text": response
            }

            service_response = requests.post(url, headers=headers, json=payload)
            if service_response.status_code == 200:
                update_status_for_answer(id,"ANSWERED")
            else:
                #update_status_for_answer(id,"ANSWERED")
                print("Status Code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")

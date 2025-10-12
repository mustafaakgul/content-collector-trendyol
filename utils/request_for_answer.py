import requests
import base64
from datetime import datetime, timedelta
import time
import os
from dotenv import load_dotenv
import json


load_dotenv()


def send_to_other_api(questions):
    other_api_url = os.getenv("OTHER_API_URL", "http://127.0.0.1:8000/api/v1/comment/")
    other_api_token = os.getenv("OTHER_API_TOKEN", "ornek_token")
    headers = {
        "Content-Type": "application/json",
        # "Authorization": f"Bearer {other_api_token}"
    }
    print(questions)
    for soru in questions:
        payload = {
            "customer_id": soru.get("customerId"),
            "product_name": soru.get("productName"),
            "content_id": soru.get("id"),
            "content": soru.get("text"),
            "web_url": soru.get("webUrl"),
            "status": soru.get("status")
        }
        try:
            response = requests.post(other_api_url, headers=headers, data=json.dumps(payload))
            if response.status_code in [200, 201]:
                print(f"Soru {payload['content_id']} başarıyla gönderildi. Yanıt: {response.status_code}")
            else:
                print(f"Soru {payload['content_id']} gönderilemedi. Hata kodu: {response.status_code}")
                print(f"Hata mesajı: {response.text}")
        except Exception as e:
            print(f"Soru {payload['content_id']} gönderilirken hata oluştu: {str(e)}")

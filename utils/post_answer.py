import requests
import base64
import os

BASE_URL = "https://apigw.trendyol.com/integration/qna/sellers/{sellerId}/questions/{questionId}/answers"

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
SELLER_ID = os.getenv("SELLER_ID")

seller_id = "554417"
question_id = "355137437"
api_key = "mDZMwneQyDYbI3DF520J"
api_secret = "MuE0tSgYYip4qsbXzNrM"

auth_str = f"{api_key}:{api_secret}"
auth_bytes = auth_str.encode("utf-8")
auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

answer_text = "Test has been completed successfully, thank you"

url = BASE_URL.replace("{sellerId}", seller_id).replace("{questionId}", question_id)

headers = {
    "Authorization": f"Basic {auth_base64}",
    "User-Agent": f"{seller_id} - SelfIntegration",
    "Content-Type": "application/json"
}

payload = {
    "text": answer_text
}

response = requests.post(url, headers=headers, json=payload)

print("Status Code:", response.status_code)
try:
    print("Response Body:", response.json())
except:
    print("Raw Response:", response.text)

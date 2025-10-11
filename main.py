import requests
import base64
from datetime import datetime, timedelta
import time
import os
from dotenv import load_dotenv


load_dotenv()


def trendyol_get_questions(api_key, api_secret, seller_id, params):
    auth_str = f"{api_key}:{api_secret}"
    auth_bytes = auth_str.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    headers = {
        "Authorization": f"Basic {auth_base64}",
        "User-Agent": f"{seller_id} - SelfIntegration",
        "Content-Type": "application/json"
    }

    url = f"https://apigw.trendyol.com/integration/qna/sellers/{seller_id}/questions/filter"

    response = requests.get(url, headers=headers, params=params)

    result = response.json()

    print(f"Toplam soru sayısı: {result['totalElements']}")
    print(f"Sayfa: {result['page']} / {result['totalPages']}")

    for soru in result['content']:
        print(f"creationDate: {soru['creationDate']}")
        print(f"customerId: {soru['customerId']}")
        print(f"id: {soru['id']}")
        print(f"Ürün: {soru['productName']}")
        print(f"Soru: {soru['text']}")
        print(f"Cevap: {soru.get('answer', {}).get('text', 'Cevap yok')}")
        print(f"Durum: {soru['status']}")
        print(f"Link: {soru['webUrl']}")
        print("-" * 40)



if __name__ == "__main__":
    # Çevre değişkenlerini oku
    API_KEY = os.getenv("API_KEY")
    API_SECRET = os.getenv("API_SECRET")
    SELLER_ID = os.getenv("SELLER_ID")

    start_date = int(time.mktime((datetime.now() - timedelta(weeks=2)).timetuple()) * 1000)
    end_date = int(time.mktime(datetime.now().timetuple()) * 1000)

    # Parametreler
    params = {
        "startDate": start_date,
        "endDate": end_date,
        "status": "WAITING_FOR_ANSWER"
    }

    result = trendyol_get_questions(API_KEY, API_SECRET, SELLER_ID, params)


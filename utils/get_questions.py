import requests
import base64

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

    questions = []
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
        questions.append(soru)

    return questions

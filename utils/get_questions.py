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

    print(f"Total questions: {result['totalElements']}")
    print(f"Page: {result['page']} / {result['totalPages']}")

    questions = []
    for question in result['content']:
        print(f"creationDate: {question['creationDate']}")
        print(f"customerId: {question['customerId']}")
        print(f"id: {question['id']}")
        print(f"Product: {question['productName']}")
        print(f"Question: {question['text']}")
        print(f"Answer: {question.get('answer', {}).get('text', 'No answer')}")
        print(f"Status: {question['status']}")
        print(f"Link: {question['webUrl']}")
        print("-" * 40)
        questions.append(question)

    return questions

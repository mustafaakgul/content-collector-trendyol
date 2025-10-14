import requests

def get_approved_comments(API_URL):
    try:
        response = requests.get(API_URL)
        response.raise_for_status()

        data = response.json()

        if data.get("status") == "true" and "payload" in data:
            comments = data["payload"]

            if not comments:
                print("Hiç onaylanmış yorum bulunamadı.")
                return

            print(f"Toplam {len(comments)} onaylanmış yorum bulundu:\n")
            for comment in comments:
                content_id = comment.get("content_id")
                content = comment.get("content")
                print(f"Content ID: {content_id} | Content: {content}")

        else:
            print("Beklenmeyen yanıt formatı:", data)

    except requests.exceptions.RequestException as e:
        print(f"API isteği başarısız oldu: {e}")
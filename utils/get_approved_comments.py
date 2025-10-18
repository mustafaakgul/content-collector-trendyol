import requests

def get_approved_comments(API_URL):
    try:
        response = requests.get(API_URL)
        response.raise_for_status()

        data = response.json()

        if data.get("status") == "true" and "payload" in data:
            comments = data["payload"]
            resp = []

            if not comments:
                print("No approved comments found.")
                return
            return comments

        else:
            print("Unexpected response format:", data)

    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")

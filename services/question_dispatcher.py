from datetime import datetime, timedelta
import time
import os
from dotenv import load_dotenv

from utils.get_questions import trendyol_get_questions
from utils.request_for_answer import send_to_other_api

load_dotenv()

if __name__ == "__main__":
    API_KEY = os.getenv("API_KEY")
    API_SECRET = os.getenv("API_SECRET")
    SELLER_ID = os.getenv("SELLER_ID")

    start_date = int(time.mktime((datetime.now() - timedelta(weeks=2)).timetuple()) * 1000)
    end_date = int(time.mktime(datetime.now().timetuple()) * 1000)

    params = {
        "startDate": start_date,
        "endDate": end_date,
        "status": "WAITING_FOR_ANSWER"
    }

    questions = trendyol_get_questions(API_KEY, API_SECRET, SELLER_ID, params)
    send_to_other_api(questions)

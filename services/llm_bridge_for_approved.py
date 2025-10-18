import os
from dotenv import load_dotenv

from utils.get_approved_comments import get_approved_comments

load_dotenv()

if __name__ == "__main__":
    API_URL = os.getenv("APPLICATION_APPROVED_API_URL")

    approved_comments = get_approved_comments(API_URL)
    post_answer(approved_comments)

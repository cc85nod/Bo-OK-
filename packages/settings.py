import os
from dotenv import load_dotenv

dot_env = '../.env'
load_dotenv(dot_env)

ACCOUNT = os.getenv("gmail_account")
PASSWORD = os.getenv("gmail_password")
from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv('EMAIL')
password=os.getenv('PASSWORD')
secret_key=os.getenv('SECRET_KEY')
print(email)
print(password)
print(secret_key)
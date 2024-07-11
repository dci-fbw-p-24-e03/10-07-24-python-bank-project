from dotenv import load_dotenv
import os

load_dotenv()
email = os.getenv('EMAIL')
password=os.getenv('PASSWORD')
print(email)
print(password)
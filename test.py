import requests
import os

# load_dotenv()  # take environment variables from .env.

# jms_getbwcounter_url = os.environ.get('JMS_GETBWCOUNTER_URL')

# if jms_getbwcounter_url:
#     r = requests.get(jms_getbwcounter_url)
#     print(r.text)

n = -1

n = 24 if n > 24 else n
n = 0 if n < 0 else n

try:
    print(int('a'))
except ValueError:
    print(10)

print(n)

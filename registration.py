import random
import string
from fake_useragent import UserAgent
import requests
from loguru import logger

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

async def register_account(email, password, refer_code=None):
    headers = {'User-Agent': UserAgent().random}
    data = {
        'email': email,
        'password': password,
        'refer_code': refer_code
    }
    try:
        response = requests.post('https://example.com/register', headers=headers, data=data)
        if response.status_code == 200:
            logger.info(f"Account registered successfully for {email}.")
            return f"Account registered successfully for {email}."
        else:
            logger.error(f"Failed to register account for {email}. Error: {response.text}")
            return f"Failed to register account for {email}. Error: {response.text}"
    except requests.RequestException as e:
        logger.exception(f"Failed to register account for {email}. Exception: {str(e)}")
        return f"Failed to register account for {email}. Exception: {str(e)}"

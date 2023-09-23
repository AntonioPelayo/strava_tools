import os

import dotenv
import requests

from athlete import profile_endpoint
from utils import handle_status_code


def main():
    dotenv.load_dotenv()

    r = requests.get(
        profile_endpoint(),
        headers={'Authorization': f'Bearer {os.getenv("ACCESS_TOKEN")}'}
    )

    if handle_status_code(r):
        print(r.json())

if __name__ == '__main__':
    main()

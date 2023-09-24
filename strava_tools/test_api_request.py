import dotenv
import requests

from strava_api_endpoints import StravaAPIEndpoints
from utils.env_utils import env_get
from utils.utils import handle_status_code

def main():
    token = env_get("APPLICATION_ACCESS_TOKEN")
    headers={'Authorization': f'Bearer {token}'}
    r = requests.get(StravaAPIEndpoints.athlete_profile(), headers=headers)

    if handle_status_code(r):
        print(r.json())

if __name__ == '__main__':
    main()

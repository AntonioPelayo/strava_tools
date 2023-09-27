import sys
from datetime import datetime

import requests

from strava_tools.utils.env_utils import env_get, env_set
from strava_tools.utils.utils import handle_status_code

from strava_tools.strava_api_endpoints import StravaAPIEndpoints

def access_token_expiration_date():
    """
    Returns the expiration date of the access token in readable format.
    """
    ts = int(env_get('APPLICATION_ACCESS_TOKEN_EXPIRES_AT'))
    return datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def access_token_is_expired():
    """
    Checks if the access token is expired.
    """
    exp = int(env_get('APPLICATION_ACCESS_TOKEN_EXPIRES_AT'))
    now = int((datetime.now() - datetime.utcfromtimestamp(0)).total_seconds())
    return True if exp < now else False

def refresh_access_token():
    """
    Refreshes the access token, and updates the .env file.
    """
    payload = {
        'client_id': env_get('APPLICATION_CLIENT_ID'),
        'client_secret': env_get('APPLICATION_CLIENT_SECRET'),
        'grant_type': 'refresh_token',
        'refresh_token': env_get('APPLICATION_REFRESH_TOKEN')
    }

    r = requests.post(StravaAPIEndpoints.token_refresh(), data=payload)

    if handle_status_code(r):
        now = (datetime.now() - datetime.utcfromtimestamp(0)).total_seconds()
        env_set('APPLICATION_ACCESS_TOKEN', r.json()['access_token'])
        env_set('APPLICATION_ACCESS_TOKEN_EXPIRES_AT', r.json()['expires_at'])
        env_set('APPLICATION_ACCESS_TOKEN_CREATED_AT', int(now))
    else:
        print("Failed to refresh access token")
        sys.exit(1)
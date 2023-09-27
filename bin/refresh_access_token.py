from strava_tools.utils.token_utils import access_token_is_expired, refresh_access_token

def main():
    if access_token_is_expired():
        refresh_access_token()
        print("Access token has been refreshed.")
    else:
        print("Access token is not expired.")

if __name__ == '__main__':
    main()
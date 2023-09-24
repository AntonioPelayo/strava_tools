import sys

def handle_status_code(r):
    """
    Handle the status codes and print the appropriate messages.
    If the request is unsuccessful, the program will terminate.
    """
    messages = {
        200: "Request successful.",
        201: "Your activity/etc. was successfully created.",
        401: "Unauthorized, check your access token.",
        403: "Forbidden; you cannot access.",
        404: "Not found; the requested asset does not exist, or you are not authorized to see it.",
        429: "Too Many Requests; you have exceeded rate limits.",
        500: "Strava is having issues, please check https://status.strava.com."
    }

    if r.status_code == 200:
        return True

    message = messages.get(r.status_code, f"Unknown status code.\n{r.json()}")
    print(message)

    sys.exit(1)

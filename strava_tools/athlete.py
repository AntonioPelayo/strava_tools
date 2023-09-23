
def profile_endpoint():
    return f'https://www.strava.com/api/v3/athlete'

def stats_endpoint(athlete_id):
    return f'https://www.strava.com/api/v3/athletes/{athlete_id}/stats'

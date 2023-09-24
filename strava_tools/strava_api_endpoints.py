
class StravaAPIEndpoints:
    BASE_URL = 'https://www.strava.com/api/v3'

    @classmethod
    def athlete_profile(cls):
        return f'{cls.BASE_URL}/athlete'
    @classmethod
    def athlete_stats(cls, athlete_id):
        return f'{cls.BASE_URL}/athletes/{athlete_id}/stats'

    @classmethod
    def token_refresh(cls):
        return f'{cls.BASE_URL}/oauth/token'

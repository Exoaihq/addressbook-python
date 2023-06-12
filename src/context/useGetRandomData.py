import requests
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=100, ttl=300)

base_url = "https://randomuser.me/api/"

def get_random_user_data(results=500, nationalities="us"):
    @cached(cache)
    def fetch_data():
        response = requests.get(f"{base_url}?results={results}&nat={nationalities}")
        return response.json()

    return fetch_data()
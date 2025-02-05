from decouple import config
import requests
from urllib.parse import urljoin
import traceback

def get_full_url(endpoint: str = None):
    try:
        base_url = config('API_URL')
        return urljoin(base_url, endpoint)
    except Exception:
        msg = traceback.format_exc()
        raise Exception(f"An exception occured: {msg}")

def get_single_item(endpoint: str = None):
    try:
        url = get_full_url(endpoint)
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception:
        msg = traceback.format_exc()
        raise Exception(f"Exception occured: {msg}")


def get_many_items(endpoint: str = None):
    try:
        url = get_full_url(endpoint)
        while url:
            response = requests.get(url)
            response.raise_for_status()
            res = response.json()
            results = res.get('results')
            url = res.get("next")
            yield results
    except Exception:
        msg = traceback.format_exc()
        raise Exception(f"Exception occured: {msg}")

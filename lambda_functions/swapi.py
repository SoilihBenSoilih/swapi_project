from typing import Generator
import traceback
from urllib.parse import urljoin

import requests
from decouple import config



def make_url(endpoint: str = None) -> str:
    """
        Make a full url with an endpoint
    """
    try:
        base_url = config('API_URL')
        return urljoin(base_url, endpoint)
    except Exception:
        msg = traceback.format_exc()
        raise Exception(f"An exception occured: {msg}")

def retrieve_item(endpoint: str = None) -> dict:
    """
        retrieve a single item, example a specific character
    """
    try:
        url = make_url(endpoint)

        response = requests.get(url)
        
        # handle errors
        response.raise_for_status()
        
        return response.json()
    except Exception:
        msg = traceback.format_exc()
        raise Exception(f"Exception occured: {msg}")


def retrieve_items(endpoint: str = None) -> Generator:
    """
        retrieve items, like films
    """
    try:
        url = make_url(endpoint)
        while url:
            # call the api
            response = requests.get(url)
            
            # handle errors
            response.raise_for_status()
            
            # get results
            res = response.json()
            results = res.get('results')
            
            # get next url
            url = res.get("next")
            
            yield results
    
    except Exception:
        msg = traceback.format_exc()
        raise Exception(f"Exception occured: {msg}")

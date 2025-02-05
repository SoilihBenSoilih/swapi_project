import json
from datetime import datetime

from swapi import retrieve_items



def retrieve_earliest_film(films: list) -> dict:
    """ 
        Get earlist film from a list of films
    """
    date_format = '%Y-%m-%d'
    return min(
        films, 
        key=lambda x: datetime.strptime(x.get("release_date"), date_format)
    )

def lambda_handler(event, context):
    """
        Lambda function to get earliest film from '/films/' endpoint
    """
    films = retrieve_items("films")
    
    results = []
    for film in films:
        results.extend(film)
    
    earliest_film = retrieve_earliest_film(results)
    
    return {
        "statusCode": 200,
        "body": json.dumps(earliest_film, default=str)
    }

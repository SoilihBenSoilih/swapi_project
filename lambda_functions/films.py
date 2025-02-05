import json
from swapi import get_many_items
from datetime import datetime



def get_earliest_film(films: list) -> dict:
    date_format = '%Y-%m-%d'
    return min(
        films, 
        key=lambda x: datetime.strptime(x.get("release_date"), date_format)
    )

def lambda_handler(event, context):
    films = get_many_items("films")
    results = []
    for film in films:
        results.extend(film)
    earliest_film = get_earliest_film(results)
    return {
        "statusCode": 200,
        "body": json.dumps(earliest_film, default=str)
    }

import json
from swapi import get_single_item
from concurrent.futures import ThreadPoolExecutor



def lambda_handler(event, context):
    film = event.get("film")
    characters = film.get("characters", [])
    characters_count = len(characters)
    
    if not characters_count:
        film['average_height'] = 0
        return {
            "statusCode": 200,
            "body": json.dumps(film, default=str)
        }
    
    heights = 0

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(get_single_item, characters))
    
    heights = sum(float(person.get("height", 0)) for person in results)

    average_height = heights / characters_count
    film["average_height"] = average_height

    return {
        "statusCode": 200,
        "body": json.dumps(film, default=str)
    }

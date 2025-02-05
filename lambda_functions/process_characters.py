import json
from concurrent.futures import ThreadPoolExecutor

from swapi import retrieve_item



def lambda_handler(event, context):
    """
        Process Characters to get avergage height and enrich film input 
    """
    # get characters and characters count
    film = json.loads(event.get("body"))
    characters = film.get("characters", [])
    characters_count = len(characters)
    
    # if no characters the average is 0
    if not characters_count:
        film['average_height'] = 0
        return {
            "statusCode": 200,
            "body": json.dumps(film, default=str)
        }

    # get characteristics of all characters in a thread 
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(retrieve_item, characters))
    
    # sum all character heights
    heights = sum(float(person.get("height", 0)) for person in results)

    # calculate average height
    average_height = heights / characters_count
    film["average_height"] = average_height
    
    return {
        "statusCode": 200,
        "body": json.dumps(film, default=str)
    }

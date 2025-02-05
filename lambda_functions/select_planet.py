import json
from swapi import get_many_items



def lambda_handler(event, context):
    film = event.get("film")
    
    planets = get_many_items('planets')

    all_planets = []
    for planet in planets:
        all_planets.extend(planet)
    
    average_height = int(film['average_height'])
    index = average_height % len(all_planets)
    selected_planet = all_planets[index]
    film["selected_planet"] = selected_planet

    return {
        "statusCode": 200,
        "body": json.dumps(film, default=str)
    }

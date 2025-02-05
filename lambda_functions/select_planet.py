import json

from swapi import retrieve_items



def lambda_handler(event, context):
    """
        Select a planet by specific index calculations and enrich film input:
        index = average_height % number_of_planets
    """
    film = json.loads(event.get("body"))
    
    # call planets endpoint
    response = retrieve_items('planets')

    # retrieve all planets
    planets = []
    for planet in response:
        planets.extend(planet)
    
    # Calculate index
    average_height = int(film['average_height'])
    index = average_height % len(planets)
    
    # Select planet and enrich the result
    selected_planet = planets[index]
    film["selected_planet"] = selected_planet

    return {
        "statusCode": 200,
        "body": json.dumps(film, default=str)
    }

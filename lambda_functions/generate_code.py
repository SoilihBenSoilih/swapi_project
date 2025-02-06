import json



def number_to_letter(number: int) -> str:
    """ Map a number to a letter using unicode code. 
        The mapping follows this logic: 1 = A, 2 = B, etc.
    """
    return chr(ord("a") + number - 1).upper()


def lambda_handler(event, context):
    """
        Generate secret code with the following:
        First letter: film's episode_id
        Second letter: number of selected planet residents % 10
        Last letter: first letter of the planet name
    """
    film = json.loads(event.get("body"))
    
    # initialize secret code
    secret_code = ""

    # compute first letter
    episode_id = film["episode_id"]
    secret_code += number_to_letter(episode_id)

    # compute second letter
    selected_planet = film["selected_planet"]
    residents_count = len(selected_planet["residents"]) % 10
    secret_code += str(residents_count)

    # get last letter
    secret_code += selected_planet["name"][0].upper()

    # format the result
    result = {
        "secret_code": secret_code
    }

    return {
        "statusCode": 200,
        "body": json.dumps(result, default=str)
    }

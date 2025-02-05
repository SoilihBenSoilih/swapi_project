import json



def map_number_to_letter(num):
    return chr(ord("a") + num - 1).upper()


def lambda_handler(event, context):
    film = event.get("film")
    
    secret_code = ""

    episode_id = film["episode_id"]
    secret_code += map_number_to_letter(episode_id)

    selected_planet = film["selected_planet"]
    residents_count = len(selected_planet["residents"]) % 10
    secret_code += map_number_to_letter(residents_count)

    secret_code += selected_planet["name"][0].upper()

    result = {
        "secret_code": secret_code
    }

    return {
        "statusCode": 200,
        "body": json.dumps(result, default=str)
    }

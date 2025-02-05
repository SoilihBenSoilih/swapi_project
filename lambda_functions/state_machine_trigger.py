import json
import time

import boto3
import requests
from decouple import config


def lambda_handler(event, context):
    """
        Trigger the state machine and get the result
    """
    # get workflow url
    workflow_url = config("WORKFLOW_URL")
    
    # trigger the step function
    response = requests.get(workflow_url)
    data = response.json()
    
    # get excecution ARN
    execution_arn = data["executionArn"]

    # initialize step function client
    stepfunctions = boto3.client("stepfunctions")

    
    while True:
        response = stepfunctions.describe_execution(executionArn=execution_arn)
        status = response["status"]

        if status == "SUCCEEDED":
            return json.loads(response["output"])
        
        elif status in ("FAILED", "TIMED_OUT", "ABORTED"):
            raise Exception(f"Execution failed: {status}")
        time.sleep(2)

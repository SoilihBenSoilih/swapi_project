# Docummentation for the challenge

### API Gateway endpoint

#### URL

* https://sv542w6qga.execute-api.us-east-1.amazonaws.com/Prod/{endpoint}

#### endpoints

* film
* characters
* planet
* code
* workflow
* trigger

### Resources
* https://github.com/aws/aws-sam-cli-app-templates for templates
* https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeExecution.html#StepFunctions-DescribeExecution-request-executionArn for the describe method
* https://stackoverflow.com/questions/61602349/get-tasks-status-in-aws-step-functions-boto3 for code example
* https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-state-machine-using-sam.html for setting up SAM
* https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions/client/describe_execution.html for executing the woorkflow
* https://chatgpt.com for troubleshooting

### Deployment process

#### Prerequisites

* install aws and configure it
* install sam
* if you need to test locally, you need docker to install docker too

#### Commands

* sam build
* sam deploy --guided


#### Local tests

* sam local start-api --port 5000 (test locally)
* sam local invoke FunctionName --event params.json (invoque a fonction with params.json a file to be passed in event)

#### Delete

* sam delete --stack-name {sam-app-name} --no-prompts

### Missing importants parts

* Tests
* Security

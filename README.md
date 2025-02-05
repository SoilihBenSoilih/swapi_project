# Star Wars API Secret Code Generator Challenge

## Overview
Build a serverless application that interacts with the Star Wars API (SWAPI) to generate a secret code using AWS Lambda functions orchestrated by AWS Step Functions and exposed via API Gateway. As you work through the challenge, record each intermediate result separately so that by the end you have a clear understanding of what your final Lambda output should be.

## Technical Stack
- AWS Lambda (Python)
- AWS Step Functions
- Amazon API Gateway
- Star Wars API (SWAPI) - [https://swapi.dev/api/](https://swapi.dev/api/)

## AWS Account Requirements
- Use your personal AWS account for this challenge.
- All services used (Lambda, Step Functions, API Gateway) are covered under the AWS perpetual free tier.
- The expected usage for this challenge should result in zero costs.
- **Important:**
  - Monitor your AWS Console for any unintended resource usage.
  - Clean up all resources after completion.
- We are not responsible for any AWS costs if resources are not properly monitored or cleaned up.

## Required Lambda Functions

### 1. getFilmData
- **Objective:**
  - Query the SWAPI `/films/` endpoint.
  - Find and return the film with the earliest release date.
- **Output:**
  - Return the complete film data for subsequent steps.
- **Note:**  
  Document the full payload returned and note which film was selected.

### 2. processCharacter
- **Objective:**
  - Accept the film data from the previous step.
  - For each character URL in that film, query the SWAPI `/people/` endpoint.
  - Calculate the average height (or another numeric aggregate) of all characters.
- **Output:**
  - Return the original film data along with the calculated average height.
- **Note:**  
  Record the individual character data responses and the computed aggregate value.

### 3. selectPlanet
- **Objective:**
  - Retrieve the complete list of planets from SWAPI by querying the `/planets/` endpoint.
  - Use the average height (from processCharacter) to select one planet:
    - Convert the average height to an integer.
    - Calculate:  
      `index = average_height % number_of_planets`
    - Select the planet at the calculated index.
- **Output:**
  - Return the selected planet data along with the data from the previous step.
- **Note:**  
  Document the logic used and the details of the selected planet.

### 4. generateCode
- **Objective:**
  Generate a 3-character secret code where:
  - **First character:** Map the film's `episode_id` to a letter (e.g., 1 = A, 2 = B, etc.).
  - **Second character:**  
    - Count the total number of residents on the selected planet (using the `residents` array).
    - Perform modulo 10 on this count (`residents_count % 10`) to get a single digit.
  - **Third character:** Use the first letter of the planet name (uppercase).
- **Output Format:**
  ```json
  {
      "secret_code": "XYZ"
  }
  ```
- **Note:**  
  Record the mapping methods and all intermediate outputs (the letter derived from `episode_id`, the calculated digit, and the first letter of the planet name) that lead to the final secret code.

### 5. state_machine_trigger
- **Objective:**
  - Serve as the API Gateway integration point.
  - Trigger the Step Functions state machine.
  - Return the final output (which includes the secret code) to the API caller.
- **Note:**  
  Document the structure of your API request payload and the final output received from the Lambda.

## Solution Requirements
1. All calculations must be performed algorithmically.
2. No hardcoding of values or results.
3. All code must include clear comments explaining the logic. (Including all functions inputs and expected outputs)
4. Record all intermediate outputs and logic in a separate document for review.

## Deliverables

1. **Code Repository:**  
   - Include Python files for all Lambda functions (with comments) and the AWS Step Functions state machine definition (JSON or YAML).

2. **Endpoint to Test the Solution:**  
   - Provide a working API Gateway endpoint URL that triggers your solution and returns the final secret code in the proper JSON format.

3. **Bonus:**  
   - Provide an Infrastructure as Code template (using CloudFormation, Terraform, or the Serverless Framework) to deploy the solution.
   - Provide deployment scripts or detailed instructions on how to deploy it

---

Good luck, and may the Force be with you!

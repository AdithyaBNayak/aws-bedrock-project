import boto3
import json
from Parameters import Parameters

bedrock_client = boto3.client("bedrock-runtime")

def get_payload_body():
    payload_body = {
        "prompt" : "Hi, How are you?",
        "temperature": 0.5,
        "top_p": 0.9,
        "max_gen_len": 512
    }
    return json.dumps(payload_body)

def get_response_from_client():
    response = bedrock_client.invoke_model(
        modelId = Parameters.MODEL_IDS.get("LLAMA2"),
        contentType = "application/json",
        accept = "application/json",
        body = get_payload_body()
    )
    response_body=json.loads(response.get("body").read())
    return response_body

llama2_response = get_response_from_client().get("generation")
print(llama2_response)
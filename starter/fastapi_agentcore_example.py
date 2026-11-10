import json
import boto3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Customer Support API Gateway")

# Initialize the Bedrock AgentCore boto3 client
bedrock_agentcore_client = boto3.client("bedrock-agentcore", region_name="us-east-1")
AGENT_RUNTIME_ARN = "arn:aws:bedrock-agentcore:us-east-1:123456789012:runtime/customer_support_agent-nUpbKY5Ff2"

class ChatRequest(BaseModel):
    prompt: str
    customer_id: str
    session_id: str  # Requires valid session tracking format

@app.post("/api/v1/support/chat")
async def invoke_agent(request: ChatRequest):
    try:
        payload = {
            "prompt": request.prompt,
            "customer_id": request.customer_id,
            "session_id": request.session_id
        }

        # Programmatically invoke the remote AgentCore runtime
        response = bedrock_agentcore_client.invoke_agent_runtime(
            agentRuntimeArn=AGENT_RUNTIME_ARN,
            runtimeSessionId=request.session_id,
            payload=json.dumps(payload)
        )

        response_body = response["body"].read().decode("utf-8")
        return {"status": "success", "data": json.loads(response_body)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  
        

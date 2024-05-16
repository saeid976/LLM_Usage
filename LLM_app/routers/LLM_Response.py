from pydantic import BaseModel
from fastapi import FastAPI, APIRouter, Response
from LLM_Brain.ChatBot import ChatBot
# import json
# app = FastAPI()

class GetGPTResponse(BaseModel):

    user_prompt: str

respond = ChatBot()

router = APIRouter()
@router.post("/gpt_response")
# app = FastAPI()
# @app.post("/gpt_response/", response_model=GetGPTResponse)
def get_features(request: GetGPTResponse):

    result, error = respond.act(user_message=request.user_prompt)

    if error:
        response_content, response_status = error, 501

    else:
        response_content, response_status = result, 200

    return Response(
                    content=response_content,
                    status_code=response_status,
                    media_type="application/json")
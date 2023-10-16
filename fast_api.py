import os
from fastapi import FastAPI
from pydantic import BaseModel
from add_delete_match_intent import add_intent, delete_intent, match_intent
import uvicorn

os.environ["HAYSTACK_TELEMETRY_ENABLED"] = "False"

app = FastAPI()

class intent_request(BaseModel):
    utterance: str

@app.post("/match_intent")
async def get_intent(request: intent_request):
    try:
        response = match_intent(query=request.utterance)

    except Exception:
        return {"state": "failure"}

    return {'intent': response}


class add_request(BaseModel):
    name: str
    examples: list


@app.post('/add_intent')
# @cross_origin()
def _add_intent_(request: add_request):
    try:
        add_intent(intent_name=request.name, examples=request.examples)

    except Exception:
        return {"state": "failure"}

    return {"state": "success"}

class intent_delete_request(BaseModel):
    machine_name: str


@app.post('/delete_intent')
# @cross_origin()
def _delete_intent_(request: intent_delete_request):
    try:
        delete_intent(intent_name=request.machine_name)

    except Exception:
        return {"state": "failure"}

    return {"state": "success"}


if __name__ == '__main__':
    uvicorn.run("fast_api:app", host='0.0.0.0', port=8000, reload=True)


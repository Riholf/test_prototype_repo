# FastAPI is our webframework for the REST API
from fastapi import FastAPI

# Import uvicorn to start the server which runs the fastapi webframework 
import uvicorn

# With the pydantic basemodel you're able to put data into the body of the request
from pydantic import BaseModel

# With requests you're able to send get, http requests to an rest api
import requests


app = FastAPI()

# define class to put text in body
class Text(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Test the swagger API via http://localhost:8000/docs"}

@app.post("/summarisation/")
async def create_summary(text: Text, summary_length: int=50):
    """ Create an extractive summarisation with text rank algorithm within the gensim package.

    Parameters
    ----------
    text : Basemodel
        Basemodel with text that should be summarized.
    summary_length : int
        Length (in words) of the summarisation. # TODO: Think/read about the restrictions of this parameter
    # TODO: Think about other parameters.

    Returns
    -------
    summary : str
        Returns the inferred summary.
    """

    # get the text from the body
    text = text.text

    url = "http://host.docker.internal:8001/summarisation-api"

    
    payload = "{\r\n  \"text\": \"" + text + "\"\r\n}"

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, params={'summary_length': summary_length}, headers=headers, data=payload)

    return response.text

# # DEBUGGING SETUP
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)

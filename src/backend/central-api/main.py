# FastAPI is our webframework for the REST API
from fastapi import FastAPI
# required so that frontend can communicate with backend
from fastapi.middleware.cors import CORSMiddleware

# Import uvicorn to start the server which runs the fastapi webframework 
import uvicorn

# With the pydantic basemodel you're able to put data into the body of the request
from pydantic import BaseModel

# With requests you're able to send get, http requests to an rest api
import requests


app = FastAPI()

origins = [
    "http://localhost:8002",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# define class to put text in body
class Text(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Test the swagger API via http://localhost:8000/docs"}

@app.post("/summarization/")
async def create_summary(text: Text, summary_length: int=50):
    """ Create an extractive summarization with text rank algorithm within the gensim package.

    Parameters
    ----------
    text : Basemodel
        Basemodel with text that should be summarized.
    summary_length : int
        Length (in words) of the summarization. # TODO: Think/read about the restrictions of this parameter
    # TODO: Think about other parameters.

    Returns
    -------
    summary : str
        Returns the inferred summary.
    """

    # get the text from the body
    text = text.text

    url = "http://summary-api:8001/summarization-api/"

    
    payload = "{\r\n  \"text\": \"" + text + "\"\r\n}"

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, params={'summary_length': summary_length}, headers=headers, data=payload)

    return response.text

# # DEBUGGING SETUP
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)

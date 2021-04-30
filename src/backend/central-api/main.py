
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Import uvicorn to start the server which runs the fastapi webframework 
import uvicorn

# With the pydantic basemodel you're able to put data into the body of the request
from pydantic import BaseModel

# With requests you're able to send get, http requests to an rest api
import requests


#IMPORTANT: code wird heute noch von mir (yannick) kommentiert

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# define class to put text in body
class Text(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Test the swagger API via http://localhost:8000/docs"}

@app.get("/summarization/form", response_class=HTMLResponse)
async def summarization(request: Request):
    summary = "Please insert some text in the input-box."
    return templates.TemplateResponse("item.html", context={"request": request, "summary": summary})

@app.post("/summarization/form", response_class=HTMLResponse)
async def summarization(request: Request, txt: str = Form(...), length: int = Form(...)): 

    """ Create an extractive summarization with text rank algorithm within the gensim package.

    Parameters
    ----------
    text : Basemodel
        Basemodel with text that should be summarized.
    summary_length : int
        Length (in words) of the summarization. # TODO: Think/read about the restrictions of this parameter
    # TODO: Think about further parameters.

    Returns
    -------
    summary : str
        Returns the inferred summary.
    """

    url = "http://summary-api:8001/summarization-api/"

    body = {"text": txt}

    response = requests.request("POST", url, params={'summary_length': length}, json = body)
    summary = response.json()

    return templates.TemplateResponse("item.html", context={"request": request, "summary": summary})


# # DEBUGGING SETUP
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8050)

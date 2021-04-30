# FastAPI is our webframework for the REST API
from fastapi import FastAPI, Form

# Import uvicorn to start the server which runs the fastapi webframework 
import uvicorn

# With the pydantic basemodel you're able to put data into the body of the request
from pydantic import BaseModel

# Summariztion Package
from gensim.summarization.summarizer import summarize # https://radimrehurek.com/gensim_3.8.3/summarization/summariser.html

app = FastAPI()

# define class to put text in body
class Summary_Data(BaseModel):
    text: str
    ratio: float


@app.post("/summarization-api/")
async def create_summary(data: Summary_Data):
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
    # get the text and parameter from the body
    text = data.text
    ratio = data.ratio

    result = summarize(text=text, ratio=ratio)
    
    return result

# # DEBUGGING SETUP
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8001)
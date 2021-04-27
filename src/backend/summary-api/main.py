# FastAPI is our webframework for the REST API
from fastapi import FastAPI

# Import uvicorn to start the server which runs the fastapi webframework 
import uvicorn

# With the pydantic basemodel you're able to put data into the body of the request
from pydantic import BaseModel

# Summarisation Package
from gensim.summarization.summarizer import summarize

app = FastAPI()

# define class to put text in body
class Text(BaseModel):
    text: str

@app.post("/summarisation-api/")
async def create_summary(text: Text, summary_length: int=20):
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

    result = summarize(text, word_count=summary_length)
    
    return result

# # DEBUGGING SETUP
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8001)
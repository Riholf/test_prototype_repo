# FastAPI is our webframework for the REST API
from fastapi import FastAPI, Form

# import uvicorn to start the server which runs the fastapi webframework 
import uvicorn

# with the pydantic basemodel you're able to put data into the body of the request
from pydantic import BaseModel

# summariztion package
from gensim.summarization.summarizer import summarize # https://radimrehurek.com/gensim_3.8.3/summarization/summariser.html

app = FastAPI()

# BaseModel with text and ratio to define the expected body in the create_summary function 
class SummaryData(BaseModel):
    text: str
    ratio: float


@app.post("/summarization-api/")
async def create_summary(data: SummaryData):
    """ Create an extractive summarization with text rank algorithm within the gensim package.

    Parameters
    ----------
    data : Basemodel
        Basemodel with text that should be summarized and the additional ratio parameter.

    Returns
    -------
    result : str
        Returns the inferred summary.
    """

    # get the summary with the summarize function
    result = summarize(text=data.text, ratio=data.ratio)
    
    return result

# # DEBUGGING SETUP
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8001)


from fastapi import FastAPI, Request
import uvicorn

from summarizer.summarizer import SimpleSummarizer

app = FastAPI()

@app.post("/summarize")
async def summarize(request: Request):
    """
    API endpoint
    Accepts only post requests.
    Takes text from json in request, making summary of
    it and send back json with text summary
    """
    data = await request.json()
    text = data.get("text", "") # Get the text from json
    summarizer = SimpleSummarizer() # Create an instanse of SimpleSummarizer class
    summary = summarizer.summarize(text) # Generate the text sumamry
    return {"summary": summary} # return summary as json

if __name__ == "__main__":
    uvicorn.run(app)
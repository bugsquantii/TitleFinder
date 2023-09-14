from fastapi import status, FastAPI, Response
from titlefinder import TitleFinder
from pydantic import BaseModel
from base64 import b64decode

app = FastAPI()

class RequestBody(BaseModel):
    url: str


@app.get("/")
def index():
    return {"message": "Hello world!"}


@app.post("/titlefinder")
def get_title(request: RequestBody):

    #Get the url from the request body
    url = request.url
    
    try:
        #Decode the url from base64
        url = b64decode(url).decode('utf-8')
    except:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    
    
    title_finder = TitleFinder()
    title = title_finder.get_title(url)
    return {"title": title}


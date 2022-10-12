from starlette.responses import StreamingResponse
from fastapi import FastAPI, File, UploadFile
import requests

#We generate a new FastAPI app in the Prod environment
#https://fastapi.tiangolo.com/
app = FastAPI()

#Call your get function for a health Check
#to receive both (face-bokeh and face-emotion)
@app.get("/", tags=["Health Check"])
async def root():
    down = ''
    
    try:
        r = requests.get('http://face-bokeh-service-container:8000/')
        if r.status_code != 200:
            down += 'face_bokeh'
    except requests.exceptions.RequestException as e:
        print('\n Cannot reach face-bokeh service.')
        down += "face-bokeh "

    try:
        r = requests.get('http://face-emotion-service-container:8000/')
        if r.status_code != 200:
            down += 'face_emotion'

    except requests.exceptions.RequestException as e:
        print('\n Cannot reach face-emotion service.')
        down += 'face_emotion'

    if down != '':
        return {"message": down+" are down"}

    return {"message": "root is still up and pretty great!"}
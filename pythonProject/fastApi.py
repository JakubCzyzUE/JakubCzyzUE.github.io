from fastapi import FastAPI
import uvicorn
import pickle
from Detector import HOGpersonDetector

app = FastAPI(debug=True)

@app.get('/')
def home():
   return "hello"

if __name__ == '__main__':
    uvicorn.run(app ,host='localhost', port=8000, reload=True, workers=1)
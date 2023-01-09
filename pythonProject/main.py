from Detector import HOGpersonDetector

if __name__ == '__main__':
    HOGpersonDetector('utils/1.jpg')
    HOGpersonDetector('utils/2.jpg')
    HOGpersonDetector('utils/3.jpg')

from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return HOGpersonDetector('utils/1.jpg'), HOGpersonDetector('utils/2.jpg'), HOGpersonDetector('utils/3.jpg')

#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}

from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")


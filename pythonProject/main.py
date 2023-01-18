from Detector import HOGpersonDetector as detector
from starlette.responses import FileResponse

if __name__ == '__main__':
    detector('utils/1.jpg')
    detector('utils/2.jpg')
    detector('utils/3.jpg')

from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/detector")
async def read_root():
    return detector('utils/1.jpg')





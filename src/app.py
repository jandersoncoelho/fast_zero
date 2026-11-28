from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_class=JSONResponse)
def read_root():
    return {"message": "Olá Mundo!"} 
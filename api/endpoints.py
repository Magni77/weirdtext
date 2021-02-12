from fastapi import FastAPI, Response
from fastapi.params import Depends
from pydantic import BaseModel

from api.dependencies import weird_text_service
from weird_text import WeirdText, DecodingError

app = FastAPI(version="v1")


class TextInput(BaseModel):
    text: str


class Result(BaseModel):
    result: str


@app.post("/encode")
def encode(text_input: TextInput, weird_text: WeirdText = Depends(weird_text_service)):
    """
    Accept string text parameters and returns pseudo encrypted string.
    """
    return Result(result=weird_text.encode(text_input.text))


@app.post("/decode")
def decode(text_input: TextInput, weird_text: WeirdText = Depends(weird_text_service)):
    """
    Accept weird formatted text and tries to decode it
    """
    return Result(result=weird_text.decode(text_input.text))


@app.exception_handler(DecodingError)
async def validation_exception_handler(request, exc):
    return Response(str(exc), status_code=400)

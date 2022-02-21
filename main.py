from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn

app = FastAPI()


@app.get('/')
def index():
    return PlainTextResponse('Hi ;)')


if __name__ == '__main__':
    uvicorn.run(app)

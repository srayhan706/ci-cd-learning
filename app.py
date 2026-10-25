import os

from fastapi import FastAPI

app = FastAPI()


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multipication(a, b):
    return a * b


@app.get("/health")
def health():
    return {"status": "ok", "env": os.getenv("APP_ENV", "local"),
            "version": os.getenv("APP_VERSION", "dev")}


@app.get("/add/{a}/{b}")
def add_route(a: int, b: int):
    return {"result": add(a, b)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8000")))

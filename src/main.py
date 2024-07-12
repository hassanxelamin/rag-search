import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"hello": "world"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)

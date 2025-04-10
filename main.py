from fastapi import FastAPI, Request
from play import play
from models import LevelData  # Import LevelData from models

app = FastAPI()

@app.post("/")
async def post(level_data: LevelData):
    return play(level_data)

# Run the application with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        port=3000
    )

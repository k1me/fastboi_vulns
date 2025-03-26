from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import os

app = FastAPI()

# ez a dir ahonnan ki szeretnenk olvasni a file tartalmat
BASE_DIR = "static_files"

# endpoint
@app.get("/read-file/")
async def read_file(filename: str):
    file_path = os.path.join(BASE_DIR, filename)
    
    try:
        with open(file_path, "r") as f:
            return PlainTextResponse(f.read())
    except FileNotFoundError:
        return {"error": "File not found"}

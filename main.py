from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, HTMLResponse
import os

app = FastAPI()

# ez a dir ahonnan ki szeretnenk olvasni a file tartalmat
BASE_DIR = "static_files"

#---------------read endpoint---------------
@app.get("/read-file/")
async def read_file(filename: str):
    file_path = os.path.join(BASE_DIR, filename)
    
    try:
        with open(file_path, "r") as f:
            return PlainTextResponse(f.read())
    except FileNotFoundError:
        return {"error ": "File not found"}
        

#---------------delete endpoint---------------
@app.delete("/delete-file/")
async def delete_file(filename: str):
	file_path = os.path.join(BASE_DIR, filename)
	
	try:
		os.remove(file_path)
		return {"status ": "success ", " message": f"Deleted {filename}"}
	except FileNotFoundError:
		return FileNotFoundError
	except Exception as e:
		return {"error ":str(e)}

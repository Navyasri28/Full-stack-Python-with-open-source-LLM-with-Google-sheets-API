from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Dict
import os
import sheets_util

app = FastAPI(title="Google Sheets Integration API")

# Constant for the Google Sheet URL provided by the user
SHEET_URL = "https://docs.google.com/spreadsheets/d/1qKJ8URimPA9o-3IcWnqjAyXsNhNOeWiqZsi7L3mnhZY/edit?usp=sharing"

class UserData(BaseModel):
    username: str
    password: str

@app.get("/")
async def root():
    return FileResponse("static/index.html")

# Mount static files
if not os.path.exists("static"):
    os.makedirs("static")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/add-user")
async def add_user(data: UserData):
    """Endpoint to add a username and password to the Google Sheet."""
    try:
        row = [data.username, data.password]
        result = sheets_util.add_row(SHEET_URL, row)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users", response_model=List[Dict])
async def get_users():
    """Endpoint to retrieve all users from the Google Sheet."""
    try:
        records = sheets_util.get_all_records(SHEET_URL)
        return records
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete-user/{username}")
async def delete_user(username: str):
    """Endpoint to delete a user from the Google Sheet."""
    try:
        result = sheets_util.delete_row(SHEET_URL, username)
        if result["status"] == "error":
            raise HTTPException(status_code=404, detail=result["message"])
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

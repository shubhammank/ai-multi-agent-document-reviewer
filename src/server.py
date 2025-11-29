from fastapi import FastAPI, UploadFile
from src.app import run_review

app = FastAPI(title="Document Reviewer API")

@app.post("/review")
async def review_document(file: UploadFile):
    path = f"uploads/{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())
    return run_review(path)

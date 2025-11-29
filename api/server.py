import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.app import run_review

app = FastAPI(title="Document Reviewer API", version="1.0.0")

# Create upload folder
os.makedirs("uploads", exist_ok=True)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/review", response_model=dict)
async def review_document(file: UploadFile = File(...)):
    """
    Upload a file and trigger the document review.
    """

    filename = file.filename
    if not filename.lower().endswith((".pdf", ".docx")):
        raise HTTPException(status_code=400, detail="Only PDF or DOCX files allowed.")

    file_path = f"uploads/{filename}"

    # Save file
    try:
        with open(file_path, "wb") as f:
            f.write(await file.read())
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to save uploaded file.")

    try:
        result = run_review(file_path)
        return JSONResponse(content={"success": True, "results": result})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok"}

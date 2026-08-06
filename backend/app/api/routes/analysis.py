from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.pdf_service import pdf_to_text
from app.services.ai_service import ai_analyze
from app.schemas.analysis import AnalysisResponse


router = APIRouter()

@router.post("/analyze",response_model=AnalysisResponse)
async def analyze(
    pdf_data: UploadFile = File(...),
    job_description: str = Form(...)
):


    if pdf_data.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Nur PDF erlaubt")

    if not job_description.strip():
        raise HTTPException(status_code=400, detail="Job Description ist leer")

    pdf_bytes = await pdf_data.read()

    if not pdf_bytes:
        raise HTTPException(status_code=400, detail="Die PDF ist leer.")

    cv_text = pdf_to_text(pdf_bytes)

    try:
        ai_answer =  ai_analyze(cv_text,job_description)
        return ai_answer
    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Die KI Analyse ist momentan nicht verfügbar"
        )


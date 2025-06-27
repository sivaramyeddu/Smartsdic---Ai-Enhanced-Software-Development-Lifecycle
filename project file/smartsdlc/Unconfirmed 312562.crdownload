from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from app.services.ai_services import (
    classify_pdf_text,
    generate_code_from_prompt,
    fix_code,
    summarize_code,
)

router = APIRouter()

class CodeRequest(BaseModel):
    prompt: str
    language: str

class BugFixRequest(BaseModel):
    code: str
    language: str

class SummarizeRequest(BaseModel):
    code: str

@router.post("/classify-requirements")
async def classify_requirements(file: UploadFile = File(...)):
    try:
        result = await classify_pdf_text(file)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate-code")
async def generate_code(req: CodeRequest):
    return generate_code_from_prompt(req.prompt, req.language)

@router.post("/bug-fix")
async def fix_bug(req: BugFixRequest):
    return fix_code(req.code, req.language)

@router.post("/summarize")
async def summarize(req: SummarizeRequest):
    return summarize_code(req.code)

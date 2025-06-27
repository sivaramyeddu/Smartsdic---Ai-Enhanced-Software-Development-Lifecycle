from fastapi import APIRouter
from pydantic import BaseModel
from app.services.feedback_service import store_feedback

router = APIRouter()

class FeedbackRequest(BaseModel):
    module: str
    rating: int  # 1 to 5
    comment: str = ""

@router.post("/submit")
def submit_feedback(feedback: FeedbackRequest):
    store_feedback(feedback)
    return {"status": "Feedback received. Thank you!"}
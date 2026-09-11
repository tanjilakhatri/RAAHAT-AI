from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.inference import run_inference


app = FastAPI(
    title="RAAHAT AI Service",
    description="AI-based non-clinical stress and distress vulnerability indicator",
    version="1.0.0",
)


class PredictionRequest(BaseModel):
    text: str


@app.get("/")
def health_check():
    return {
        "service": "RAAHAT AI",
        "status": "running",
        "diagnostic": False,
    }


@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        result = run_inference(request.text)
        return result

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="AI inference failed.",
        )
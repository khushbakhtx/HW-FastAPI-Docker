import warnings
from typing import Dict

from app.dto.dto import ModelInput, ModelOutput
from fastapi import FastAPI
from app.model.engine import Model
from app.preprocessing.data_preprocessing import calculate_features

warnings.filterwarnings("ignore")

import os
import sys

if os.path.dirname(os.path.abspath(__file__)) not in sys.path:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()

col_names_and_order = [
    "Age", "Sex", "RestingBP", "Cholesterol", "FastingBS", "MaxHR", "ExerciseAngina", "Oldpeak",
    "chest_pain_ASY", "chest_pain_ATA", "chest_pain_NAP", "chest_pain_TA",
    "restingECG_LVH", "restingECG_Normal", "restingECG_ST",
    "st_slope_Down", "st_slope_Flat", "st_slope_Up"
]
model_path = "./artefacts/catboost-estimated-model.joblib"


@app.get("/readiness")
async def health_check() -> Dict:

    return {"status": "success"}


@app.post("/predict")
async def get_predictions(input_data: ModelInput):

    model = Model(model_path)
    
    preprocessed = calculate_features(input_data.dict(), col_names_and_order)
    final_data = [list(v.values()) for v in preprocessed]   
    preds = model.infer(final_data)    
    model_name = os.path.basename(model_path)    
    output = ModelOutput(predictions=preds.tolist(), model_name=model_name)
    return output

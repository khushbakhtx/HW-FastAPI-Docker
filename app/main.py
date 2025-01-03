import warnings
from typing import Dict

from app.dto.dto import ModelInput, ModelOutput
from fastapi import FastAPI
from app.model.engine import Model
from app.preprocessing.prepare_data import calculate_feautres

warnings.filterwarnings('ignore')

import os
import sys

if os.path.dirname(os.path.abspath(__file__)) not in sys.path:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()

col_names_and_order = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
model_path = '/app/app/artefacts/catboost_model.pkl'


@app.get("/readiness")
async def health_check() -> Dict:
    return {'status': 'success'}


@app.post("/predict")
async def get_predictions(input_data: ModelInput):
    model = Model(model_path)
    preprocessed = calculate_feautres(input_data.dict(), col_names_and_order)
    final_data = [list(v.values()) for v in preprocessed]
    preds = model.infer(final_data)
    model_name = model_path.split('/')[-1]
    output = ModelOutput(predictions=preds.tolist(), model_name=model_name)
    return output

import joblib
from typing import List, Union

import numpy as np
import pandas as pd
from catboost import CatBoostClassifier


class Model:
    def __init__(self, model_path: str) -> None:

        self.model_path = model_path
        self.model = None

    def _load_model(self) -> CatBoostClassifier:

        if self.model is None: 
            self.model = joblib.load(self.model_path)

    def infer(self, input_data: Union[pd.DataFrame, np.ndarray, List]) -> np.ndarray:

        self._load_model()
        output = self.model.predict(input_data)
        return output

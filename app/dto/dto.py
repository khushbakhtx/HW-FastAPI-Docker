from typing import Union
from pydantic import BaseModel, ConfigDict


class ModelInput(BaseModel):
    Age: Union[float, int]
    Sex: Union[float, int]  
    RestingBP: Union[float, int]
    Cholesterol: Union[float, int]
    FastingBS: Union[float, int]  
    MaxHR: Union[float, int]
    ExerciseAngina: Union[float, int]  
    Oldpeak: Union[float, int]
    chest_pain_ASY: Union[float, int]
    chest_pain_ATA: Union[float, int]
    chest_pain_NAP: Union[float, int]
    chest_pain_TA: Union[float, int]
    restingECG_LVH: Union[float, int]
    restingECG_Normal: Union[float, int]
    restingECG_ST: Union[float, int]
    st_slope_Down: Union[float, int]
    st_slope_Flat: Union[float, int]
    st_slope_Up: Union[float, int]

    model_config = ConfigDict(arbitrary_types_allowed=True)


class ModelOutput(BaseModel):
    
    prediction: int
    model_name: str 

    model_config = ConfigDict(arbitrary_types_allowed=True)

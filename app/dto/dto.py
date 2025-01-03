from typing import Union

from pydantic import BaseModel, ConfigDict


class ModelInput(BaseModel):
    sepal_length: Union[float, int, list]
    sepal_width: Union[float, int, list]
    petal_length: Union[float, int, list]
    petal_width: Union[float, int, list]

    model_config = ConfigDict(arbitrary_types_allowed=True)


class ModelOutput(BaseModel):
    predictions: Union[int, list]
    model_name: str

    model_config = ConfigDict(arbitrary_types_allowed=True)

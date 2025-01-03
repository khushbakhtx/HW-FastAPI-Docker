from typing import Dict, List, Union

import numpy as np
import pandas as pd


def calculate_feautres(
    input_data: Union[Dict, pd.DataFrame, np.array, List], col_names: List[str] = None
):

    try:
        df = pd.DataFrame.from_dict(input_data, orient='index').T
    except Exception as e:
        raise ValueError(
            f"Incorrect value supplied for preprocessing: input:{input_data}, error: {e}"
        )

    # feature calculation generation
    df['petal_length_squared'] = df['petal_length'] ** 2
    df['petal_width_squared'] = df['petal_width'] ** 2

    return df.to_dict(orient='records')

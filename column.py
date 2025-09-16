import pandas as pd

def detect_column_types(df, threshold=20):
    result = {}

    for column in df.columns:
        dtype = df[column].dtype

        if dtype == 'object':
            avg_len = df[column].dropna().astype(str).map(len).mean()
            if avg_len > 30:
                result[column] = "text"
            else:
                result[column] = "categorical"
        elif pd.api.types.is_numeric_dtype(dtype):
            unique_count = df[column].nunique()
            if unique_count <= threshold:
                result[column] = "categorical"
            else:
                result[column] = "numerical"
        else:
            result[column] = "categorical"

    return result

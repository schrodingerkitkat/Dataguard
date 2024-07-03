"""
Helper functions for DataGuard.
"""

import pandas as pd
from typing import Any, Callable, List
from concurrent.futures import ProcessPoolExecutor, as_completed
import json
import yaml

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data from various file formats into a pandas DataFrame.
    """
    file_extension = file_path.split('.')[-1].lower()

    if file_extension == 'csv':
        return pd.read_csv(file_path)
    elif file_extension == 'json':
        return pd.read_json(file_path)
    elif file_extension in ['xls', 'xlsx']:
        return pd.read_excel(file_path)
    elif file_extension == 'parquet':
        return pd.read_parquet(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}")

def generate_report(errors: List[str], output_format: str = 'json') -> str:
    """
    Generate a validation report in the specified format.
    """
    report = {
        "validation_status": "Failed" if errors else "Passed",
        "error_count": len(errors),
        "errors": errors
    }

    if output_format == 'json':
        return json.dumps(report, indent=2)
    elif output_format == 'yaml':
        return yaml.dump(report, default_flow_style=False)
    else:
        raise ValueError(f"Unsupported output format: {output_format}")

def parallelize_dataframe(df: pd.DataFrame, func: Callable[[pd.DataFrame], Any], n_cores: int = 4) -> List[Any]:
    """
    Apply a function to a DataFrame in parallel using multiple cores.
    """
    df_split = np.array_split(df, n_cores)
    
    with ProcessPoolExecutor(max_workers=n_cores) as executor:
        futures = [executor.submit(func, df_chunk) for df_chunk in df_split]
        results = [future.result() for future in as_completed(futures)]
    
    return results


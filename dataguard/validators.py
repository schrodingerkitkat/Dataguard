"""
Core validation logic and built-in rules for DataGuard.
"""

import pandas as pd
from typing import Any, Callable, Dict, List, Optional, Union
from .exceptions import ValidationError, RuleDefinitionError
from .utils import parallelize_dataframe

class DataValidator:
    def __init__(self):
        self.rules = {}
        self.errors = []

    def add_rule(self, column: str, rule: Callable[[Any], bool], error_message: str):
        """
        Add a validation rule for a specific column.
        """
        if column not in self.rules:
            self.rules[column] = []
        self.rules[column].append((rule, error_message))

    def validate(self, data: pd.DataFrame, parallel: bool = False) -> bool:
        """
        Validate the entire DataFrame against all defined rules.
        """
        self.errors = []

        if parallel:
            return self._validate_parallel(data)
        else:
            return self._validate_sequential(data)

    def _validate_sequential(self, data: pd.DataFrame) -> bool:
        for column, rules in self.rules.items():
            if column not in data.columns:
                self.errors.append(f"Column '{column}' not found in the dataset.")
                continue

            for rule, error_message in rules:
                mask = ~data[column].apply(rule)
                if mask.any():
                    error_indices = data.index[mask].tolist()
                    self.errors.append(f"{error_message} in column '{column}' at indices: {error_indices}")

        return len(self.errors) == 0

    def _validate_parallel(self, data: pd.DataFrame) -> bool:
        def apply_rules(df: pd.DataFrame) -> List[str]:
            chunk_errors = []
            for column, rules in self.rules.items():
                if column not in df.columns:
                    chunk_errors.append(f"Column '{column}' not found in the dataset.")
                    continue

                for rule, error_message in rules:
                    mask = ~df[column].apply(rule)
                    if mask.any():
                        error_indices = df.index[mask].tolist()
                        chunk_errors.append(f"{error_message} in column '{column}' at indices: {error_indices}")
            return chunk_errors

        chunk_errors = parallelize_dataframe(data, apply_rules)
        self.errors = [error for chunk in chunk_errors for error in chunk]

        return len(self.errors) == 0

    def get_errors(self) -> List[str]:
        """
        Return all validation errors.
        """
        return self.errors

# Built-in validation rules
def is_not_null(value: Any) -> bool:
    return pd.notna(value)

def is_unique(value: Any) -> bool:
    return True  # This will be checked at the DataFrame level

def is_in_range(min_value: Union[int, float], max_value: Union[int, float]) -> Callable[[Any], bool]:
    def _is_in_range(value: Any) -> bool:
        return min_value <= value <= max_value
    return _is_in_range

def matches_regex(pattern: str) -> Callable[[Any], bool]:
    import re
    compiled_pattern = re.compile(pattern)
    return lambda value: bool(compiled_pattern.match(str(value)))

def is_of_type(data_type: type) -> Callable[[Any], bool]:
    return lambda value: isinstance(value, data_type)
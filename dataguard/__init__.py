"""
DataGuard: Robust Data Validation for Modern ETL Pipelines
"""

__version__ = "0.1.0"
__author__ = "DataGuard Contributors"
__license__ = "MIT"

from .validators import DataValidator
from .exceptions import (
    ValidationError,
    RuleDefinitionError,
    DataSourceError,
)
from .utils import (
    load_data,
    generate_report,
)

__all__ = [
    "DataValidator",
    "ValidationError",
    "RuleDefinitionError",
    "DataSourceError",
    "load_data",
    "generate_report",
]
"""
Custom exception classes for DataGuard.
"""

class ValidationError(Exception):
    """
    Raised when data fails validation checks.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class RuleDefinitionError(Exception):
    """
    Raised when there's an issue with defining a validation rule.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class DataSourceError(Exception):
    """
    Raised when there's an issue with the data source.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
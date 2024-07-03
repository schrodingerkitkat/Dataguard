
# DataGuard: Robust Data Validation for Modern ETL Pipelines



[![PyPI version](https://badge.fury.io/py/dataguard.svg)](https://badge.fury.io/py/dataguard)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/schrodingerkitkat/dataguard.svg?branch=main)](https://travis-ci.org/yourusername/dataguard)
[![Coverage Status](https://coveralls.io/repos/github/schrodingerkitkat/dataguard/badge.svg?branch=main)](https://coveralls.io/github/yourusername/dataguard?branch=main)

DataGuard is a comprehensive, flexible, and easy-to-use Python library for implementing robust data validation checks within ETL pipelines, ensuring data quality and reliability.

## Features

- **Declarative Validation:** Define validation rules using a clear, expressive syntax
- **Extensible Rule Set:** Rich library of built-in validation rules with easy extensibility for custom rules
- **Data Source Agnostic:** Support validation across various data sources (CSV, JSON, Parquet, databases) with a unified interface
- **Pipeline Integration:** Seamless integration with popular ETL frameworks like Apache Airflow, Prefect, or within standalone Python scripts
- **Error Handling and Reporting:** Flexible options for handling validation failures with detailed, actionable validation reports
- **Performance Optimization:** Efficient validation logic with support for parallel processing on large datasets

## Installation

Install DataGuard using pip:

```bash
pip install dataguard
```

## Quick Start

Here's a simple example to get you started with DataGuard:

```python
from dataguard import DataValidator, load_data, generate_report

# Load your data
df = load_data('path/to/your/data.csv')

# Create a validator
validator = DataValidator()

# Add some rules
validator.add_rule('age', lambda x: x >= 0, "Age must be non-negative")
validator.add_rule('email', lambda x: '@' in x, "Invalid email format")

# Validate the data
is_valid = validator.validate(df)

if not is_valid:
    errors = validator.get_errors()
    report = generate_report(errors, output_format='json')
    print(report)
```

## Documentation

For full documentation, including API reference and advanced usage examples, visit our [documentation site](https://dataguard.readthedocs.io).

## Contributing

We welcome contributions to DataGuard! Please see our [Contributing Guide](CONTRIBUTING.md) for more details on how to get started.

## License

DataGuard is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Support

If you encounter any problems or have any questions, please [open an issue](https://github.com/schrodingerkitkat/dataguard/issues/new) on GitHub.

## Roadmap

We're constantly working to improve DataGuard. Here are some features we're planning for future releases:

- Schema Validation: Ability to validate data against schemas defined in formats like JSON Schema or Avro
- Data Drift Detection: Implement statistical methods to detect changes in data patterns over time
- Machine Learning Integration: Explore the use of ML models for anomaly detection or more complex validation rules
- Visualization: Provide tools or integrations to visualize validation results and data quality trends

Stay tuned for updates!


---

DataGuard - Ensuring the integrity of your data, one pipeline at a time.

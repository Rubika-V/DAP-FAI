# Data Acquisition and Integration Pipeline

## Overview

This project implements a Python-based data acquisition pipeline that
integrates data from multiple sources into a unified analytical dataset.

The pipeline handles:

- CSV sales data
- Excel employee correction data
- JSON website logs
- Weather API data
- Large-scale CSV processing
- API schema change detection and handling

## Technologies Used

- Python
- Pandas
- JSON
- OpenPyXL
- Pytest

## Data Sources

1. Sales data – CSV
2. Employee data – Excel
3. Website logs – JSON
4. Weather data – JSON representation of API response

## Large Dataset Processing

The pipeline demonstrates processing of 5 million sales records using
chunk-based processing.

The CSV is processed in chunks of 100,000 records instead of loading
the entire dataset into memory.

## Schema Drift Handling

The expected weather fields are:

- date
- location
- temperature
- rainfall

If the API changes fields such as:

temperature → temp
rainfall → rain

the pipeline detects the change and maps the known fields to the
standard schema.

## Testing

Automated tests are implemented using Pytest.

The tests verify:

- Sales data availability
- Weather schema validation
- Handling of changed weather field names

## How to Run

Install dependencies:

    pip install -r requirements.txt

Run the main pipeline:

    python main.py

Run large-data processing:

    python process_large_data.py

Run tests:

    python -m pytest
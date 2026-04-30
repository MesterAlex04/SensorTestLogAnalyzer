# Sensor Test Log Analyzer

A lightweight Python automation tool designed to parse, validate, and report hardware sensor data. This utility is built to assist QA Engineers in identifying faulty components by analyzing telemetry logs (CSV) and generating structured error reports (JSON).

## 1. Features
- **CSV Data Ingestion:** Reads raw sensor data including IDs, temperature, and voltage.
- **Automated Validation:** Checks data against predefined safety thresholds (e.g., Max Temperature, Min Voltage).
- **Structured Reporting:** Exports all detected "failed tests" into a clean JSON format for traceability.
- **Clean Architecture:** Modular design with separate functions for ingestion, processing, and reporting.

## 2. Tech Stack
- **Language:** Python 3.x
- **Libraries:** `csv`, `json` (Standard Library)

## 3. How It Works
The script follows a standard data pipeline:
1. **Ingestion:** Loads the `raw_sensor_data.csv` file.
2. **Analysis:** Iterates through each record, converting strings to floats and comparing them against safety constants.
3. **Filtering:** Items exceeding 80°C or dropping below 3.3V are flagged.
4. **Output:** A file named `failed_tests.json` is generated with all anomalous records.

## 4. Usage
1. Ensure you have a file named `raw_sensor_data.csv` in the root folder.
2. Run the script:
``bash
  python main.py``
3. Check failed_tests.json for the results.
   
## 5. Sample input (CSV)
  sensor_id,temperature,voltage
  S1,45.2,5.0
  S2,85.0,4.8
  S3,40.0,3.1

# Smart File & Data Automation Tool

## About
A Python project that cleans customer data stored in a CSV file.

## Features
- Reads customer data from a CSV file.
- Removes duplicate email records.
- Skips records with missing email addresses.
- Generates a cleaned CSV file.
- Creates a text report with processing statistics.
- Handles missing input files and invalid CSV columns.

## Technologies
- Python
- CSV module
- pathlib
- datetime

## Project Files
- `main.py` — Main automation script
- `customers.csv` — Sample input data
- `cleaned_customers.csv` — Cleaned output data
- `report.txt` — Processing report

## How to Run
1. Install Python 3.
2. Open a terminal in the project folder.
3. Run:

   `python main.py`

## Expected Results
- Valid unique records: 3
- Duplicate records removed: 1
- Missing-email records skipped: 1

## Note
The sample data is fictional and intended for demonstration purposes.
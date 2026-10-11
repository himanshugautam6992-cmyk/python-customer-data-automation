
import csv
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent
INPUT_FILE = BASE_DIR / "customers.csv"
OUTPUT_FILE = BASE_DIR / "cleaned_customers.csv"
REPORT_FILE = BASE_DIR / "report.txt"


def clean_customer_data():
    if not INPUT_FILE.exists():
        print("Error: customers.csv not found.")
        return

    seen_emails = set()
    cleaned_rows = []
    duplicate_count = 0
    missing_email_count = 0

    try:
        with INPUT_FILE.open(
            "r", newline="", encoding="utf-8-sig"
        ) as file:
            reader = csv.DictReader(file)

            required = {"name", "email", "city"}
            if not reader.fieldnames or not required.issubset(
                reader.fieldnames
            ):
                print("Error: CSV columns must be name,email,city.")
                return

            for row in reader:
                email = (row.get("email") or "").strip().lower()

                if not email:
                    missing_email_count += 1
                    continue

                if email in seen_emails:
                    duplicate_count += 1
                    continue

                seen_emails.add(email)
                cleaned_rows.append({
                    "name": (row.get("name") or "").strip(),
                    "email": email,
                    "city": (row.get("city") or "").strip()
                })

        with OUTPUT_FILE.open(
            "w", newline="", encoding="utf-8"
        ) as file:
            writer = csv.DictWriter(
                file, fieldnames=["name", "email", "city"]
            )
            writer.writeheader()
            writer.writerows(cleaned_rows)

        report = (
            "CUSTOMER DATA AUTOMATION REPORT\n"
            f"Generated: {datetime.now():%Y-%m-%d %H:%M:%S}\n"
            f"Valid unique records: {len(cleaned_rows)}\n"
            f"Duplicate records removed: {duplicate_count}\n"
            f"Missing-email records skipped: {missing_email_count}\n"
        )

        REPORT_FILE.write_text(report, encoding="utf-8")

        print("Automation completed successfully!")
        print(f"Cleaned records: {len(cleaned_rows)}")
        print(f"Duplicates removed: {duplicate_count}")
        print(f"Missing emails: {missing_email_count}")
        print(f"Output: {OUTPUT_FILE}")
        print(f"Report: {REPORT_FILE}")

    except (OSError, csv.Error, UnicodeError) as error:
        print(f"Processing error: {error}")


if __name__ == "__main__":
    clean_customer_data()

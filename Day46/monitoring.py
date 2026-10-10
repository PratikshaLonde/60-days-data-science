
import logging
from pathlib import Path
from datetime import datetime

import pandas as pd

# 1. LOGGING CONFIGURATION

LOG_DIR = Path(__file__).resolve().parent
LOG_FILE = LOG_DIR / "customer_monitoring.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


# 2. LOGGING FUNCTIONS

def log_event(message):
    logger.info(message)


def log_error(message):
    logger.error(message)


# 3. DATA VALIDATION

def validate_customer_data(data):
    required_columns = ["sales", "profit"]

    if data.empty:
        log_error("Dataset is empty.")
        return False

    missing_columns = [
        column for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        log_error(f"Missing required columns: {missing_columns}")
        return False

    for column in required_columns:
        numeric_values = pd.to_numeric(
            data[column], errors="coerce"
        )

        if numeric_values.isna().any():
            log_error(
                f"Missing or invalid numeric values in {column}."
            )
            return False

    log_event(
        f"Dataset validation successful. Rows: {len(data)}"
    )
    return True


# 4. MONITORING SUMMARY

def log_monitoring_summary(data):
    log_event(
        f"Monitoring summary | Rows: {len(data)} | "
        f"Columns: {len(data.columns)}"
    )

    sales = pd.to_numeric(data["sales"], errors="coerce")
    profit = pd.to_numeric(data["profit"], errors="coerce")

    log_event(f"Total sales: {sales.sum():.2f}")
    log_event(f"Total profit: {profit.sum():.2f}")


# 5. TRACK MONITORING REQUESTS

def monitor_request(request_name, data):
    request_id = datetime.now().strftime("%Y%m%d%H%M%S%f")

    log_event(
        f"Request started | ID: {request_id} | "
        f"Name: {request_name}"
    )

    try:
        if not validate_customer_data(data):
            log_error(
                f"Request failed validation | ID: {request_id}"
            )
            return False

        log_monitoring_summary(data)

        log_event(
            f"Request completed successfully | ID: {request_id}"
        )
        return True

    except Exception:
        logger.exception(
            f"Unexpected request failure | ID: {request_id}"
        )
        return False


# 6. LOAD AND MONITOR DATASET

def main():
    log_event("Customer Intelligence monitoring started.")

    dataset_path = (
        Path(__file__).resolve().parent.parent
        / "cleaned_dataset.csv"
    )

    try:
        log_event(f"Loading dataset: {dataset_path}")

        data = pd.read_csv(dataset_path)

        print("Dataset loaded successfully!")
        print(f"Rows: {len(data)}")
        print(f"Columns: {len(data.columns)}")

        success = monitor_request(
            "Customer dataset validation",
            data,
        )

        if success:
            print("\nReal dataset validation passed!")
            print("Monitoring completed successfully.")
        else:
            print("\nDataset validation failed.")
            print("Check the monitoring log for details.")

    except FileNotFoundError:
        log_error(f"Dataset file not found: {dataset_path}")
        print("Dataset file not found. Check the file path.")

    except pd.errors.EmptyDataError:
        log_error("Dataset file is empty.")
        print("Dataset file is empty.")

    except pd.errors.ParserError:
        logger.exception("Unable to parse the CSV dataset.")
        print("CSV format error. Check the dataset.")

    except Exception:
        logger.exception(
            "Unexpected error while monitoring dataset."
        )
        print("An unexpected error occurred. Check the log file.")

    print(f"\nLog file: {LOG_FILE}")


if __name__ == "__main__":
    main()

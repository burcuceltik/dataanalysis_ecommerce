from pathlib import Path

import pandas as pd

from config import RAW_DATA_DIR


def summarize_csv(path: Path) -> dict:
    df = pd.read_csv(path)
    return {
        "file": path.name,
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": list(df.columns),
        "missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
    }


def main() -> None:
    csv_files = sorted(RAW_DATA_DIR.glob("*.csv"))

    if not csv_files:
        print(f"No CSV files found in {RAW_DATA_DIR}")
        print("Download the Olist dataset and place the CSV files in data/raw/.")
        return

    summaries = [summarize_csv(path) for path in csv_files]
    summary_df = pd.DataFrame(summaries)
    print(summary_df[["file", "rows", "columns", "missing_values", "duplicate_rows"]])


if __name__ == "__main__":
    main()

from pathlib import Path

import pandas as pd

from config import RAW_DATA_DIR, PROJECT_ROOT


OUTPUT_PATH = PROJECT_ROOT / "docs" / "data_overview.md"


def load_csv_files() -> list[Path]:
    return sorted(RAW_DATA_DIR.glob("*.csv"))


def summarize_file(path: Path) -> dict:
    df = pd.read_csv(path)
    return {
        "file": path.name,
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "column_names": ", ".join(df.columns),
    }


def build_markdown(summary_df: pd.DataFrame) -> str:
    table_columns = ["file", "rows", "columns", "missing_values", "duplicate_rows"]
    table_lines = [
        "| " + " | ".join(table_columns) + " |",
        "| " + " | ".join("---" for _ in table_columns) + " |",
    ]
    for row in summary_df[table_columns].to_dict("records"):
        table_lines.append("| " + " | ".join(str(row[column]) for column in table_columns) + " |")
    table = "\n".join(table_lines)

    column_sections = []
    for row in summary_df.to_dict("records"):
        column_sections.append(f"### {row['file']}\n\n{row['column_names']}\n")

    return "\n".join(
        [
            "# Data Overview",
            "",
            "This file is generated from the CSV files in `data/raw/`.",
            "",
            "## Table Summary",
            "",
            table,
            "",
            "## Columns",
            "",
            "\n".join(column_sections),
        ]
    )


def main() -> None:
    csv_files = load_csv_files()
    if not csv_files:
        raise FileNotFoundError("No CSV files found in data/raw/.")

    summary_df = pd.DataFrame(summarize_file(path) for path in csv_files)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(build_markdown(summary_df), encoding="utf-8")
    print(f"Data overview written to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

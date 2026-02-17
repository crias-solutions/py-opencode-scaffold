"""Voltage Data Processor - Load, clean, and visualize voltage data from Excel files."""

import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd


def load_excel_data(file_path: Path) -> pd.DataFrame:
    """Load voltage data from Excel file using XML parsing to avoid styling issues.

    Args:
        file_path: Path to the Excel file.

    Returns:
        DataFrame with columns: Timestamp, voltage_1, voltage_2, voltage_3
    """
    ns = {"main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}

    rows_data = []
    with zipfile.ZipFile(file_path, "r") as z:
        with z.open("xl/worksheets/sheet1.xml") as f:
            tree = ET.parse(f)
            root = tree.getroot()

            for row in root.findall(".//main:row", ns):
                cells = row.findall("main:c", ns)
                row_values = []
                for c in cells:
                    is_elem = c.find("main:is", ns)
                    if is_elem is not None:
                        t = is_elem.find("main:t", ns)
                        if t is not None and t.text:
                            row_values.append(t.text)
                            continue
                    v = c.find("main:v", ns)
                    if v is not None and v.text:
                        row_values.append(v.text)
                    else:
                        row_values.append("")

                if row_values:
                    rows_data.append(row_values)

    if not rows_data:
        msg = "No data found in Excel file"
        raise ValueError(msg)

    headers = rows_data[0]
    data_rows = rows_data[1:]

    df = pd.DataFrame(data_rows, columns=headers)
    df.columns = ["Timestamp", "voltage_1", "voltage_2", "voltage_3"]

    for col in ["voltage_1", "voltage_2", "voltage_3"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["Timestamp"] = pd.to_numeric(df["Timestamp"], errors="coerce")
    df = df.dropna()

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean voltage data by interpolating missing values.

    Args:
        df: DataFrame with voltage data.

    Returns:
        Cleaned DataFrame with interpolated values.
    """
    voltage_cols = ["voltage_1", "voltage_2", "voltage_3"]

    missing_before = df[voltage_cols].isna().sum().sum()
    if missing_before > 0:
        df[voltage_cols] = df[voltage_cols].interpolate(method="linear")
        df[voltage_cols] = df[voltage_cols].bfill().ffill()

    return df


def visualize(df: pd.DataFrame, output_path: Path, show: bool = True) -> None:
    """Create time series visualization of voltage data.

    Args:
        df: DataFrame with voltage data.
        output_path: Path to save the plot.
        show: Whether to display the plot.
    """
    fig, ax = plt.subplots(figsize=(14, 6))

    ax.plot(df.index, df["voltage_1"], label="Voltage 1", alpha=0.8)
    ax.plot(df.index, df["voltage_2"], label="Voltage 2", alpha=0.8)
    ax.plot(df.index, df["voltage_3"], label="Voltage 3", alpha=0.8)

    ax.set_xlabel("Sample Index")
    ax.set_ylabel("Voltage")
    ax.set_title("Voltage Data Over Time")
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    print(f"Plot saved to: {output_path}")

    if show:
        plt.show()

    plt.close()


def main() -> dict[str, Any]:
    """Main function to process voltage data for all Raw_Data_*.xlsx files."""
    data_dir = Path("data")
    input_files = sorted(data_dir.glob("Raw_Data_*.xlsx"))

    if not input_files:
        msg = "No Raw_Data_*.xlsx files found in data directory"
        raise FileNotFoundError(msg)

    results = {}
    for input_file in input_files:
        print(f"\n{'=' * 50}")
        print(f"Processing: {input_file.name}")
        print("=" * 50)

        output_csv = data_dir / f"cleaned_{input_file.stem}.csv"
        output_plot = data_dir / f"plot_{input_file.stem}.png"

        print(f"Loading data from: {input_file}")
        df = load_excel_data(input_file)
        print(f"Loaded {len(df)} rows")

        print("Cleaning data...")
        df = clean_data(df)

        print(f"Saving cleaned data to: {output_csv}")
        df.to_csv(output_csv, index=False)

        print("Creating visualization...")
        visualize(df, output_plot, show=False)

        results[input_file.name] = {
            "rows_processed": len(df),
            "output_csv": str(output_csv),
            "output_plot": str(output_plot),
        }

    return results


if __name__ == "__main__":
    result = main()
    print(f"\nProcessing complete: {result}")

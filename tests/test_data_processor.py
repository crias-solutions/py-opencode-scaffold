"""Tests for voltage data processor."""

import zipfile
from pathlib import Path

import pandas as pd
import pytest  # noqa: F401

from src.data_processor import clean_data, load_excel_data, visualize


def create_test_excel(path: Path, data: list[list[str]]) -> None:
    """Create a minimal xlsx file for testing."""
    ns = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"

    rows_xml = ""
    for i, row in enumerate(data):
        row_num = i + 1
        cells_xml = ""
        for j, val in enumerate(row):
            col_letter = chr(65 + j)
            cells_xml += f'<c r="{col_letter}{row_num}"><v>{val}</v></c>'
        rows_xml += f'<row r="{row_num}">{cells_xml}</row>'

    sheet_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="{ns}">
<sheetData>
{rows_xml}
</sheetData>
</worksheet>'''

    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
</Types>"""

    workbook_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
</Relationships>"""

    workbook = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="{ns}">
<sheets>
<sheet name="sheet1" sheetId="1" r:id="rId1" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>
</sheets>
</workbook>"""

    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", workbook_rels)
        z.writestr("xl/workbook.xml", workbook)
        z.writestr("xl/worksheets/sheet1.xml", sheet_xml)
        z.writestr("xl/_rels/workbook.xml.rels", workbook_rels)


class TestLoadExcelData:
    """Tests for load_excel_data function."""

    def test_load_valid_excel(self, tmp_path: Path) -> None:
        """Test loading valid Excel file."""
        test_data = [
            ["Timestamp", "Voltage_0", "Voltage_1", "Voltage_2"],
            ["1.0", "0.1", "0.2", "0.3"],
            ["2.0", "0.4", "0.5", "0.6"],
        ]
        test_file = tmp_path / "test.xlsx"
        create_test_excel(test_file, test_data)

        df = load_excel_data(test_file)

        assert len(df) == 2
        assert "voltage_1" in df.columns
        assert "voltage_2" in df.columns
        assert "voltage_3" in df.columns
        assert df["voltage_1"].iloc[0] == 0.1

    def test_load_empty_file_returns_empty_df(self, tmp_path: Path) -> None:
        """Test that file with only header returns empty DataFrame."""
        test_data = [["Timestamp", "Voltage_0", "Voltage_1", "Voltage_2"]]
        test_file = tmp_path / "test.xlsx"
        create_test_excel(test_file, test_data)

        df = load_excel_data(test_file)

        assert len(df) == 0


class TestCleanData:
    """Tests for clean_data function."""

    def test_clean_no_changes_needed(self) -> None:
        """Test cleaning data with no missing values."""
        df = pd.DataFrame(
            {
                "voltage_1": [1.0, 2.0, 3.0],
                "voltage_2": [4.0, 5.0, 6.0],
                "voltage_3": [7.0, 8.0, 9.0],
            }
        )

        result = clean_data(df)

        assert result["voltage_1"].tolist() == [1.0, 2.0, 3.0]

    def test_clean_interpolates_missing(self) -> None:
        """Test that missing values are interpolated."""
        df = pd.DataFrame(
            {
                "voltage_1": [1.0, None, 3.0],
                "voltage_2": [4.0, 5.0, 6.0],
                "voltage_3": [7.0, 8.0, 9.0],
            }
        )

        result = clean_data(df)

        assert result["voltage_1"].iloc[1] == 2.0


class TestVisualize:
    """Tests for visualize function."""

    def test_visualize_saves_file(self, tmp_path: Path) -> None:
        """Test that visualization saves a file."""
        df = pd.DataFrame(
            {
                "voltage_1": [1.0, 2.0, 3.0],
                "voltage_2": [4.0, 5.0, 6.0],
                "voltage_3": [7.0, 8.0, 9.0],
            }
        )
        output_path = tmp_path / "test_plot.png"

        visualize(df, output_path, show=False)

        assert output_path.exists()
        assert output_path.stat().st_size > 0

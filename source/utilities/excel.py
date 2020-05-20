import pandas as pd
from openpyxl import load_workbook
from source.utilities import globals


def get_sheet(sheet):
    data = pd.read_excel(globals.EXCEL, sheet_name=sheet, index_col=globals.INDEX_COLUMN)
    return data


def get_value(sheet, row_name, col_name):
    data = get_sheet(sheet)
    value = data.loc[row_name, col_name]
    return value


def write_to_excel(sheet, row_name, column_name, value_to_write):
    data = get_sheet(sheet)
    data.loc[row_name, column_name] = value_to_write
    writer = pd.ExcelWriter(globals.EXCEL_PATH)
    workbook = load_workbook(globals.EXCEL_PATH)
    writer.book = workbook
    writer.sheets = dict((ws.title, ws) for ws in workbook.worksheets)
    data.to_excel(writer, sheet_name=sheet, index=False)
    writer.save()

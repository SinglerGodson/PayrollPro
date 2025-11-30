import json

import pandas
from openpyxl.reader.excel import load_workbook

user_id_col = 38
config = {
        "教职工": {
            "header_row": 3,
            "index_col": 1, # 序号列
            "skip_cols": lambda i: i in (1, 3, 4, 38) or i > 28
        },
        "管理人员": {
            "header_row": 5,
            "index_col": 0, # 序号列
            "skip_cols": lambda i: i == 0 or i > 22
        },
        "工勤人员（校医、教官等）": {
            "header_row": 3,
            "index_col": 0, # 序号列
            "skip_cols": lambda i:i == 0 or i > 21
        },
        "校长": {
            "header_row": 5,
            "index_col": 0, # 序号列
            "skip_cols": lambda i: i == 0 or i > 19
        },
    }
class ExcelReader:

    def __init__(self, user_input_path):
        self.user_input_path = user_input_path

    def read_write(self):
        book = load_workbook(self.user_input_path, data_only=True)
        for sheet_name in book.sheetnames:
            if sheet_name not in config:
                continue

            sheet = book[sheet_name]
            conf = config[sheet_name]

            skip_cols = conf["skip_cols"]
            index_row = conf["index_col"]
            header_row = conf["header_row"]

            msg_col = user_id_col + 1
            send_tag_col = user_id_col + 2
            h1  = sheet[header_row]
            h2 = sheet[header_row + 1]
            for row in sheet.iter_rows(min_row=header_row + 2, max_col=send_tag_col):
                if not str(row[index_row].value).isdigit():
                    break

                if len(row) > send_tag_col and row[send_tag_col] == "已发送":
                    continue

                if row[msg_col].value is None:
                    sheet[f'AN{row[0].row}'] = self.msg_concat(h1, h2, row, skip_cols)

        book.save(self.user_input_path)



    def msg_concat(self, header1, header2, cells, skip_cols):
        data = {}
        h_1 = None
        for i, cell in enumerate(cells):

            if skip_cols(i):
                continue

            h1 = header1[i].value
            if not pandas.isna(h1) and h1 != h_1:
                h_1 = h1

            h_2 = header2[i].value
            value = cell.value
            if pandas.isna(h_2):
                h_2 = h_1

            if not pandas.isna(h_2) and not pandas.isna(value):
                if h_2 == "小计":
                    h_2 = h_1 + h_2

                data[h_2] = value
        return json.dumps(data, ensure_ascii=False).replace('"', "").replace('\n', "")


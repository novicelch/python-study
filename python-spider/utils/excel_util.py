# !/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "liuchenhu";
import openpyxl;

def create_excel(header, body, file_path):
    # 获取 workbook 对象
    workbook = openpyxl.Workbook();
    # 获取 sheet 对象
    active_sheet = workbook.active;
    # 数据操作
    active_sheet.append(header);
    for item in body:
        active_sheet.append(item);
    # 文件保存
    workbook.save(filename=file_path);

if __name__ == "__main__":
    pass;
# !/user/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "liuchenhu";

from utils import excel_util;
import random;

def write_excel():
    header = ["第一季度", "第二季度", "第三季度", "第四季度"]
    file_path = "C:/Users/liuchenhu/Desktop/文档/excel_test.xlsx";
    body = list();
    for item in range(1, 10):
        line = list();
        for i in range(1, len(header) + 1):
            line.append(i * random.randint(1, 10));
        body.append(line);
    excel_util.create_excel(header, body, file_path);

if __name__ == "__main__":
    write_excel();
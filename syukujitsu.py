#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import datetime
import csv
import io

CSV_PATH = 'https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv'

class SyukujitsuApi:
    def __init__(self):
        res = requests.get(CSV_PATH)
        data_str = res.content.decode('shift-jis')

        csv_file_obj = io.StringIO()
        csv_file_obj.write(data_str)
        csv_file_obj.seek(0)
        csv_reader = csv.reader(csv_file_obj)
        self.data_list = [row for row in csv_reader]
        csv_file_obj.close()

    def is_syukujitsu_today(self):
        today = datetime.date.today()
        return self.is_syukujitsu(date=today)

    def is_syukujitsu(self, date=None):
        date_str = date.strftime('%Y/%-m/%-d')        
        return len([x for x in self.data_list if x[0] == date_str]) > 0


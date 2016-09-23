import datetime

import xlrd
import xlwt
import os
from xlutils.copy import copy


class ExcelOps(object):
    def generateParamFiles(self):
        if os.path.exists('参数表.xls'):
            workbook = xlrd.open_workbook('参数表.xls')
            table = workbook.sheets()[0]
            self.totalColumns = table.ncols
            self.totalRows = table.nrows
        else:
            self.workbook = xlwt.Workbook()
            self.sheet = self.workbook.add_sheet('参数表', cell_overwrite_ok=True)
            self.initParamTable(self.sheet)
            self.workbook.save('参数表.xls')
        print("init param successfully")

    # 初始化参数表
    def initParamTable(self, sheet):
        # 初始化参数表中的煤种类
        column = 1
        file = open('煤种列表.txt', 'r')
        for line in file:
            sheet.write(0, column, line)
            column += 1
        self.totalColumns = column
        file.close()
        # 初始化参数表的时间列,先写死后续优化
        dates = self.dateRange("2016-01-01", "2016-12-31")
        self.writeDateIntoTable(dates, sheet)

    def dateRange(self, beginDate, endDate):
        dates = []
        dt = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
        date = beginDate[:]
        while date <= endDate:
            dates.append(date)
            dt = dt + datetime.timedelta(1)
            date = dt.strftime("%Y-%m-%d")
        return dates

    def writeDateIntoTable(self, dates, sheet):
        print('the length of dates is : ' + str(len(dates)))
        row = 1
        for date in dates:
            sheet.write(row, 0, date)
            row += 1
        self.totalRows = row

    # 在表格里更新煤种的价格
    def updateParamTable(self, itemSelected, priceInput, beginDate, endDate):
        startDateIndex = self.findIndexOfDate(beginDate)
        endDateIndex = self.findIndexOfDate(endDate)
        # if string.(startDateIndex, endDateIndex) > 0:
        #     return
        kindIndex = self.findIndexOfKind(itemSelected)
        oldBook = xlrd.open_workbook('参数表.xls')
        newBook = copy(oldBook)
        for index in range(startDateIndex, endDateIndex + 1):
            newBook.get_sheet(0).write(index, kindIndex, priceInput)
        newBook.save('参数表.xls')

    def findIndexOfDate(self, date):
        sheet = xlrd.open_workbook('参数表.xls').sheets()[0]
        for row in range(self.totalRows):
            cell_value = sheet.cell_value(row, 0)
            if cell_value == str(date):
                return row

    def findIndexOfKind(self, itemSelected):
        sheet = xlrd.open_workbook('参数表.xls').sheets()[0]
        for column in range(1, self.totalColumns):
            cell_value = sheet.cell_value(0, column)
            if cell_value == str(itemSelected + '\n'):
                return column

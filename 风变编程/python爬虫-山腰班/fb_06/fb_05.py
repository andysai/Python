import openpyxl
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='new title'
sheet['A1'] = '歌曲名'
sheet['B1'] = '专辑名'
sheet['C1'] = '播放时长'
sheet['D1'] = '播放链接'
rows = [['借口', '七里香', '260', 'https://y.qq.com/n/yqq/song/002XWgfo0IKPOH.html'],['夜的第七章', '依然范特西', '228', 'https://y.qq.com/n/yqq/song/0010ibBn4bYFTk.html']]
for i in rows:
    sheet.append(i)
print(rows)
wb.save('test_1.xlsx')
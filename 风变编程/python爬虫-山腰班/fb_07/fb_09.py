import requests,csv

# 获取题库的URL
URL = 'https://www.shanbay.com/api/v1/vocabtest/category/'
get_res = requests.get(URL)
json_res = get_res.json()
data_res = json_res['data']
# 用户输入需要测试的词库
chooise = int(input('请输入想测的词库，输入数字编号，获取题库的代码:'
                    '(1.GMAT、2.考研、3.高考、4.四级、5.六级、6.英专、7.托福、8.GRE、9.雅思、10.任意),按Enter确认:'))
# 获取对应的题库
number = data_res[chooise-1][0]

# 获取对应等级测试的题库URL
url = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='
# 下载50个单词
test = requests.get(url + number)
#对test进行解析。
words = test.json()
#新增一个list，用于统计用户认识的单词
danci = []
#创建一个空的列表，用于记录用户认识的单词
words_knows = []
#创建一个空的列表，用于记录用户不认识的单词
not_knows = []
# 判断是否认识单词
print ('测试现在开始。如果你认识这个单词，请输入Y，否则直接敲Enter：')
n = 0
for i in words['data']:
    n = n+1
    konw_words = i['content']
    print('\n第{}个单词:{}'.format(n,konw_words))
    answer = input('如果认识请按Y，否侧按enter:')
    if answer == 'Y':
        danci.append(konw_words)
        words_knows.append(konw_words)
    else:
        danci.append(konw_words)
        not_knows.append(konw_words)

print('一共测试了{}个单词，你认识的单词有{}个，不认识的单词有{}个。'.format(len(danci),len(words_knows),len(not_knows)))
# 打印错题集
with open('cuoti.txt','test_1',encoding='utf-8') as f:
    for i in not_knows:
        if i == None:
            print('你没有不认识的单词')
        else:
            print('你不认识的单词有:' + i)
        f.write(i + '\r\n')

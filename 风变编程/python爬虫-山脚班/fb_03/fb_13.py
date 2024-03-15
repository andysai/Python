from urllib.request import quote
c = '猫砂'
a = '%E7%8C%AB%E7%A0%82'
b = c.encode('gbk')
print(quote(b))
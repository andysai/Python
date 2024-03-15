list = (
'xfu@casc.ac.cn',
'hym@casc.ac.cn',
'ljm@casc.ac.cn',
'lss@casc.ac.cn',
'pwj@casc.ac.cn',
'lxg@casc.ac.cn',
'lhb@casc.ac.cn',
'lhh@casc.ac.cn',
'chenfan@casc.ac.cn',
'xyk@casc.ac.cn',
'czl@casc.ac.cn',
'cll@casc.ac.cn',
'yrx@casc.ac.cn',
'ljg@casc.ac.cn',
'ck@casc.ac.cn',
'lzz@casc.ac.cn',
'lcg@casc.ac.cn',
'lhr@casc.ac.cn',
'lcl@casc.ac.cn',
'zwl@casc.ac.cn',
'cxb@casc.ac.cn',
'lyh@casc.ac.cn',
'fy@casc.ac.cn',
'zls@casc.ac.cn',
'lsz@casc.ac.cn',
'ly@casc.ac.cn',
'qwg@casc.ac.cn',
'hya@casc.ac.cn',
'qzj@casc.ac.cn'
)


for i in list:
    if '@' == i[3:4]:
        print(i[:3])
    elif '@' == i[2:3]:
        print(i[:2])
    elif '@' == i[7:8]:
        print(i[:7])
    else:
        print('@不在第三位')
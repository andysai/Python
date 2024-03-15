
url_lists = []
for i in range(1,11):
    if i == 1:
        url = 'http://www.mtime.com/top/tv/top100/'
        url_lists.append(url)
    else:
        url = 'http://www.mtime.com/top/tv/top100/index-' + str(i) + '.html'
        url_lists.append(url)

print(url_lists)
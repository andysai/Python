from pyecharts.charts import WordCloud
import pyecharts.options as opts

words = [
    ('Sam S Club', 10000),
    ('Macys', 6000),
    ('Amy Schumer', 4300),
    ('Beautifully', 5000),
    ('Congratulations', 6500),
    ('Jurassic', 4500),
    ('Love', 5500),
    ('Honorable', 3900),
    ('King', 4800),
]
wordcloud = WordCloud()
wordcloud.add('词云图', words, word_size_range=[20, 100])
wordcloud.set_global_opts(title_opts=opts.TitleOpts(title='WordCloud-词云图'))
wordcloud.render('../source_material/01/20-词云图.html')
print('生成成功')

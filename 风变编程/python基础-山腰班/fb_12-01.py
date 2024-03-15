class Chinese:
    def __init__(self, name, birth, region,hometown):
        self.name = name
        self.birth = birth
        self.region = region
        self.hometown = hometown

    def born(self):
        print('我出生在%s。' % self.hometown)


wufeng = Chinese('sai','广东','ss','dg')
wufeng.born()
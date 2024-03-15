class China:
    # 属性:眼睛是黑色的
	black_eyes=True
    # 方法:打印出'吃饭，选择用筷子。'
	def start(self):
		return '吃饭，选择用筷子。'

t = China()
print(t.black_eyes)
print(t.start())
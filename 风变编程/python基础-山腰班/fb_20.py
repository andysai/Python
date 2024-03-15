class Book:
    def __init__(self, book_name, author, recommended_language, state=0):
        # 对实例属性进行初始化
        # 分别表示书名、作者、推荐语和借阅状态
        self.book_name = book_name
        self.author = author
        self.recommended_language = recommended_language
        self.state = state

    def __str__(self):
        # 为了后续方便参数传递，借阅状态state采用默认参数，用0来表示'未借出'，1来表示'已借出'
        if self.state == 0 :
            status = '未借出'
        else :
            status = '已借出'
        # 返回书籍信息
        return '名称:《%s》 作者:%s 推荐语: %s 状态:%s' % (self.book_name,self.author,self.recommended_language,status)

class BookManager:
    # 创建一个列表，列表里每个元素都是Book类的一个实例
    books = []

    def __init__(self):
        # 创建三个实例对象
        book1 = Book('惶然录', '费尔南多·佩索阿', '一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = Book('以箭为翅', '简媜', '调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book('心是孤独的猎手', '卡森·麦卡勒斯', '我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。', 1)

        # 创建三个实例对象
        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)

    def menu(self):
        # 显示选择菜单，根据不同的选择调用不同的方法
        print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地。\n')
        while True:
            print('1.查询所有书籍\n2.添加书籍\n3.借阅书籍\n4.归还书籍\n5.退出系统\n')
            choice = int(input('请输入数字选择对应的功能:'))
            # 1.查询所有书籍
            if choice == 1:
                # 调用方法show_all_book()
                self.show_all_book()

            # 2.添加书籍
            elif choice == 2:
                # 调用方法add_book()
                self.add_book()

            # 3.借阅书籍
            elif choice == 3:
                # 调用方法lend_book()
                self.lend_book()

            # 4.归还书籍
            elif choice == 4:
                # 调用方法return_book()
                self.return_book()

            # 5.退出系统
            elif choice == 5:
                print('感谢使用！愿你我成为爱书之人，在茫茫书海里相遇。')
                break

    def show_all_book(self):
        # 显示每本书籍的信息
        print('书籍信息如下：')
        for book in self.books:
            print(book)
            print('')

    def add_book(self):
        # 添加书籍
        # 获取书籍相应信息，赋值给属性
        new_name = input('请输入书籍名称：')
        new_author = input('请输入书籍作者：')
        new_recommended_language = input('请输入书籍推荐语：')

        # 传入参数，创建Book类实例new_book
        new_book = Book(new_name,new_author,new_recommended_language)

        # 将new_book添加到books里
        self.books.append(new_book)

        print('书籍录入成功！\n')

    def check_book(self, name):
        for book in self.books:
            if book.book_name == name:
                return book
        else:
            return None

    def lend_book(self):
        name = input('请输入书籍的名称：')
        res = self.check_book(name)

        if res != None:
            if res.state == 1:
                print('你来晚了一步，这本书已经被借走了噢')
            else:
                print('借阅成功，借了不看会变胖噢～')
                res.state = 1
        else:
            print('这本书暂时没有收录在系统里呢')

    def return_book(self):
        # 归还书籍
        name = input('请输入归还书籍的名称：')
        # 调用check_book方法，将返回值赋值给变量res
        res = self.check_book(name)
        # 如果返回的是空值，即这本书的书名不在系统里
        if res == None:
            # 如果返回的是实例对象
            print('没有这本书噢，你恐怕输错了书名～')
        else:
            # 如果实例属性state等于0，即这本书的借阅状态为'未借出'
            if res.state == 0:
                print('这本书没有被借走，在等待有缘人的垂青呢！')
            # 如果实例属性state等于1，即状态为'已借出'
            else:
                print('归还成功！')
                # 归还后书籍借阅状态为0，重置为'未借出'
                res.state = 0

manager = BookManager()
manager.menu()
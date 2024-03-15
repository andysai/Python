# 9-4 就餐人数：在为9-1编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0。
# 根据这个类创建一个名为restaurant的实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
# 添加一个名为set_number_served()的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为increment_served()的方法，它让你能够将就餐人数递增。
# 调用这个方法并向它传递一这样的值：你认为这家餐馆每天可能接待的就餐人数。

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        return '\n餐馆的名字为:' + self.restaurant_name + '\n菜肴有:' + self.cuisine_type

    def open_restaurant(self):
        return '餐馆正在营业'

    def read_number_served(self):
        """在餐馆就餐过的人数"""
        return "Our served " + str(self.number_served) + " people.\n"

    def set_number_served(self,number):
        self.number_served = number
        return restaurant.read_number_served()

    def increment_served(self, increment_number):
        self.number_served = self.number_served + increment_number
        return '递增之后的用餐人数为:' + str(self.number_served) + '人'

restaurant = Restaurant('Chinese','noodle')
print(restaurant.read_number_served())
restaurant = Restaurant('Chinese','noodle',200)
print(restaurant.read_number_served())
print(restaurant.set_number_served(200))
print(restaurant.increment_served(200))
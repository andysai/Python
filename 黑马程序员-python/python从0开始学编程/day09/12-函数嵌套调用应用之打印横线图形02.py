def print_line():
    print('-' * 20)

# def print_lines(num):
#     i = 0
#     while i < num:
#         print_line()
#         i += 1
#
# print_lines(3)

def print_lines(num):
    for i in range(num):
        print_line()

print_lines(3)

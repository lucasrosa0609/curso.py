# https://docs.python.org/3/library/exceptions.html

def divide(n1, n2):
    if n2 == 0:
        raise ValueError("n2 nao pode ser 0")
#     try:
#         return n1/n2
#     except ZeroDivisionError as error:
#         print('Log:', error)
#         raise
#
# try:
#     print(divide(2, 0))
# except ZeroDivisionError as error:
#     print(error)
#
    return n1 / n2

try:
    print(divide(2, 1))
    print(divide(2, 0))  # vai dar erro
except ValueError as error:
    print(error)



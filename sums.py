# 練習二加總

# 接收任意參數 加總
def my_sum(*numbers):
    out = 0
    print(numbers)
    print(type(numbers))
    for i in numbers:
        out += i
    return out    


print(my_sum(7, 99, 12, 33, 5))
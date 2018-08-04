formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))#调用format函数，然后给formatter赋值
print(formatter.format(formatter, formatter, formatter, formatter))#format自己传给自己
print(formatter.format(
    "try your",
    "own text here",
    "maybe a poem",
    "or a song about fear"
))#传字符串

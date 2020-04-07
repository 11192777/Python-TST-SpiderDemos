# coding-utf-8

str = "你好{}啊，哈哈哈哈"

print(str.format("年后"))
print(str.format(123))
print(str.format([1, 2, 3, "222"]))
print(str.format({"name": "孟庆宇", "age": 12}))

str = "你好{}啊，哈{}哈哈哈"
print(str.format("123", 222, {"angin": 12}))

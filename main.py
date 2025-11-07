# 接收字符串
text = input("请输入字符串：")
# 统计字符频率的字典
char_freq = {}
for char in text:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
# 按字符出现频率降序排序
sorted_chars = sorted(char_freq.items(), key=lambda item: item[1], reverse=True)
# 打印结果
for char, freq in sorted_chars:
    print(f"字符 '{char}' 出现的频率：{freq}")频率的差别")

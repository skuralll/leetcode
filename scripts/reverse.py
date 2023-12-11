s = input()

# シンプル
sl = list(s)
s_rev = ""
for i in range(len(sl) - 1, -1, -1):
    s_rev += sl[i]
print(s_rev)

# モジュール使用
s_rev = "".join(reversed(s))
print(s_rev)

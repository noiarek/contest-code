_ = input()
a = map(int, raw_input().split())
a.sort()
first = 0
second = 1
added ={}

first = a.pop()
a = a[2:]

while a:

    if a[-1] * a[0] != first or a[-1] in added:
        second = a[-1]
        break
    del a[0]

    if a:
        del a[-1]

print first, second
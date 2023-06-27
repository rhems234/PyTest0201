total = int(input())
count = int(input())

result = 0

for i in range(1, count + 1):
    x, y = map(int, input().split())
    result += x * y

if total == result:
    print("Yes")
else:
    print("No")

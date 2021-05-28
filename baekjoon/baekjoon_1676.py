sum = 1
for i in range(1, int(input()) + 1):
    sum *= i
cnt = 0
while not sum % 10:
    cnt += 1
    sum //= 10
print(cnt)

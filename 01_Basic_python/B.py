
test_case = int(input())

n, m = map(int, input().split())

mattrix = []
for i in range(n):
    arr = list(map(int, input().split()))
    mattrix.append(arr)


print(test_case)
print(n, m)
# print(mattrix)
for i in range(n):
    for j in range(m):
        print(mattrix[i][j], end=" ")
    print()
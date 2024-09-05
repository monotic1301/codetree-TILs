n = int(input())
stores = list(map(int,input().split(' ')))
boss, employee = map(int,input().split(' '))

answer = 0
for store in stores:
    if (store-boss)%employee ==0:
        answer += (store-boss)//employee + 1
    else:
        answer += (store-boss)//employee + 2

print(answer)
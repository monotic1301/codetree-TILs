n = int(input())
stores = list(map(int,input().strip().split(' ')))
boss, employee = map(int,input().strip().split(' '))

answer = 0
for store in stores:
    if store - boss <= 0:
        answer += 1
    else:
        if (store-boss)%employee ==0:
            answer += (store-boss)//employee + 1
        else:
            answer += (store-boss)//employee + 2

print(answer)
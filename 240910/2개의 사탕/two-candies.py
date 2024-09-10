from collections import deque

N, M = map(int, input().strip().split())

box = []

red = [0, 0, "R", False]
blue = [0, 0, "B", False]
for i in range(N):
    line = input().strip()
    r = line.find('R')
    b = line.find('B')
    if r != -1:
        red = [i, r, "R", False]
    if b != -1:
        blue = [i, b, "B", False]
    box.append(list(line))


def moving(box, candy, d):  # 박스, 사탕 위치, 방향
    # 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    while True:
        new_y = candy[0] + dy[d]
        new_x = candy[1] + dx[d]
        if box[new_y][new_x] == ".":  # .일경우만 움직이기
            box[candy[0]][candy[1]] = "."
            candy = [new_y, new_x, candy[2], candy[3]]
            box[new_y][new_x] = candy[2]
        elif box[new_y][new_x] == "O":  # O를 만난 경우 탈출
            candy = [-1, -1, candy[2], True]
            candy[3] = True
        else:  # 캔디나 벽을 만난 경우는 멈춤
            break

    return box, candy


queue = deque([[box, red, blue, 0]])
answer = -1
while queue:
    box, red, blue, count = queue.popleft()
    if answer != -1 or count == 11:
        break
    for d in range(4):  # 4방향에 대해서 시도
        new_box, new_red = moving(box, red, d)
        new_box, new_blue = moving(new_box, blue, d)
        if new_red[3] == False:
            if new_blue[3] == False:
                new_box, new_red = moving(new_box, new_red, d)

        if new_red[3] == True and new_blue[3] == False:
            answer = count
        elif new_red[3] == False and new_blue[3] == False:
            if red != new_red or new_blue != blue:
                queue.append([new_box, new_red, new_blue, count + 1])
print(answer)
import random

# 1.增加勝負判斷
# 2.贏的時候提示猜幾次
# 3.提示區間

x = random.randint(1, 50)
win = False
min = 1
max = 50

for i in range(5):
    y = eval(input(f'[{i + 1}/5]請猜一個數字({min}~{max}之間):'))
    if x == y:
        win = True
        break
    elif i == 4:
        break

    if x > y:
        if y > min:
            min = y
        print('猜大一點')
    else:
        if max > y:
            max = y
        print('猜小一點')

if win:
    print(f'恭喜過關!共猜了{i + 1}次')
else:
    print(f'遊戲結束!答案為:{x}')

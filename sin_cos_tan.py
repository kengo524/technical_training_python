import math

min = 0
max = 360
interval = 15

for b in range(min, max, interval): #上記で作成した配列から取り出す。
    s = round(math.sin(math.radians(b)), 4)#取り出した数値をsin()に代入し、計算させる。その際、度→ラジアンに変更。以下同様。
    c = round(math.cos(math.radians(b)), 4)
    t = round(math.tan(math.radians(b)), 4)
    print(f'sin{b}°:{s}') #print(f'{s} is {i} years old')の形で文字列と変数を両立して表示する。
    print(f'cos{b}°:{c}')
    print(f'tan{b}°:{t}')

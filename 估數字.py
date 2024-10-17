import random
ans = random.randint(1,100)
i=0
for i in range(1,11):
    pa= input(f"答案係咩？(剩餘次數：{11-i}/10): ")
    try:
        pa = int(pa)
        if pa < ans:
            print("大啲")
        elif pa > ans:
            print("細啲")
        elif pa == ans:
            print("恭喜")
            break

    except:
        print("整數啊屌你")
else:
    print("輸咗")
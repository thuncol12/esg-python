
# 구구단
# 2-9단
def gugudan():
    for i in range(2, 10):
        for j in range(1, 10):
            print(f'{j}*{i}={i*j}', end=' ')
        print()


gugudan()


# 커피자판기
print('아메리카노: 2500원\n라떼: 3000원')
menu = {
    '아메리카노': 2500,
    '라떼': 3000
}
money, coffee = input("돈 커피명: ").split()
money = int(money)
if money == menu[coffee]:
    print(f'{coffee} 나왔습니다. ')
elif money > menu[coffee]:
    print(f'{coffee} 나왔습니다. 거스름돈은 {money-menu[coffee]}원입니다.')

# BMI
weight, height = map(int, input("체중과 키를 입력하세요. ").split())
while True:
    BMI = weight/((height/100)**2)
    print("BMI: ", BMI)
    if BMI < 18.5:
        print("저체중입니다. ")
    elif 18.5 <= BMI <= 24.9:
        print("정상입니다. ")
    elif 25 <= BMI <= 29.9:
        print("과체중입니다. ")
    elif 30 <= BMI:
        print('비만입니다. ')
    break

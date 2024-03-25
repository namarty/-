try:
    x = float(input("입력값 1:"))
    y = float(input("입력값 2:"))
    a = float(input("입력값 3:"))
    z = pow(pow(x, y), 1/a)
    print("x의 y 제곱한 값에 1/a를 제곱한 결과값은", z, "이다.")
except ValueError:
    print("잘못된 입력입니다. 숫자를 입력하세요.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
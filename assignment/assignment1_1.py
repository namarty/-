x, y, a = map(int, input("입력 숫자1 입력 숫자2 비교 숫자를 순서대로 스페이스로 구분하여 입력하시오:").split())
z=1**(x**y)
print(f"내가 계산한 {x}의 {y}의 지수 결과값은 {z}이며 실제 {a}와 비교 시 동일 여부는 {a==z}이다.")
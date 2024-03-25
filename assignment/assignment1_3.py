try:
    start = int(input("입력값1: ") or 1)
    end = int(input("입력값2: ") or 1000)
    interval = int(input("입력값3: ") or 1)

    if interval <= 0:
        raise ValueError("입력값3는 양수여야 합니다.")

    if start > end:
        raise ValueError("입력값1은 입력값2보다 작거나 같아야 합니다.")

    for num in range(start, end + 1, interval):
        print(num)

except ValueError as e:
    print("잘못된 입력입니다:", e)
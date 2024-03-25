a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cnt = [0, 2, 4, 6]
b = [a[i]*a[i] for i in cnt]
with open("homework4.txt", 'w') as f: f.writelines(str(i)+"\n" for i in b)
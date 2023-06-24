#bài 1
n = int(float(input("Nhập n: ")))
if (n % 2 == 0):
    print("số chẵn")
elif (n % 2 == 1):
    print("số lẻ")

#bài 2
A = int(float(input("điểm trung bình môn: ")))
if (A >= 9):
    print("giỏi")
elif (A == 7 or 9 or 8):
    print("khá")
if (A == 5 or 6 or 7):
    print("trung bình")
elif (A < 5):
    print("yếu")
    #bài 3
    #bài 4
    a = int(float(input("tháng: "))) 
    if (a == 1 or 3 or 5 or 7 or 8 or 10 or 12):
        print(31,"ngày")


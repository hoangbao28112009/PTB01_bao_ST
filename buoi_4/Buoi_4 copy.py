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
elif (A == 7 or  8):
    print("khá")
if (A == 5 or 6 ):
    print("trung bình")
elif (A <= 4):
    print("yếu")
#bài 4
b = int(float(input("tháng: ")))
if (b == 1 or 3 or 5 or 7 or 8 or 10 or 12):
        print(31,"ngày")
elif (b == 4 or 6 or 9  or 11):
        print(30,"ngày")    
if (b == 2):
  c = int(float(input("năm: ")))
  (c % 4 or 400)
  print (29,"ngày")
  not (c % 4 or 400)
  print(28,"ngày")

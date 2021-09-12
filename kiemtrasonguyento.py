print(" nhap vào số N lớn hơn 1");

n= int(input())
flag  = True

#kiểm tra SNT
if( n<2):
    flag = False
elif(n == 2):
    flag = True
elif(n % 2 == 0):
    flag = False
else:
    for i in range(3, n, 2):
        if( n % i == 0):
            flag = False

# Tìm kết quả
if flag == True:
    print(n," là số nguyên tố")
else:
    print(n, "không phải là số nguyên tố")

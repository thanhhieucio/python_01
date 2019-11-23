import  pandas as pd


def giaithua(n):
    """Đây là hàm tính giai thừa của
       một số nguyên by Quantrimang.com"""
    if n == 1:
        return 1
    else:
        return (n * giaithua(n - 1))


# num = 5
# num1 = int(input("Nhập số cần tính giai thừa: "))
# print("Giai thừa của", num, "là", giaithua(num))
# print("Giai thừa của", num1, "là", giaithua(num1))

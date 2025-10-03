txt="salom dunyo"
#                   5
# for i in range(len(txt)):
#     print(txt[i], end=" ") # txt[i]

# for i in txt:
#     print(i, end=" ") # txt[i]

# print(txt[0])
# print(txt[1])
# print(txt[2])
# print(txt[3])
# print(txt[4])

# agar foydalanuvchi son kiritsa shu sonning uzunligini toping.
# son= abs(int(input("sonni kiriting: ")))
# count=0
# while son>=1:
#     son//=10
#     count+=1
# print(count)

# Kiritilgan textni palendrom ekanligini aniqlang
# txt=input("so'zni kiriting: ")

# reverse_txt=txt[::-1] 

# if txt == reverse_txt:
#     print("Palindrom")
# else:
#     print("palindrom emas")

# a=int(input("A sonni kiriting: "))
# b=int(input("B sonni kiriting: "))
# c=int(input("C sonni kiriting: "))
# if a>b:
#     if a>c:
#         print("A sonni katta")
# elif b>a:
#     if b>c:
#         print("B sonni katta")
# elif c>a:
#     if c>b:
#         print("C sonni katta")
# txt="Respublik"
# n=9

# print(txt[2:8:])

# for i in range(n):
#     for j in range(n):
#         # if i==j or j==n-i+n//2 or (i==n-1 and j==n-2) or (j==n-1 and i==n-2):
#         if i==n-1 or i==j or i==0 or j==n-i-1 :
#             print(txt[j], end=" ")
#         elif j==0:
#             print(txt[i], end=" ")
#         else:
#             print("  ", end="")
#     print()

print()

# n=13
# a=False
# for i in range(2, n//2):
#     if n%i:
#         a=True
#     else:
#         a=False

# if a:
#     print("Tub son")
# else:
#     print("Tub emas")
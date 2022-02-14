# print("Welcome, to the 'Health Management system' let's get started!!!\nlemme know if you wanna log or retrive\n")
#
# def getdate():
#     import datetime
#     return datetime.datetime.now()
#
# a = int(input("type 1 for log and 2 for retrive\n"))
#
# def log(k):
#     if k == 1:
#         kked = int(input("1 for diet and 2 for exe"))
#         if kked == 1:
#             kkd = input("enter diet")
#             with open("kiki.diet.txt", "a") as op:
#                 op.write(str([str(getdate())]) + ":" + kkd + "\n")
#                 op.close()
#
#         elif kked == 2:
#             kke = input("Enter exercise")
#             with open("kiki.exe.txt", "a") as op:
#                 op.write(str([str(getdate())]) + ":" + kke + "\n")
#                 op.close()
#
#     elif k == 2:
#         kbed = int(input("1 for diet and 2 for exe"))
#         if kbed == 1:
#             kbd = input("Enter diet")
#             with open("kb.diet.txt", "a") as op:
#                 op.write(str([str(getdate())]) + ":" + kbd + "\n")
#                 op.close()
#         elif kbed == 2:
#             kbe = input("Enter exercise")
#             with open("kb.exe.txt", "a") as op:
#                 op.write(str([str(getdate())]) + ":" + kbe + "\n")
#                 op.close()
#
#     elif k == 3:
#         haed = int(input("Enter 1 for diet and 2 for exercise"))
#         if haed == 1:
#             had = input("Enter diet")
#             with open("gaurav.diet.txt", "a") as p:
#                 p.write(str([str(getdate())])+ ":" + had + "\n")
#                 p.close()
#
#         elif haed == 2:
#             hae = input("Enter exercise")
#             with open("gaurav.exe.txt", "a") as p:
#                 p.write(str([str(getdate())]) + ":" + hae + "\n")
#                 p.close()
#
#     else:
#         print("Didn't get you. Enter either enter 1 or 2")
#
#
# def retrive(z):
#     if z == 1:
#         ed = int(input("Enter 1 for diet and 2 for exercise\n"))
#         if ed == 1:
#             with open("kiki.diet.txt") as op:
#                 for i in op:
#                     print(i)
#         elif ed == 2:
#             with open("kiki.exe.txt") as op:
#                 for i in op:
#                     print(i)
#
#     elif z == 2:
#         ed = int(input("Enter 1 for diet and 2 for exercise\n"))
#         if ed == 1:
#             with open("kb.diet.txt") as op:
#                 for i in op:
#                     print(i)
#         elif ed == 2:
#             with open("kb.exe.txt") as op:
#                 for i in op:
#                     print(i)
#
#     elif z == 3:
#         ed = int(input("Enter 1 for diet and 2 for exercise\n"))
#         if ed == 1:
#             with open("gaurav.diet.txt") as p:
#                 for i in p:
#                     print(i)
#         elif ed == 2:
#             with open("gaurav.exe.txt") as p:
#                 for i in p:
#                     print(i)
#
#     else:
#         print("Didn't get you. Either enter 1 or 2")
#
#
# if a == 1:
#     k = int(input("whose data do you wanna log\ntype 1 for kiki, 2 for kb and 3 for gaurav\n"))
#     log(k)
# else:
#     z = int(input("whose data do you wanna retrive\ntype 1 for kiki, 2 for kb and 3 for gaurav\n"))
#     retrive(z)







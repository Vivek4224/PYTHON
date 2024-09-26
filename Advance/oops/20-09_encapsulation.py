# class Auth:
#     class Register:
#         def __init__(self,username,email,pwd,cpwd):
#             self.u = username
#             self.e = email
#             self.p = pwd
#             self.cp = cpwd

#         def is_email_valid(self):
#             if '.' in self.e and "@" in self.e:
#                 return True
#             else:
#                 return False

#         def check_password(self):
#             if len(self.p) >= 8:
#                 if self.p == self.cp:
#                     return True
#                 else:
#                     return False
#             else:
#                 return False

#         def user_register(self):
#             if self.is_email_valid():
#                 if self.check_password():
#                     print("user register successfully.")
#                 else:
#                     print("invalid data")
#             else:
#                 print("invalid data")

# new_obj = Auth().Register("vivek08",".@","teat1234","teat1234")
# print(new_obj.e)
# print(new_obj.p)
# while(1):
#     username = input("Enter a userName: ")
#     email = input("Enter a email: ")
#     password = input("Enter a password: ")
#     comfirm_password = input("Enter a confirm password: ")
#     obj = Auth().Register(username,email,password,comfirm_password)
#     obj.user_register()

class ATM:
    def __init__(self,pin):
        self.p = pin

    def setPin(self,atm_pin):
        self.sp = atm_pin

    def getPIN(self):
        print(self.p)

obj = ATM("2222")
obj.setPin("1111")
obj.getPIN()







        
            

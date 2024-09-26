"""
syntax class and object:

 class classname:
    # block of code

 obj_name = classname()

"""

# num1 = 10
# num2 = 20 

# def add():
#     res = num1 + num2
#     print(res)

# print(num1)
# print(num2)
# add()



# class math:
#     num1 = 10
#     num2 = 20

#     def add(self):
#         res = self.num1 + self.num2
#         print(res)

# obj = math()
# print(obj.num1)
# print(obj.num2)
# obj.add()

class Auth:
    class Register:
        def user_register(self):
            print("Regester successfully.")
        
obj = Auth().Register()
obj.user_register()





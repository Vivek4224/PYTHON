# compile-time - static binding
# method overloading

# class math1:
#     def add(self,a,b):
#         return a + b
    
#     def add(self,a,b,c):
#         return a + b + c

# obj = math1()
# print(obj.add(10,20,30))

# class math1:
#     def add(self,a = None,b = None,c = None):
#         if a != None and b != None and c != None:
#             return a + b + c
#         if a != None and b != None:
#             return a + b

# obj = math1()
# print(obj.add(10,20))
# print(obj.add(10,20,30))

# run-time - dynamic binding
# method overriding

class math1:
    def info(self):
        return "this is a math1 method"

class math2(math1):
    def info(self):
        print(super().info())
        return "this is a math2 method"

obj = math2()
obj.info()
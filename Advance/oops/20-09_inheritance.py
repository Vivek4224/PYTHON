# class A:
#     def a(self):
#         print("This is class A")

# class B:
#     def b(self):
#         print("This is class B")

# obj = A()
# obj.a()

# obj = B()
# obj.b()

# class A:
#     def a(self):
#         print("This is a class A")

# class B(A):
#     def b(self):
#         print("This is a class B")

# class C(B):
#     def c(self):
#         print("This is a class C")

# obj = C()
# # print(dir(C))
# obj.a()
# obj.b()
# obj.c()



# class A:
#     def a(self):
#         print("This is a class A")

# class B:
#     def b(self):
#         print("This is a class B")

# class C(A,B):
#     def c(self):
#         print("This is a class C")

# obj = C()
# obj.a()
# obj.b()
# obj.c()

class Shape:
    def shape(self):
        print("Form Shape class")

class Shape2D(Shape):
    def shape2D(self):
        print("this is Shape2D")
    
class Circle(Shape2D):
    def circle(self):
        print("this is circle")

class Square(Circle):
    def square(self):
        print("this is square")
        
class Shape3D(Shape):
    def shape3D(self):
        print("this is SHape 3D")

obj = Square()
obj.square()
obj.shape2D()
obj.shape()

# print(Square.mro())
print(Square.__mro__)
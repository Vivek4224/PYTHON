# from Instagram.auth.register import register,otp
from Instagram.auth.register import *
from Instagram.auth import login
from Instagram.auth import forgot_password
from Instagram.post import create_post as cp
from Instagram.post import like
from Instagram.post import comment

# print( register())
# print(otp())
print(register())
print(otp())
print(login.login())
print(forgot_password.password())
print(cp.post())
print(like.like())
print(comment.comment())


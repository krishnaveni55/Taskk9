#1.The expected output for the given python code.
data=[10,501,22,37,100,999,87,351]
result=filter(lambda x:x>4,data)
print(list(result))

#2.python code using lambda fuction to check every element of list is aan integer or string
from functools import reduce
test_list = [[6,3,5],["Kpk", 3, "is"],[9, "good", 4]]
print("The original list : " + str(test_list))
res = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, str)], test_list, [])
print("The string instances : " + str(res))
res1 = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, int)], test_list, [])
print("The string instances : " + str(res1))

#3.python lambda function to create fibbonacci series from 1 to 50
def fibonacci(count): 
   fibo_list = [0, 1]
   any(map(lambda _: fibo_list.append(sum(fibo_list[-2:])),range(2, count)))
   return fibo_list[:count]
print(fibonacci(50))

#4.python function to validate the regular expression for following:
#a.email address
import re
def validate_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+",email):
        return True
    return False
email="krishnaveni5556@gmail.com"
if validate_email(email):
    print("validate email address")
else:
    print("invalid email address")

#b.mobile number of bangladesh
import re
def validate_bangladeshpno(number):
  pattern =r'^(\+880)+([\s.-]?1[0-9]{3})+([\s.-]?[0-9]{6})$'
  if re.fullmatch(pattern,number):
    return True
  else:
    return False
bangladeshno1="+880.9876.543123"
print("valid bangladesh number:",validate_bangladeshpno(bangladeshno1))
bangladeshno2="213354765867"
print("valid bangladesh number:",validate_bangladeshpno(bangladeshno2))
bangladeshno3="+8801234568762"
print("valid bangladesh number:",validate_bangladeshpno(bangladeshno3))

#c.Telephone number of usa
import  re
def validate_usaphnumber(number):
    pattern=r'^(\+1)+([\s.-]?[0-9]{3})+([\s.-]?[0-9]{3})+([\s.-]?[0-9]{4})$'
    if re.match(pattern,number):
        return True
    else:
        return False
usanumber1="+1-567-765-0987"
print("valid usa number:",validate_usaphnumber(usanumber1))
usanumber2="+15567798934"
print("valid usa number:",validate_usaphnumber(usanumber2))
usanumber3="5678 8907 876590"
print("valid usa number:",validate_usaphnumber(usanumber3))

#d.16 character of alpha numeric password composed of alphabets of uppercase,lowercase,special characters and numbers.
import re 
def validate_password(password):
    pattern=r'^\b[A-Za-z0-9@$!%*#?&]{16}$'
    match=re.fullmatch(pattern,password)
    if match:
        return("yes")
    else:
        return("no")
password1="Huihga$%7LKe#iyf"
print("valid password",validate_password(password1))
password2="KRISG123kBJUHMMH"
print("valid password",validate_password(password2))
password3="Ok^%$#@$%*gkfjlk"
print("valid password",validate_password(password3))

### eval函数
#### 用来获取字符串中的数据结构
person= "{'name':'lee'}"
a = eval(person)
print(a['name'])

#### 进行数学运算
expression = "1*2/3/8*79"

print(eval(expression))


### bin hex oct 内减函数
print(bin(10)) #10进制转2进制
print(hex(10)) #10进制转2进制
print(oct(10)) #10进制转8进制


### locals 输出局部变量，global输出全局变量
print(locals())
print(globals())
print(__file__)


age_dic = {'Lee': 32, 'Marlon': 30, 'Frank': 26}

print(max(age_dic.values()))


### zip函数
print(max(zip(age_dic.values(), age_dic.keys())))



### max取字典中的某一个Key中最大的数
people = [{'name':'Lee','age':32},
          {'name':'Marlon','age':30},
          {'name':'Frank','age':28}
         ]

print(max(people,key=lambda x:x['age']))


### pow
print(pow(3, 3, 2))


# slice切片
a = 'hello'
s1 = slice(2, 4)
print(a[s1])

### sorted

people = [{'name': 'Lee', 'age': 32},
          {'name': 'Marlon', 'age': 30},
          {'name': 'Frank', 'age': 28}]

print(sorted(people, key=lambda x:x['age']))

age_dic = {'Lee': 32, 'Marlon': 30, 'Frank': 26}

print(sorted(age_dic, key=lambda x:age_dic[x]))

print(sorted(zip(age_dic.values(), age_dic.keys())))


####  __import__ 函数用来当模块的名字通过字符串传过来的时候，导入相应的额模块

module_name = 'test'
test = __import__(module_name)
test.say_hello()
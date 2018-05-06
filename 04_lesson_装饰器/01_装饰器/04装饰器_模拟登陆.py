user_dic = {'username': None, 'login': False}

def auth(auth_type):
    def login(func):
        def wrapper(*args, **kwargs):
            if user_dic['username'] and user_dic['login']:
                res = func(*args, **kwargs)
                return res
            if auth_type == 'filedb':
                username = input('用户名: ').strip()
                passwd = input('密码: ').strip()
                f =  open('filedb', 'r')
                user_info = {"username":username, "passwd": passwd}
                for user in f:
                    if eval(user) == user_info:
                        res = func(*args, **kwargs)
                        user_dic['username'] = 'username'
                        user_dic['login'] = True
                        return res
                else:
                    print("用户名或者密码错误")
            else:
                print("不支持这种认证方式")
                return "不支持这种认证方式"
        return wrapper
    return login


@auth(auth_type='filedb')  # 相当于 login = auth(login) ---> index = login(index)
def index():
    print("欢迎来到商城")
    pass


@auth(auth_type='filedb')  # 相当于 login = auth(login) ---> index = login(index)
def home():
    print('home page')
    pass


@auth(auth_type='filedb')  # 相当于 login = auth(login) ---> index = login(index)
def shoping_car():
    print('shopping car')
    pass

index()
home()
shoping_car()
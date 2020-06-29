import requests


class UserInputError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo
    def __str__(self):
        return self.errorinfo

userInput = 'a';

try:
    if (not userInput.isdigit()):
        raise UserInputError('用户输入错误')
except UserInputError as ue:
    print(ue)
finally:
    pass




# # 传统的打开文件写法
# file1 = open('a.txt', encoding='utf8')
# try:
#     data = file1.read()
# finally:
#     file1.close()

# # with
# with open('a.txt', encoding='utf8') as file1:
#     data = file1.read()


class Open:
    def __enter__(self):
        print('enter')

    def __exit__(self, type, value, trace):
        print('eixt')

    def __call__(self, a):
        print('call')
        print(a)
        pass

with Open() as f:
    f('a')
    pass

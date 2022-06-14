# -*- coding: utf-8 -*- 
import os

class AUTOPip:
    def __init__(self):
        '''
        阿里云镜像：http://mirrors.aliyun.com/pypi/simple/
        清华大学镜像：https://pypi.tuna.tsinghua.edu.cn/simple/
        豆瓣镜像：http://pypi.doubanio.com/simple/
        中科大镜像：https://pypi.mirrors.ustc.edu.cn/simple
        华中科大镜像:http://pypi.hustunique.com/
        百度镜像:https://mirror.baidu.com/pypi/simple
        '''
        alimirror = 'http://mirrors.aliyun.com/pypi/simple/'
        tumirror = 'https://pypi.tuna.tsinghua.edu.cn/simple/'
        dbmirror = 'http://pypi.doubanio.com/simple/'
        usmirror = 'https://pypi.mirrors.ustc.edu.cn/simple'
        humirror = 'http://pypi.hustunique.com/'
        bdmirror = 'https://mirror.baidu.com/pypi/simple'
        pass
    
    # pip by pipreqs
    def apip0(self):
        syscode = os.system('pipreqs ./ --encoding=utf-8 --force --mode=no-pin')
        if syscode == 0:
            print('get requirements txt file success.')
            syscode = os.system('pip install -r ./requirements.txt')
            if syscode == 0:
                print('pip install success.')
            else:
                print('get return os code: {}, some is pip fail.'.format(syscode))
        else:
            print('get return os code: {}, pipreqs fail.'.format(syscode))
        print('syscode:', syscode)
    
    # pip install by reqs txt 
    def apip1(self, reqpath = './requirements.txt'):
        if os.path.exists(reqpath):
            os.system('pip install -r {}'.format(reqpath))
        else:
            reqpath = './requirements.txt'
            os.system('pip install -r {}'.format(reqpath))
        pass
    
if __name__ == "__main__":
    print("To test your plugin first, run the Python file directly from the command line")
    ap = AUTOPip()
    ap.apip0()
    # ap.apip1()
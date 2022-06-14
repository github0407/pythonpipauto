# -*- coding: utf-8 -*-

# 安装步骤
# 注意打包前修改相关配置，打包完就不方便做修改了
# 1. 运行python3 setup.py sdist
# 2. 在dist文件夹，在文件夹里面就有一个创建好的安装包，格式为***.tar.gz的压缩包,
# 运行 pip3 install --target=指定目录(不指定此参数，将默认安装到python系统下：
# /python目录/Lib/site-packages) dist/***.tar.gz

import setuptools

setuptools.setup(
    name='autopipreqs',  # 包的名字
    author='hankesen',  # 作者
    version='1.0.0',  # 版本号
    license='MIT',

    description='auto install pypi of project required.',
    long_description='''depends on pip method : requirements -> pipreqs -> setuptools -> some autoinstall''',
    author_email='hankesen@yxqiche.com',  # 你的邮箱**
    url='http://gitlab.yxqiche.com/algoplat/pycommon.git',  # 可以写github上的地址，或者其他地址
    # 包内需要引用的文件夹

    packages=setuptools.find_packages(),
    # 依赖包
    install_requires=[
        "lxml >= 3.7.1",
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',  # 支持的语言
        'Programming Language :: Python :: 3',  # python版本 。。。
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries'
    ],
    zip_safe=True,
)

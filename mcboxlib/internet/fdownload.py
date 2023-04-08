import os
def install_package():
    try:
        import tdqm
        import requests
        import retry
        import multitasking
    except ModuleNotFoundError:
        r = os.popen("pip install tqdm requests multitasking retry -i https://pypi.tuna.tsinghua.edu.cn/simple some-package")
        r = os.system("python -m pip install tqdm requests multitasking retry -i https://pypi.tuna.tsinghua.edu.cn/simple some-package")
        r = os.system("pip3 install tqdm requests multitasking retry -i https://pypi.tuna.tsinghua.edu.cn/simple some-package")
        return 2 # 包安装完成
    return 0
r = install_package()
if r == 2:
    import tdqm,requests,retry,multitasking
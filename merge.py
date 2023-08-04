import os
import sys

def merge(dir):
    '''
    dir: 指定imgs下目录名，如 '20230804''
    '''
    path = os.path.join(os.path.dirname(__file__), 'imgs', dir)
    os.chdir(path)
    print(os.getcwd())

    # powershell 批量重命名脚本
    # ps1 = "dir *.jpg | %{$x=0} {Rename-Item $_ -NewName \"Base$($x.tostring(\'0000\')).jpg\"; $x++ }"
    
    # 需提前安装配置ffmpeg
    # list.txt按行记录，格式 'file xxxx.jpg'
    os.system(f'ffmpeg -r 2 -f concat -i list.txt {dir}.mp4 -y')


if __name__ == '__main__':
    if len(sys.argv)>1:
        merge(sys.argv[1])


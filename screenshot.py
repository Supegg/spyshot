from PIL import ImageGrab, ImageDraw, ImageFont
import time, os
from win32 import win32gui, win32print
from win32.lib import win32con
from win32.win32api import GetSystemMetrics


def get_real_resolution():
    """获取真实的分辨率"""
    hDC = win32gui.GetDC(0)
    # 横向分辨率
    w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    # 纵向分辨率
    h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
    return w, h


def get_screen_size():
    """获取缩放后的分辨率"""
    w = GetSystemMetrics (0)
    h = GetSystemMetrics (1)
    return w, h


def shot():
    width, height = get_real_resolution()
    
    now = time.localtime()
    dir = os.path.join(os.path.dirname(__file__), 'imgs')
    if not os.path.exists(dir):
        os.mkdir(dir)
    dir = os.path.join(os.path.dirname(__file__), 'imgs/' + time.strftime("%Y%m%d", now))
    if not os.path.exists(dir):
        os.mkdir(dir)

    name = time.strftime("%H_%M_%S", now)

    img = ImageGrab.grab(bbox=(0, 0, width, height))
    draw = ImageDraw.Draw(img)
    fontStyle = ImageFont.truetype("SimHei.ttf", 50, encoding="utf-8")
    draw.text((60, 45), time.strftime("%Y-%m-%d %H:%M:%S", now), (0, 255, 0), font=fontStyle)

    img.save(f'{dir}/{name}.jpg')
    with open(f'{dir}/list.txt', 'a') as f:
        f.write(f'file {name}.jpg\n')
    img.save(f'imgs/screen.jpg')


if __name__ == "__main__":
    shot()

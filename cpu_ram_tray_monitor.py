# pip install pystray pillow psutil pywin32
# 위 모듈 설치 필요
# 파이썬 트레이 아이콘 표시 프로그램. 

import psutil
import time
import threading
import os
import sys
import win32com.client
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw

APP_NAME = "시스템모니터"
EXE_PATH = sys.executable  # .py로 실행 중이면 .exe로 교체 필요

def draw_gauge(draw, center, radius, percent, color, width=4):
    x0, y0 = center[0] - radius, center[1] - radius
    x1, y1 = center[0] + radius, center[1] + radius
    start = -90
    end = start + int(360 * percent / 100)
    draw.ellipse((x0, y0, x1, y1), outline=(220, 220, 220), width=width)
    draw.pieslice((x0, y0, x1, y1), start=start, end=end, fill=color)

# 아이콘 이미지 생성 - 막대바 형태로.
def create_icon_image(cpu_percent, ram_percent):
    width, height = 32, 32
    img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    def get_color(p):
        if p < 30: return (0, 200, 0)
        elif p < 70: return (255, 165, 0)
        else: return (255, 0, 0)

    bar_width = 10
    max_height = 28
    bottom = height - 2

    # CPU 막대
    cpu_height = int((cpu_percent / 100) * max_height)
    draw.rectangle([4, bottom - cpu_height, 4 + bar_width, bottom], fill=get_color(cpu_percent))

    # RAM 막대
    ram_height = int((ram_percent / 100) * max_height)
    draw.rectangle([18, bottom - ram_height, 18 + bar_width, bottom], fill=get_color(ram_percent))

    return img.resize((16, 16), Image.LANCZOS)

def get_startup_shortcut_path():
    startup_dir = os.path.join(os.environ["APPDATA"], "Microsoft\\Windows\\Start Menu\\Programs\\Startup")
    return os.path.join(startup_dir, f"{APP_NAME}.lnk")

def is_in_startup():
    return os.path.exists(get_startup_shortcut_path())

def toggle_startup(icon, item):
    shortcut_path = get_startup_shortcut_path()
    if is_in_startup():
        os.remove(shortcut_path)
        item.checked = False
    else:
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.Targetpath = EXE_PATH
        shortcut.WorkingDirectory = os.path.dirname(EXE_PATH)
        shortcut.IconLocation = EXE_PATH
        shortcut.save()
        item.checked = True
    icon.update_menu()

def monitor_loop(icon):
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent

        new_icon = create_icon_image(cpu, ram)
        icon.icon = new_icon  # 변경된 이미지 할당
        icon.title = f"CPU: {cpu}% | RAM: {ram}%"
        time.sleep(2)

def on_exit(icon, item):
    icon.visible = False
    icon.stop()

def main():
    startup_item = MenuItem(
        "시작 시 실행",
        toggle_startup,
        checked=lambda item: is_in_startup()
    )
    icon = Icon(APP_NAME)
    icon.menu = Menu(startup_item, MenuItem("종료", on_exit))
    icon.icon = create_icon_image(0, 0)
    threading.Thread(target=monitor_loop, args=(icon,), daemon=True).start()
    icon.run()

if __name__ == "__main__":
    main()
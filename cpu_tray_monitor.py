# pip install psutil pystray pillow
# 파이썬 트레이 아이콘 표시 프로그램. 
# 위의 모듈 설치해야 함.
import psutil
import time
import threading
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw, ImageFont
import math

# 폰트 설정 (Windows 기본 폰트 사용)
FONT_PATH = "C:/Windows/Fonts/arial.ttf"


def create_icon_image(cpu_percent):
    """CPU 사용률에 따라 게이지 스타일의 원형 아이콘 생성"""
    img = Image.new('RGBA', (64, 64), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # 색상 선택
    if cpu_percent < 30:
        fill_color = (0, 200, 0)       # 초록
    elif cpu_percent < 70:
        fill_color = (255, 165, 0)     # 주황
    else:
        fill_color = (255, 0, 0)       # 빨강

    # 배경 원 (회색 테두리)
    draw.ellipse((4, 4, 60, 60), outline=(200, 200, 200), width=4)

    # 게이지 각도 계산
    angle = int((cpu_percent / 100.0) * 360)
    start_angle = -90  # 위에서 시작

    # 게이지 그리기 (호 형태)
    draw.pieslice((4, 4, 60, 60), start=start_angle, end=start_angle + angle, fill=fill_color)

    return img.resize((16, 16), Image.LANCZOS)
def cpu_monitor_loop(icon):
    """CPU 사용률을 주기적으로 업데이트"""
    while icon.visible:
        cpu = psutil.cpu_percent(interval=1)
        icon.icon = create_icon_image(cpu)
        icon.title = f"CPU 사용률: {cpu}%"
        time.sleep(2)

def on_exit(icon, item):
    icon.visible = False
    icon.stop()

def main():
    icon = Icon("CPU 사용률")
    icon.menu = Menu(MenuItem("종료", lambda icon, item: on_exit(icon, item)))
    icon.icon = create_icon_image(0)
    
    # 백그라운드에서 업데이트 루프 실행
    threading.Thread(target=cpu_monitor_loop, args=(icon,), daemon=True).start()

    icon.run()

if __name__ == "__main__":
    main()
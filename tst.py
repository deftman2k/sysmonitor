import random

def create_icon_image(cpu_percent, ram_percent):
    # 랜덤 색상으로 테스트해보기
    img = Image.new('RGBA', (64, 64), (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    return img.resize((16, 16), Image.LANCZOS)

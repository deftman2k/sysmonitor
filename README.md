# 🖥️ 시스템 트레이 CPU/RAM 사용량 모니터

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Windows](https://img.shields.io/badge/Platform-Windows%2010%2F11-blue)
![License](https://img.shields.io/badge/License-MIT-green)

작업 표시줄(시스템 트레이)에 **CPU 및 RAM 사용률을 실시간 게이지로 시각화**해주는 경량 모니터링 도구입니다.

## 🎯 주요 기능

- 🟢 CPU / RAM 실시간 사용률 모니터링
- 📊 아이콘에 원형 게이지 또는 막대 그래프로 사용률 표시
- 🖱️ 트레이 우클릭 메뉴:
  - 시작 시 자동 실행 설정
  - 작업 관리자 바로 열기
  - 종료

---

## 📸 실행 화면

| 트레이 아이콘 | 우클릭 메뉴 |
|---------------|-------------|
| ![icon](docs/icon_sample.png) | ![menu](docs/context_menu.png) |

---

## 🛠️ 설치 방법

### 1. 패키지 설치
```bash
pip install -r requirements.txt
```

2. 실행
```bash
python cpu_ram_tray_monitor.py
```

3. 실행 파일 빌드 (PyInstaller)
```bash
pyinstaller cpu_ram_tray_monitor.spec --upx-dir="C:\Tools\upx"
※ myicon.ico 아이콘 파일 과 UPX 압축 은 선택 사항입니다.(--upx-dir 옵션 빼시면 됩니다)
```

📂 주요 파일
파일명	설명
cpu_ram_tray_monitor.py	메인 실행 스크립트
cpu_ram_tray_monitor.spec	PyInstaller 빌드 설정 파일
myicon.ico	(선택) 실행 파일 아이콘
requirements.txt	필요한 파이썬 패키지 목록

🧩 향후 추가 예정 기능
.

📃 라이선스
MIT License

🙋‍♂️ 제작자
Chris Park .
문의 및 제안은 Issues 또는 Pull Request로 남겨주세요.

Dropee SN Design

Automation Engine for Dropee Tasks

Developed by SN DESIGN STUDIO

---

Overview

Dropee SN Design is an automation engine designed to automate tasks inside the Dropee ecosystem.

This project provides an automated system capable of handling multiple operational modules including task automation, reward handling, tap automation, and account management.

The tool is designed for use in Termux environments and optimized for lightweight execution.

---

Features

• Auto Task Engine
• Auto Reward System
• Tap Automation
• Multi Account Manager
• Lightweight Termux Compatible
• Modular Python Architecture

---

Requirements

Before installing the system make sure you have:

- Termux
- Python 3.10 or higher
- Git
- Internet connection

---

Installation Guide

Step 1 — Update Termux

Open Termux and run:

pkg update && pkg upgrade -y

---

Step 2 — Install Required Packages

pkg install git -y
pkg install python -y

Verify installation:

python --version
git --version

---

Step 3 — Clone Repository

git clone https://github.com/Narong69za/dropee-sn-design.git

Enter project folder:

cd dropee-sn-design

---

Step 4 — Install Python Dependencies

pip install -r requirements.txt

---

Step 5 — Configure Accounts

Open the account file:

nano accounts/accounts.txt

Insert your token on each line:

TOKEN_ACCOUNT_1
TOKEN_ACCOUNT_2

Save the file.

---

Step 6 — Run The Program

python main.py

---

Project Structure

dropee-sn-design/

core/
modules/
utils/
data/

config/
accounts/
logs/
scripts/

main.py
requirements.txt

---

Video Tutorial

You can watch the full setup tutorial here:

YouTube
https://youtube.com/your-video-link

The tutorial explains:

• How to install Termux
• How to clone the repository
• How to extract the Dropee token
• How to run the automation system

---

Author

SN DESIGN STUDIO

GitHub
https://github.com/Narong69za

---

License

MIT License

Copyright (c) 2026 SN DESIGN STUDIO

---

ภาษาไทย (Thai Documentation)

ภาพรวมระบบ

Dropee SN Design เป็นระบบ Automation สำหรับช่วยจัดการงานต่าง ๆ ภายในระบบ Dropee แบบอัตโนมัติ

ตัวโปรแกรมถูกออกแบบให้สามารถทำงานบน Termux และใช้ภาษา Python ในการพัฒนา

ระบบสามารถช่วยทำงานอัตโนมัติ เช่น

- ทำ Task อัตโนมัติ
- กด Tap อัตโนมัติ
- รับ Reward อัตโนมัติ
- รองรับหลายบัญชี

---

คุณสมบัติของระบบ

• ระบบ Auto Task
• ระบบ Auto Reward
• ระบบ Tap Automation
• รองรับหลาย Account
• โครงสร้าง Modular Python
• ใช้งานบน Termux ได้ง่าย

---

ขั้นตอนการติดตั้ง

ขั้นตอนที่ 1 อัพเดท Termux

เปิด Termux แล้วรัน

pkg update && pkg upgrade -y

---

ขั้นตอนที่ 2 ติดตั้งแพคเกจที่จำเป็น

pkg install git -y
pkg install python -y

ตรวจสอบเวอร์ชัน

python --version
git --version

---

ขั้นตอนที่ 3 Clone โปรเจค

git clone https://github.com/Narong69za/dropee-sn-design.git

เข้าโฟลเดอร์โปรเจค

cd dropee-sn-design

---

ขั้นตอนที่ 4 ติดตั้ง Python Dependencies

pip install -r requirements.txt

---

ขั้นตอนที่ 5 ใส่ Token ของบัญชี

เปิดไฟล์

nano accounts/accounts.txt

ใส่ Token ของบัญชีในแต่ละบรรทัด

ตัวอย่าง

TOKEN_ACCOUNT_1
TOKEN_ACCOUNT_2

---

ขั้นตอนที่ 6 รันโปรแกรม

python main.py

---

ผู้พัฒนา

SN DESIGN STUDIO

GitHub
https://github.com/Narong69za

---

License

MIT License

Copyright (c) 2026 SN DESIGN STUDIO

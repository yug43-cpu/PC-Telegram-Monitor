# PC Telegram Monitor

A Windows PC monitoring tool that sends important PC and internet status information to a private Telegram channel.

The monitor runs locally on the PC and starts automatically after Windows login using Task Scheduler.

No VPS or separate server is required.

---

## Features

* PC online status
* PC ON time
* PC OFF duration
* Current uptime
* Internet connected/disconnected status
* Internet disconnect duration
* Download speed
* Upload speed
* Local IP address
* Public IP address
* High download speed alert
* High upload speed alert
* Live Telegram status message
* Automatic Windows startup
* Multiple PC support

---

## Requirements

Before starting, make sure you have:

* Windows PC
* Internet connection
* Python 3
* Git
* Telegram account
* Telegram Bot
* Private Telegram channel

---

## 1. Create Telegram Bot

Open Telegram and search for:

```text
@BotFather
```

Start BotFather:

```text
/start
```

Create a new bot:

```text
/newbot
```

Follow the instructions.

BotFather will provide a Bot Token.

Example:

```text
123456789:XXXXXXXXXXXXXXXXXXXXXXXX
```

Keep the token private.

Do not upload the token to GitHub.

---

## 2. Create Telegram Channel

Create a private Telegram channel.

Example:

```text
My PC Monitor
```

Open the channel settings:

```text
Channel Info
→ Administrators
→ Add Administrator
```

Add your Telegram bot as an administrator.

Give the bot permission to:

```text
Post Messages
```

---

## 3. Get Telegram Chat ID

You need the Chat ID of your private channel.

The Chat ID normally looks similar to:

```text
-1001234567890
```

Save this value.

You will use it in the `.env` file.

---

## 4. Install Python

Install Python on the Windows PC.

During installation, enable:

```text
Add Python to PATH
```

After installation, open Command Prompt or PowerShell.

Check Python:

```bash
python --version
```

Example:

```text
Python 3.13.x
```

If the version is displayed, Python is installed correctly.

---

## 5. Install Git

Install Git for Windows.

Check the installation:

```bash
git --version
```

Example:

```text
git version 2.x.x
```

---

## 6. Clone the Project

Open Command Prompt or PowerShell.

Go to the location where you want to keep the project.

Example:

```bash
cd Desktop
```

Clone the repository:

```bash
git clone https://github.com/yug43-cpu/PC-Telegram-Monitor.git
```

Open the project:

```bash
cd PC-Telegram-Monitor
```

Check the project files:

```bash
dir
```

---

## 7. Create Virtual Environment

Inside the project folder, create a Python virtual environment:

```bash
python -m venv venv
```

This creates the local `venv` folder.

---

## 8. Activate Virtual Environment

Activate the virtual environment:

```bash
venv\Scripts\activate
```

You should see `(venv)` at the beginning of the command line.

Example:

```text
(venv) C:\Users\YourName\Desktop\PC-Telegram-Monitor>
```

---

## 9. Install Required Packages

Make sure the virtual environment is active.

Run:

```bash
pip install -r requirements.txt
```

The required packages will be installed automatically.

---

## 10. Create .env File

Inside the main project folder, create a file named:

```text
.env
```

Add:

```env
BOT_TOKEN=YOUR_BOT_TOKEN
CHAT_ID=YOUR_CHAT_ID
PC_NAME=Home-PC
```

Replace:

```text
YOUR_BOT_TOKEN
```

with the token from BotFather.

Replace:

```text
YOUR_CHAT_ID
```

with your Telegram channel Chat ID.

Set your PC name using:

```text
PC_NAME=Home-PC
```

Example:

```env
BOT_TOKEN=123456789:XXXXXXXXXXXXXXXXXXXXXXXX
CHAT_ID=-1001234567890
PC_NAME=Home-PC
```

The `.env` file contains private information.

Never upload it to GitHub.

---

## 11. Test the Monitor

Before configuring automatic startup, test the monitor manually.

Make sure the virtual environment is active:

```bash
venv\Scripts\activate
```

Run:

```bash
python monitor\monitor.py
```

Check your Telegram channel.

The bot should send the PC monitoring information.

Example:

```text
🖥️ Home-PC

🟢 PC ONLINE

⏰ ON: 07:30:20 AM
⏱️ Uptime: 2h 15m

🌐 NETWORK

📍 Local IP: 192.168.x.x
🌍 Public IP: xxx.xxx.xxx.xxx

🟢 INTERNET CONNECTED

📥 Download: 2.50 MB/s
📤 Upload: 0.30 MB/s
```

If the message appears in Telegram, the monitor is working.

Stop the monitor with:

```text
Ctrl + C
```

---

## 12. Live Status Updates

The monitor creates one main Telegram status message.

Instead of sending a new message every minute, it edits the existing message.

The status is updated every:

```text
60 seconds
```

The live message contains:

* PC status
* ON time
* Uptime
* Internet status
* Local IP
* Public IP
* Download speed
* Upload speed
* Last update time

---

## 13. High Speed Alerts

The monitor checks network speed.

The alert threshold is:

```text
10 MB/s
```

If download speed becomes greater than:

```text
10 MB/s
```

the bot sends a high download speed alert.

If upload speed becomes greater than:

```text
10 MB/s
```

the bot sends a high upload speed alert.

The bot does not repeatedly send alerts while the speed stays above the threshold.

The alert resets when the speed returns to normal.

Example:

```text
Normal
↓
12 MB/s
↓
Alert sent
↓
15 MB/s
↓
No repeated alert
↓
5 MB/s
↓
Alert reset
↓
13 MB/s
↓
New alert
```

---

## 14. Internet Disconnect Alerts

When the internet connection is lost, the bot sends an alert.

Example:

```text
🔴 INTERNET DISCONNECTED
```

When the connection comes back:

```text
🟢 INTERNET RESTORED
```

The restored message also shows approximately how long the internet was disconnected.

Example:

```text
🟢 INTERNET RESTORED

⏱️ Disconnected for: 8m 25s
```

---

## 15. PC ON / Restart Detection

When Windows starts a new session, the monitor detects the change and can send a PC ON notification.

Example:

```text
🟢 PC ON

🖥️ Home-PC
⏰ Time: 07:30:20 AM
🕐 PC was OFF for: 6h 45m
```

The OFF duration is calculated using the monitor's saved state.

A sudden power failure, crash, or forced power-off may not always be detected as a normal shutdown.

---

# Automatic Windows Startup

After confirming that the monitor works manually, configure Windows Task Scheduler.

This allows the monitor to start automatically whenever you log in to Windows.

---

## 16. Open Task Scheduler

Open the Windows Start Menu.

Search for:

```text
Task Scheduler
```

Open it.

Click:

```text
Create Task
```

---

## 17. General Settings

Open the:

```text
General
```

tab.

Set:

```text
Name:
PC Telegram Monitor
```

Select:

```text
Run only when user is logged on
```

Enable:

```text
Run with highest privileges
```

---

## 18. Trigger Settings

Open:

```text
Triggers
```

Click:

```text
New
```

Set:

```text
Begin the task:
At log on
```

Select:

```text
Any user
```

Click:

```text
OK
```

The monitor will now start automatically after Windows login.

---

## 19. Action Settings

Open:

```text
Actions
```

Click:

```text
New
```

Select:

```text
Start a program
```

For:

```text
Program/script
```

enter the path to:

```text
pythonw.exe
```

Example:

```text
C:\Users\YourName\Desktop\PC-Telegram-Monitor\venv\Scripts\pythonw.exe
```

For:

```text
Add arguments
```

enter:

```text
C:\Users\YourName\Desktop\PC-Telegram-Monitor\monitor\monitor.py
```

For:

```text
Start in
```

enter:

```text
C:\Users\YourName\Desktop\PC-Telegram-Monitor
```

Important:

Use `pythonw.exe` instead of `python.exe`.

`pythonw.exe` allows the monitor to run without opening a Command Prompt window.

Replace `YourName` with your Windows username.

---

## 20. Find Your Python Path

If you do not know your virtual environment path, activate the environment:

```bash
venv\Scripts\activate
```

Then run:

```bash
python -c "import sys; print(sys.executable)"
```

Example output:

```text
C:\Users\YourName\Desktop\PC-Telegram-Monitor\venv\Scripts\python.exe
```

For Task Scheduler, change:

```text
python.exe
```

to:

```text
pythonw.exe
```

So the final program path becomes:

```text
C:\Users\YourName\Desktop\PC-Telegram-Monitor\venv\Scripts\pythonw.exe
```

---

## 21. Conditions

Open:

```text
Conditions
```

If you want the monitor to run regardless of whether the PC is connected to AC power, disable:

```text
Start the task only if the computer is on AC power
```

For a desktop PC, this normally does not matter.

---

## 22. Settings

Open:

```text
Settings
```

Make sure this option is enabled:

```text
Allow task to be run on demand
```

Click:

```text
OK
```

to create the task.

---

## 23. Test Automatic Startup

In Task Scheduler, find:

```text
PC Telegram Monitor
```

Right-click it and select:

```text
Run
```

Check Telegram.

The monitor should start.

Now restart Windows.

After logging in, the monitor should automatically start.

You do not need to manually run:

```bash
python monitor\monitor.py
```

every time.

---

# Multiple PC Setup

You can use the same project on multiple Windows PCs.

Each PC should have its own local configuration and monitoring data.

All PCs can use the same:

```text
Telegram Bot
Telegram Channel
GitHub Repository
```

---

## 24. Setup Another PC

On the second PC, install Python and Git.

Clone the project:

```bash
git clone https://github.com/yug43-cpu/PC-Telegram-Monitor.git
```

Open the project:

```bash
cd PC-Telegram-Monitor
```

Create the virtual environment:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

---

## 25. Configure the Second PC

Create a new `.env` file on the second PC:

```env
BOT_TOKEN=YOUR_BOT_TOKEN
CHAT_ID=YOUR_CHAT_ID
PC_NAME=Office-PC
```

Use the same:

```text
BOT_TOKEN
CHAT_ID
```

but give the PC a different:

```text
PC_NAME
```

Example:

PC 1:

```env
PC_NAME=Home-PC
```

PC 2:

```env
PC_NAME=Office-PC
```

Each PC should have its own `.env`.

Do not copy the `.env` file through GitHub.

---

## 26. Test the Second PC

Run:

```bash
python monitor\monitor.py
```

The Telegram message should identify the PC:

```text
🖥️ Office-PC
```

After testing, configure Task Scheduler on the second PC using the same automatic startup process.

---

## 27. Important Multiple PC Rule

Do not copy:

```text
monitor_data.json
```

from one PC to another.

Each PC must create and maintain its own monitoring data.

Example:

```text
Home-PC
└── monitor_data.json

Office-PC
└── monitor_data.json
```

---

# Project Structure

```text
PC-Telegram-Monitor/
│
├── monitor/
│   ├── monitor.py
│   ├── telegram.py
│   ├── storage.py
│   └── monitor_data.json
│
├── venv/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

Local/private files:

```text
.env
venv/
monitor/monitor_data.json
```

These should remain locally.

---

# Troubleshooting

## Telegram message is not received

Check:

```text
BOT_TOKEN
CHAT_ID
```

Also make sure:

* The bot is added to the channel.
* The bot is an administrator.
* The bot has permission to post messages.
* Internet is working.

---

## Monitor works manually but not automatically

Check Task Scheduler.

Make sure:

```text
Trigger:
At log on
```

Program:

```text
...\venv\Scripts\pythonw.exe
```

Arguments:

```text
...\monitor\monitor.py
```

Start in:

```text
...\PC-Telegram-Monitor
```

---

## Wrong PC name

Open `.env` and check:

```env
PC_NAME=Home-PC
```

Change it to the required PC name.

Restart the monitor after changing `.env`.

---

## Python package error

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Then run:

```bash
pip install -r requirements.txt
```

---

# Quick Setup

For a new PC:

```bash
git clone https://github.com/yug43-cpu/PC-Telegram-Monitor.git
cd PC-Telegram-Monitor
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env`:

```env
BOT_TOKEN=YOUR_BOT_TOKEN
CHAT_ID=YOUR_CHAT_ID
PC_NAME=Home-PC
```

Test:

```bash
python monitor\monitor.py
```

If Telegram works, configure Windows Task Scheduler:

```text
Trigger:
At log on

Program:
...\venv\Scripts\pythonw.exe

Arguments:
...\monitor\monitor.py

Start in:
...\PC-Telegram-Monitor
```

Restart Windows and log in.

The monitor should start automatically.

---

# License

For personal use, learning, and experimentation.

#MADE BY YUG❤️

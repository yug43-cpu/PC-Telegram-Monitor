# PC Telegram Monitor

A simple Windows PC monitoring tool that sends important PC and internet information to a private Telegram channel.

The monitor runs automatically in the background and updates one live Telegram message.

No VPS or separate server is required.

---

## Features

* PC online status
* PC ON time
* PC uptime
* PC OFF duration
* Internet connected/disconnected status
* Internet disconnect duration
* Download speed
* Upload speed
* Local IP address
* Public IP address
* High download speed alert
* High upload speed alert
* Live Telegram status message
* Automatic start after Windows login
* Support for multiple PCs

---

## How It Works

```text
Windows PC
    ↓
PC Telegram Monitor
    ↓
Telegram Bot
    ↓
Private Telegram Channel
```

The monitor runs directly on the Windows PC.

For multiple PCs:

```text
PC 1 ──┐
       │
PC 2 ──┼──→ Same Telegram Bot
       │          ↓
PC 3 ──┘    Same Private Channel
```

---

# 1. Requirements

You need:

* Windows PC
* Internet connection
* Python
* Git
* Telegram account
* Private Telegram channel
* Telegram Bot

---

# 2. Install Python

Download and install Python.

During Python installation, make sure this option is enabled:

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
Python 3.x.x
```

If the Python version appears, Python is installed correctly.

---

# 3. Install Git

Install Git for Windows.

After installation, open Command Prompt or PowerShell.

Check Git:

```bash
git --version
```

Example:

```text
git version 2.x.x
```

If the version appears, Git is installed correctly.

---

# 4. Create Telegram Bot

Open Telegram.

Search for:

```text
@BotFather
```

Open BotFather.

Send:

```text
/start
```

Then send:

```text
/newbot
```

BotFather will ask for a bot name.

Example:

```text
PC Monitor Bot
```

Then it will ask for a username.

Example:

```text
my_pc_monitor_bot
```

The username should end with:

```text
bot
```

BotFather will give you a Bot Token.

It will look similar to:

```text
123456789:XXXXXXXXXXXXXXXXXXXXXXXX
```

Keep this token private.

Do not upload it to GitHub.

---

# 5. Create Private Telegram Channel

Create a new Telegram channel.

Example:

```text
My PC Monitor
```

Set the channel as:

```text
Private
```

---

# 6. Add Bot to Telegram Channel

Open your Telegram channel.

Go to:

```text
Channel Info
↓
Administrators
↓
Add Administrator
```

Search for your bot.

Add the bot as an administrator.

Give the bot permission to:

```text
Post Messages
```

The bot needs permission to send messages to the channel.

---

# 7. Get Telegram Chat ID

You need the Telegram channel Chat ID.

For a private channel, it normally looks similar to:

```text
-1001234567890
```

Save this Chat ID.

You will add it to the `.env` file later.

Keep your Telegram configuration private.

---

# 8. Clone the GitHub Repository

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

Go inside the project:

```bash
cd PC-Telegram-Monitor
```

Check the files:

```bash
dir
```

You should see files similar to:

```text
monitor
.gitignore
requirements.txt
README.md
```

---

# 9. Create Python Virtual Environment

Inside the project folder, run:

```bash
python -m venv venv
```

This creates:

```text
venv/
```

The virtual environment keeps this project's Python packages separate from other Python projects.

---

# 10. Activate Virtual Environment

Run:

```bash
venv\Scripts\activate
```

You should now see:

```text
(venv)
```

at the beginning of the terminal.

Example:

```text
(venv) C:\Users\YourName\Desktop\PC-Telegram-Monitor>
```

---

# 11. Install Required Packages

Make sure `(venv)` is visible in the terminal.

Then run:

```bash
pip install -r requirements.txt
```

The project uses these Python packages:

```text
requests
psutil
python-dotenv
pywin32
```

---

# 12. Create .env File

Inside the main project folder, create a file named:

```text
.env
```

Your project should look similar to:

```text
PC-Telegram-Monitor/
│
├── monitor/
├── venv/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

Open `.env`.

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

with the token received from BotFather.

Replace:

```text
YOUR_CHAT_ID
```

with your Telegram channel Chat ID.

Change the PC name if you want.

Example:

```env
BOT_TOKEN=123456789:XXXXXXXXXXXXXXXX
CHAT_ID=-1001234567890
PC_NAME=Home-PC
```

Do not upload `.env` to GitHub.

---

# 13. Check .gitignore

The `.gitignore` file should contain:

```gitignore
# Python
__pycache__/
*.py[cod]
*.pyo

# Virtual environment
venv/
.venv/

# Environment / secrets
.env

# Monitoring data
monitor/monitor_data.json

# Logs
*.log

# VS Code
.vscode/

# OS
Thumbs.db
Desktop.ini
```

This keeps private and unnecessary files out of GitHub.

---

# 14. Project Structure

The project will look similar to:

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
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

Some files and folders are created automatically:

```text
venv/
monitor/__pycache__/
monitor/monitor_data.json
```

These are local files.

They should not be uploaded to GitHub.

---

# 15. Test the Monitor Manually

Before making the monitor automatic, test it manually.

Make sure the virtual environment is active:

```bash
venv\Scripts\activate
```

Run:

```bash
python monitor\monitor.py
```

Check your Telegram channel.

You should receive a message similar to:

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

If the Telegram message arrives, the monitor is working.

Stop the program with:

```text
Ctrl + C
```

---

# 16. Live Telegram Message

The monitor creates one main status message.

It does not create a new status message every minute.

The same message is edited and updated.

Example:

```text
🖥️ Home-PC

🟢 PC ONLINE

⏱️ Uptime: 3h 20m

🟢 INTERNET CONNECTED

📥 Download: 3.25 MB/s
📤 Upload: 0.45 MB/s

🔄 Last Update: 10:30:00 AM
```

The current update interval is:

```text
60 seconds
```

---

# 17. High Speed Alerts

The monitor checks download and upload speed.

The alert threshold is:

```text
10 MB/s
```

If download speed becomes greater than:

```text
10 MB/s
```

the bot sends:

```text
🚨 HIGH DOWNLOAD SPEED
```

If upload speed becomes greater than:

```text
10 MB/s
```

the bot sends:

```text
🚨 HIGH UPLOAD SPEED
```

The bot does not repeatedly send alerts while the speed remains high.

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
No new alert
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

# 18. Internet Disconnect Alert

When the internet disconnects, the bot sends:

```text
🔴 INTERNET DISCONNECTED
```

When the internet comes back:

```text
🟢 INTERNET RESTORED
```

The restored message also shows the disconnect duration.

Example:

```text
🟢 INTERNET RESTORED

⏱️ Disconnected for: 8m 25s
```

---

# 19. PC ON / Restart Detection

When Windows starts again, the monitor detects the new Windows session.

It can send:

```text
🟢 PC ON
```

It can also show approximately how long the PC was OFF.

Example:

```text
🟢 PC ON

🖥️ Home-PC
⏰ Time: 07:30:20 AM
🕐 PC was OFF for: 6h 45m
```

Note:

PC OFF duration is estimated from the last saved monitoring time.

A sudden power failure or forced shutdown may not be detected as a normal shutdown event.

---

# 20. Make Monitor Start Automatically

After manual testing works, configure Windows Task Scheduler.

This makes the monitor start automatically when you log in to Windows.

Open:

```text
Start Menu
```

Search:

```text
Task Scheduler
```

Open Task Scheduler.

---

# 21. Create Automatic Startup Task

In Task Scheduler, click:

```text
Create Task
```

Do not use only the Basic Task option.

---

# 22. Task Scheduler - General

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

# 23. Task Scheduler - Trigger

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

Choose:

```text
Any user
```

Click:

```text
OK
```

Now the monitor will start automatically when the Windows user logs in.

---

# 24. Task Scheduler - Action

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

enter the path to `pythonw.exe`.

Example:

```text
C:\Users\YOUR_USERNAME\Desktop\PC-Telegram-Monitor\venv\Scripts\pythonw.exe
```

For:

```text
Add arguments
```

enter:

```text
C:\Users\YOUR_USERNAME\Desktop\PC-Telegram-Monitor\monitor\monitor.py
```

For:

```text
Start in
```

enter:

```text
C:\Users\YOUR_USERNAME\Desktop\PC-Telegram-Monitor
```

Important:

Use:

```text
pythonw.exe
```

instead of:

```text
python.exe
```

`pythonw.exe` allows the monitor to run without opening a visible Command Prompt window.

Important:

Replace `YOUR_USERNAME` with your actual Windows username.

---

# 25. How to Find Your Python Path

If you are not sure where your virtual environment Python is located, activate the environment:

```bash
venv\Scripts\activate
```

Then run:

```bash
python -c "import sys; print(sys.executable)"
```

It will show something similar to:

```text
C:\Users\YourName\Desktop\PC-Telegram-Monitor\venv\Scripts\python.exe
```

For Task Scheduler, use:

```text
pythonw.exe
```

instead of:

```text
python.exe
```

So the path becomes:

```text
C:\Users\YourName\Desktop\PC-Telegram-Monitor\venv\Scripts\pythonw.exe
```

---

# 26. Task Scheduler - Conditions

Open:

```text
Conditions
```

If you want the monitor to work while the PC is running on battery, disable:

```text
Start the task only if the computer is on AC power
```

For a desktop PC, this setting normally does not matter.

---

# 27. Task Scheduler - Settings

Open:

```text
Settings
```

Make sure:

```text
Allow task to be run on demand
```

is enabled.

Click:

```text
OK
```

to save the task.

---

# 28. Test Automatic Startup

First test the task manually.

In Task Scheduler:

```text
PC Telegram Monitor
↓
Right Click
↓
Run
```

Check Telegram.

The monitor should start.

Now restart Windows.

After Windows starts and you log in, the monitor should start automatically.

You should receive or see the Telegram monitoring message.

If this works, automatic startup is complete.

---

# 29. What Happens After Windows Restart?

The complete process is:

```text
Windows Restart
      ↓
Windows Login
      ↓
Task Scheduler starts
      ↓
pythonw.exe starts
      ↓
monitor.py starts
      ↓
PC and Internet information is checked
      ↓
Telegram message is sent
      ↓
Live message keeps updating
```

You do not need to manually open the Python program every time.

---

# 30. Run the Monitor Manually

If you want to run it manually:

Go to the project folder:

```bash
cd PC-Telegram-Monitor
```

Activate virtual environment:

```bash
venv\Scripts\activate
```

Run:

```bash
python monitor\monitor.py
```

Stop it with:

```text
Ctrl + C
```

---

# 31. Multiple PC Setup

This section is optional.

You can use the same GitHub project on multiple Windows PCs.

You do not need a separate GitHub repository for every PC.

Example:

```text
PC 1 ──┐
       │
PC 2 ──┼──→ Same Telegram Bot
       │          ↓
PC 3 ──┘    Same Private Channel
```

Each PC should have its own:

```text
.env
venv/
monitor_data.json
```

---

# 32. Setup Second PC

On the second PC, install:

```text
Python
Git
```

Then open Command Prompt or PowerShell.

Clone the same project:

```bash
git clone https://github.com/yug43-cpu/PC-Telegram-Monitor.git
```

Go inside:

```bash
cd PC-Telegram-Monitor
```

Create virtual environment:

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

# 33. Create .env on Second PC

Create a new:

```text
.env
```

Use the same bot and channel:

```env
BOT_TOKEN=YOUR_BOT_TOKEN
CHAT_ID=YOUR_CHAT_ID
PC_NAME=Second-PC
```

The important part is the different:

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

---

# 34. Test Second PC

Run:

```bash
python monitor\monitor.py
```

Check Telegram.

You should see:

```text
🖥️ Office-PC
```

This makes it easy to know which PC sent the information.

After testing, configure Task Scheduler on the second PC using the same automatic startup steps.

---

# 35. Example With Two PCs

PC 1 `.env`:

```env
BOT_TOKEN=YOUR_BOT_TOKEN
CHAT_ID=YOUR_CHAT_ID
PC_NAME=Home-PC
```

PC 2 `.env`:

```env
BOT_TOKEN=YOUR_BOT_TOKEN
CHAT_ID=YOUR_CHAT_ID
PC_NAME=Office-PC
```

Telegram can then show:

```text
🖥️ Home-PC
🟢 PC ONLINE
```

and:

```text
🖥️ Office-PC
🟢 PC ONLINE
```

Both PCs can use the same Telegram bot and same private channel.

---

# 36. Each PC Has Its Own Data

Each PC creates its own:

```text
monitor/monitor_data.json
```

Example:

```text
PC 1
└── monitor_data.json

PC 2
└── monitor_data.json
```

Do not copy the file from one PC to another.

Each PC should maintain its own monitoring history.

---

# 37. Do Not Upload Private Files

Never upload these to GitHub:

```text
.env
venv/
monitor/monitor_data.json
```

The `.env` file contains private Telegram information.

The `venv` folder contains installed Python packages.

The `monitor_data.json` file contains local monitoring data.

---

# 38. Updating the Project

If the project is updated on GitHub, go to the project folder and run:

```bash
git pull
```

Example:

```bash
cd PC-Telegram-Monitor
git pull
```

If `requirements.txt` was changed, activate the virtual environment:

```bash
venv\Scripts\activate
```

Then install the updated packages:

```bash
pip install -r requirements.txt
```

---

# 39. Important Files

```text
monitor/monitor.py
```

Main monitoring program.

```text
monitor/telegram.py
```

Telegram send and edit functions.

```text
monitor/storage.py
```

Stores local monitoring information.

```text
monitor/monitor_data.json
```

Local monitoring data.

Do not upload it to GitHub.

```text
.env
```

Telegram Bot Token, Chat ID and PC name.

Do not upload it to GitHub.

```text
requirements.txt
```

Required Python packages.

```text
.gitignore
```

Files that should not be uploaded to GitHub.

```text
README.md
```

Complete project setup and instructions.

---

# 40. Troubleshooting

## Python is not working

Check:

```bash
python --version
```

If it does not work, reinstall Python.

During installation enable:

```text
Add Python to PATH
```

---

## Git is not working

Check:

```bash
git --version
```

If it does not work, install Git for Windows.

---

## Virtual environment is not activating

Make sure you are inside the project folder.

Then run:

```bash
venv\Scripts\activate
```

---

## Telegram message is not received

Check:

```text
BOT_TOKEN
CHAT_ID
```

Make sure the bot is an administrator of the Telegram channel.

Make sure the bot has permission to post messages.

---

## Monitor works manually but not automatically

Check Task Scheduler.

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

Trigger:

```text
At log on
```

Also make sure the Task Scheduler task is enabled.

---

## Wrong PC name appears

Open:

```text
.env
```

Check:

```env
PC_NAME=Home-PC
```

or:

```env
PC_NAME=Office-PC
```

Restart the monitor after changing `.env`.

---

# 41. Quick Setup

If you forget the complete process later, follow these steps.

Clone:

```bash
git clone https://github.com/yug43-cpu/PC-Telegram-Monitor.git
```

Enter project:

```bash
cd PC-Telegram-Monitor
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

Create:

```text
.env
```

Add:

```env
BOT_TOKEN=YOUR_BOT_TOKEN
CHAT_ID=YOUR_CHAT_ID
PC_NAME=Home-PC
```

Test:

```bash
python monitor\monitor.py
```

If Telegram works, configure:

```text
Task Scheduler
↓
Create Task
↓
Trigger: At log on
↓
Program: pythonw.exe
↓
Arguments: monitor\monitor.py
↓
Start in: PC-Telegram-Monitor
```

Restart Windows.

After Windows login, the monitor should start automatically.

---

# 42. Complete One PC Setup Flow

```text
Install Python
      ↓
Install Git
      ↓
Create Telegram Bot
      ↓
Create Private Channel
      ↓
Add Bot as Administrator
      ↓
Get Chat ID
      ↓
Clone GitHub Repository
      ↓
Create Python venv
      ↓
Activate venv
      ↓
Install requirements
      ↓
Create .env
      ↓
Add Bot Token + Chat ID + PC Name
      ↓
Run monitor manually
      ↓
Test Telegram
      ↓
Create Windows Task Scheduler Task
      ↓
Set Trigger: At log on
      ↓
Set pythonw.exe
      ↓
Set monitor.py as argument
      ↓
Save Task
      ↓
Restart Windows
      ↓
Monitor starts automatically
```

---

# 43. Complete Multiple PC Setup Flow

```text
Same GitHub Repository
        ↓
Clone on each PC
        ↓
Create venv on each PC
        ↓
Install requirements
        ↓
Create separate .env
        ↓
Use different PC_NAME
        ↓
Create separate monitor_data.json
        ↓
Configure Task Scheduler on each PC
        ↓
Use same Telegram Bot
        ↓
Use same Telegram Channel
        ↓
Monitor all PCs from Telegram
```

---

# 44. Project Goal

This project is made for personal PC and internet monitoring.

It runs locally on Windows and sends important information to Telegram.

No VPS is required.

No separate monitoring server is required.

The same project can be used on one PC or multiple PCs.

---

# License

This project is for personal use, learning, and experimentation.

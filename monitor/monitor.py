import os
import time
import requests
import psutil
import socket
from datetime import datetime

from dotenv import load_dotenv

from telegram import send_message, edit_message
from storage import load_data, save_data

import win32api


# ================================
# Configuration
# ================================

load_dotenv()

PC_NAME = os.getenv("PC_NAME", "PC")

UPDATE_INTERVAL = 60
SPEED_SAMPLE_INTERVAL = 1
INTERNET_CHECK_TIMEOUT = 5

INTERNET_TEST_URL = "https://www.google.com/generate_204"
PUBLIC_IP_URL = "https://api.ipify.org"

HIGH_SPEED_THRESHOLD = 10.0


# ================================
# Time Functions
# ================================

def get_now():
    return datetime.now()


def get_boot_time():
    return datetime.fromtimestamp(psutil.boot_time())


def get_pc_uptime():
    return int(time.time() - psutil.boot_time())


def format_duration(seconds):
    days, seconds = divmod(int(seconds), 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    parts = []

    if days:
        parts.append(f"{days}d")

    if hours:
        parts.append(f"{hours}h")

    if minutes:
        parts.append(f"{minutes}m")

    if seconds or not parts:
        parts.append(f"{seconds}s")

    return " ".join(parts)


def format_time(value):
    if not value:
        return "-"

    try:
        dt = datetime.fromisoformat(value)
        return dt.strftime("%I:%M:%S %p")

    except ValueError:
        return "-"


# ================================
# Internet Functions
# ================================

def check_internet():
    try:
        response = requests.get(
            INTERNET_TEST_URL,
            timeout=INTERNET_CHECK_TIMEOUT
        )

        return response.status_code in (200, 204)

    except requests.RequestException:
        return False


def get_local_ip():
    socket_connection = None

    try:
        socket_connection = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )

        socket_connection.connect(("8.8.8.8", 80))

        local_ip = socket_connection.getsockname()[0]

        return local_ip

    except OSError:
        return "Unavailable"

    finally:
        if socket_connection:
            socket_connection.close()


def get_public_ip():
    try:
        response = requests.get(
            PUBLIC_IP_URL,
            timeout=5
        )

        if response.ok:
            return response.text.strip()

        return "Unavailable"

    except requests.RequestException:
        return "Unavailable"


# ================================
# Network Speed
# ================================

def get_network_speed(interval=SPEED_SAMPLE_INTERVAL):
    before = psutil.net_io_counters()

    time.sleep(interval)

    after = psutil.net_io_counters()

    download_bytes = after.bytes_recv - before.bytes_recv
    upload_bytes = after.bytes_sent - before.bytes_sent

    download_mb = (
        download_bytes / interval / (1024 * 1024)
    )

    upload_mb = (
        upload_bytes / interval / (1024 * 1024)
    )

    return download_mb, upload_mb


# ================================
# Telegram Live Status
# ================================

def create_status_message(
    data,
    internet,
    download,
    upload,
    local_ip,
    public_ip
):
    uptime = get_pc_uptime()

    if internet:
        internet_status = "🟢 INTERNET CONNECTED"
    else:
        internet_status = "🔴 INTERNET DISCONNECTED"

    message = f"""🖥️ {PC_NAME}
━━━━━━━━━━━━━━━━━━

🟢 PC ONLINE

⏰ ON: {format_time(data.get("current_pc_on"))}
⏱️ Uptime: {format_duration(uptime)}

🌐 NETWORK

📍 Local IP: {local_ip}
🌍 Public IP: {public_ip}

{internet_status}

📥 Download: {download:.2f} MB/s
📤 Upload: {upload:.2f} MB/s
"""

    last_disconnect = data.get(
        "last_internet_disconnect"
    )

    if last_disconnect:
        start = format_time(
            last_disconnect.get("start")
        )

        end = format_time(
            last_disconnect.get("end")
        )

        duration = format_duration(
            last_disconnect.get("duration", 0)
        )

        message += f"""
🔴 Last Internet Disconnect
{start} → {end}
⏱️ {duration}
"""

    last_pc_off = data.get("last_pc_off")

    if last_pc_off:
        start = format_time(
            last_pc_off.get("start")
        )

        end = format_time(
            last_pc_off.get("end")
        )

        duration = format_duration(
            last_pc_off.get("duration", 0)
        )

        message += f"""
🔴 Last PC OFF
{start} → {end}
⏱️ {duration}
"""

    message += f"""
🔄 Last Update: {get_now().strftime("%I:%M:%S %p")}
"""

    return message


# ================================
# Telegram Alerts
# ================================

def send_internet_disconnect_alert():
    message = f"""🔴 INTERNET DISCONNECTED

🖥️ {PC_NAME}
⏰ Time: {get_now().strftime("%I:%M:%S %p")}
"""

    send_message(message)


def send_internet_restored_alert(duration):
    message = f"""🟢 INTERNET RESTORED

🖥️ {PC_NAME}
⏰ Time: {get_now().strftime("%I:%M:%S %p")}
⏱️ Disconnected for: {format_duration(duration)}
"""

    send_message(message)


def send_pc_on_alert(off_duration):
    message = f"""🟢 PC ON

🖥️ {PC_NAME}
⏰ Time: {get_now().strftime("%I:%M:%S %p")}
🕐 PC was OFF for: {format_duration(off_duration)}
"""

    send_message(message)


def send_pc_off_alert():
    message = f"""🔴 PC OFF

🖥️ {PC_NAME}
⏰ Time: {get_now().strftime("%I:%M:%S %p")}
"""

    send_message(message)


def send_high_download_alert(speed):
    message = f"""🚨 HIGH DOWNLOAD SPEED

🖥️ {PC_NAME}
📥 {speed:.2f} MB/s
⏰ {get_now().strftime("%I:%M:%S %p")}
"""

    send_message(message)


def send_high_upload_alert(speed):
    message = f"""🚨 HIGH UPLOAD SPEED

🖥️ {PC_NAME}
📤 {speed:.2f} MB/s
⏰ {get_now().strftime("%I:%M:%S %p")}
"""

    send_message(message)


# ================================
# Windows Shutdown Handler
# ================================

def shutdown_handler(ctrl_type):
    if ctrl_type in (2, 5, 6):
        print("Windows shutdown detected.")

        now = get_now()

        data = load_data()

        data["last_pc_off"] = {
            "start": now.isoformat(),
            "end": now.isoformat(),
            "duration": 0
        }

        data["last_seen"] = now.isoformat()

        save_data(data)

        send_pc_off_alert()

        return True

    return False


# ================================
# Main Monitor
# ================================

def main():
    print("PC Monitor Started")
    print("------------------")
    print(f"PC Name: {PC_NAME}")

    # Enable Windows shutdown detection
    try:
        win32api.SetConsoleCtrlHandler(
            shutdown_handler,
            True
        )

        print("Windows shutdown handler enabled.")

    except Exception as error:
        print("Shutdown handler could not start:")
        print(error)

    # Load previous monitoring data
    data = load_data()

    current_time = get_now()
    current_boot_time = get_boot_time()

    previous_boot_time = data.get("boot_time")
    previous_seen = data.get("last_seen")

    pc_was_rebooted = False

    # Check whether Windows was restarted
    if previous_boot_time:
        try:
            old_boot_time = datetime.fromisoformat(
                previous_boot_time
            )

            if old_boot_time != current_boot_time:
                pc_was_rebooted = True

        except ValueError:
            pass

    # Handle PC startup
    if pc_was_rebooted and previous_seen:
        try:
            previous_seen_time = datetime.fromisoformat(
                previous_seen
            )

            off_duration = (
                current_time - previous_seen_time
            ).total_seconds()

            data["last_pc_off"] = {
                "start": previous_seen,
                "end": current_time.isoformat(),
                "duration": off_duration
            }

            print(
                "Estimated PC OFF duration:",
                format_duration(off_duration)
            )

            send_pc_on_alert(off_duration)

        except ValueError:
            print("Previous PC time data is invalid.")

    elif not previous_boot_time:
        print("First PC monitor run.")

    else:
        print("Monitor restarted on the same Windows session.")

    # Save current PC information
    data["pc_name"] = PC_NAME
    data["boot_time"] = current_boot_time.isoformat()

    if not data.get("current_pc_on") or pc_was_rebooted:
        data["current_pc_on"] = current_boot_time.isoformat()

    data["last_seen"] = current_time.isoformat()

    # Check internet
    current_internet = check_internet()

    data["internet_connected"] = current_internet

    if not current_internet:
        if not data.get("internet_disconnect_start"):
            data["internet_disconnect_start"] = (
                current_time.isoformat()
            )

    save_data(data)

    # Get IP information
    local_ip = get_local_ip()

    if current_internet:
        public_ip = get_public_ip()
    else:
        public_ip = "Unavailable"

    # Get network speed
    download, upload = get_network_speed()

    # Create live status message
    message = create_status_message(
        data,
        current_internet,
        download,
        upload,
        local_ip,
        public_ip
    )

    print(message)

    # Send initial Telegram message
    message_id = send_message(message)

    if not message_id:
        print("Failed to send Telegram message.")
        return

    print("Live Telegram monitoring started.")

    previous_internet = current_internet

    # High-speed alert state
    download_high_alerted = (
        download > HIGH_SPEED_THRESHOLD
    )

    upload_high_alerted = (
        upload > HIGH_SPEED_THRESHOLD
    )

    # ================================
    # Continuous Monitoring
    # ================================

    while True:
        time.sleep(UPDATE_INTERVAL)

        current_time = get_now()

        # Check internet
        current_internet = check_internet()

        # Internet disconnected
        if previous_internet and not current_internet:
            print("Internet disconnected.")

            data["internet_disconnect_start"] = (
                current_time.isoformat()
            )

            send_internet_disconnect_alert()

        # Internet restored
        elif not previous_internet and current_internet:
            print("Internet restored.")

            disconnect_start = data.get(
                "internet_disconnect_start"
            )

            if disconnect_start:
                try:
                    start_time = datetime.fromisoformat(
                        disconnect_start
                    )

                    disconnect_duration = (
                        current_time - start_time
                    ).total_seconds()

                    data["last_internet_disconnect"] = {
                        "start": disconnect_start,
                        "end": current_time.isoformat(),
                        "duration": disconnect_duration
                    }

                    send_internet_restored_alert(
                        disconnect_duration
                    )

                except ValueError:
                    print(
                        "Internet disconnect time is invalid."
                    )

            data["internet_disconnect_start"] = None

        # Save current state
        data["pc_name"] = PC_NAME
        data["internet_connected"] = current_internet
        data["last_seen"] = current_time.isoformat()

        save_data(data)

        # Get IP information
        local_ip = get_local_ip()

        if current_internet:
            public_ip = get_public_ip()
        else:
            public_ip = "Unavailable"

        # Get network speed
        download, upload = get_network_speed()

        # ================================
        # High Download Alert
        # ================================

        if download > HIGH_SPEED_THRESHOLD:
            if not download_high_alerted:
                send_high_download_alert(download)
                download_high_alerted = True

        else:
            download_high_alerted = False

        # ================================
        # High Upload Alert
        # ================================

        if upload > HIGH_SPEED_THRESHOLD:
            if not upload_high_alerted:
                send_high_upload_alert(upload)
                upload_high_alerted = True

        else:
            upload_high_alerted = False

        # Create updated status
        message = create_status_message(
            data,
            current_internet,
            download,
            upload,
            local_ip,
            public_ip
        )

        # Edit the same Telegram message
        if edit_message(message_id, message):
            print(
                "Status updated:",
                current_time.strftime("%I:%M:%S %p")
            )

        else:
            print("Failed to update status.")

        previous_internet = current_internet


# ================================
# Start Program
# ================================

if __name__ == "__main__":
    main()
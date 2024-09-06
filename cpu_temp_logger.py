import subprocess
from datetime import datetime
import os

MAX_LINES = 20000

# 获取当前脚本文件的目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# log.txt文件的完整路径
log_file_path = os.path.join(script_dir, 'log.txt')

def log_message(message):
    with open(log_file_path, 'a', encoding='utf-8') as log_file:
        log_file.write(f'{message}\n')

def trim_log_file():
    try:
        with open(log_file_path, 'r', encoding='utf-8') as log_file:
            lines = log_file.readlines()
        if len(lines) > MAX_LINES:
            with open(log_file_path, 'w', encoding='utf-8') as log_file:
                log_file.writelines(lines[-MAX_LINES:])
    except FileNotFoundError:
        pass

# 获取sensors命令的输出
try:
    result = subprocess.run(['/usr/bin/sensors'], stdout=subprocess.PIPE, text=True, check=True)
    output = result.stdout
except Exception as e:
    log_message(f"Error running sensors command: {e}")
    output = ""

# 获取当前时间
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 记录时间和sensors命令的输出
log_message(current_time)
log_message(output.strip())
log_message('/*********************************************************************/')

# 修剪log.txt文件
trim_log_file()

print("Core temperatures have been written to log.txt")

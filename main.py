import paramiko
import pyautogui
import os
from dotenv import load_dotenv

load_dotenv('.env')
host = os.environ.get('HOST')
port = int(os.environ.get('PORT'))
username = os.environ.get('USER')
password = os.environ.get('PASSWORD')


def check_font(host, port, username, password):

    # Создание объекта SSHClient
    ssh = paramiko.SSHClient()
    # Игнорирование неизвестных хостов
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Подключение к серверу
        ssh.connect(host, port, username, password)

        # Отправка команды на сервер
        stdin, stdout, stderr = ssh.exec_command('/file print where name ="disk1/dude/files/arial.ttf"')

        # Вывод результата выполнения команды
        a = stdout.read().decode()
        a = a.split()
        shrift = '.ttf'
        if shrift not in a:
            copy(host, port, username, password)
        else:
            pyautogui.alert(text="Шрифт уже есть в директории!", title="Уведомление", button="OK")
    except Exception as e:
        pyautogui.alert(text=f"Ошибка: {e}", title="Error", button="OK")
    finally:
        # Закрытие соединения
        ssh.close()


def copy(host, port, username, password):
    transport = paramiko.Transport((host, port))
    try:
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        remotepath = 'disk1/dude/files/arial.ttf'
        localpath = 'arial.ttf'
        sftp.put(localpath, remotepath)
        pyautogui.alert(text="Шрифт успешной скопирован!", title="Уведомление", button="OK")
    except Exception as e:
        pyautogui.alert(text=f"Ошибка: {e}", title="Error", button="OK")
    finally:
        sftp.close()
        transport.close()


check_font(host, port, username, password)


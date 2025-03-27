# SSH Font Installer for Dude (MikroTik)

Этот скрипт на Python копирует шрифт Arial на сервер Dude (MikroTik) через SSH, чтобы обеспечить поддержку русского языка в интерфейсе.

## Требования

- Python 3.x
- Установленный пакет `paramiko` (для работы с SSH)
- Файл `.env` с параметрами подключения

## Установка

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```
2. Установите зависимости:
   ```sh
   pip install -r requirements.txt
   ```
3. Создайте файл `.env` в корневой директории проекта и добавьте в него следующие параметры:
   ```ini
   HOST=192.168.1.1
   PORT=22
   USERNAME=login
   PASSWORD=password
   ```


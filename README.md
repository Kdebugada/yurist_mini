# Telegram Бот для Мини-приложения Юридических Услуг

Этот бот предназначен для запуска мини-приложения Telegram с юридическими услугами в ОАЭ. Бот разработан с использованием aiogram 3.x.

## Установка

### Обычная установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Kdebugada/yurist_mini.git
cd yurist_mini
```

2. Установите зависимости:

**Windows:**
```bash
install_dependencies.bat
```

**Linux/Mac:**
```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```

Или вручную:
```bash
pip install -r requirements.txt
```

3. Настройте переменные окружения:
   - Создайте файл `.env` в корневой директории проекта
   - Добавьте следующие переменные:
     ```
     BOT_TOKEN=ваш_токен_бота
     WEBAPP_URL=url_вашего_мини_приложения
     ```

### Установка с использованием Docker

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Kdebugada/yurist_mini.git
cd yurist_mini
```

2. Настройте переменные окружения (как описано выше)

3. Запустите контейнер с помощью Docker Compose:

**Windows:**
```bash
start_docker.bat
```

**Linux/Mac:**
```bash
chmod +x start_docker.sh
./start_docker.sh
```

Или вручную:
```bash
docker-compose up -d
```

## Запуск бота

### Обычный запуск

**Windows:**
```bash
start_bot.bat
```

**Linux/Mac:**
```bash
chmod +x start_bot.sh
./start_bot.sh
```

Или вручную:
```bash
python bot.py
```

### Запуск через Docker

**Windows:**
```bash
start_docker.bat
```

**Linux/Mac:**
```bash
chmod +x start_docker.sh
./start_docker.sh
```

Или вручную:
```bash
docker-compose up -d
```

### Просмотр логов Docker-контейнера

**Windows:**
```bash
logs_docker.bat
```

**Linux/Mac:**
```bash
chmod +x logs_docker.sh
./logs_docker.sh
```

Или вручную:
```bash
docker-compose logs -f
```

### Остановка Docker-контейнера

**Windows:**
```bash
stop_docker.bat
```

**Linux/Mac:**
```bash
chmod +x stop_docker.sh
./stop_docker.sh
```

Или вручную:
```bash
docker-compose down
```

## Функциональность

- При запуске бота командой `/start` пользователь получает приветственное сообщение с кнопкой для открытия мини-приложения
- Бот также отвечает на любые текстовые сообщения, предлагая открыть мини-приложение
- Доступны команды:
  - `/start` - запуск бота
  - `/help` - получение помощи
  - `/info` - информация о услугах
  - `/contact` - контактная информация

## Структура проекта

- `bot.py` - основной файл бота
- `requirements.txt` - зависимости проекта
- `.env` - файл с переменными окружения
- `Dockerfile` - файл для создания Docker-образа
- `docker-compose.yml` - файл для запуска через Docker Compose
- `start_bot.bat` и `start_bot.sh` - скрипты для запуска бота
- `install_dependencies.bat` и `install_dependencies.sh` - скрипты для установки зависимостей
- `start_docker.bat` и `start_docker.sh` - скрипты для запуска бота через Docker
- `logs_docker.bat` и `logs_docker.sh` - скрипты для просмотра логов Docker-контейнера
- `stop_docker.bat` и `stop_docker.sh` - скрипты для остановки Docker-контейнера
- `*.html` - файлы мини-приложения Telegram

## Особенности aiogram 3.x

В этом проекте используется aiogram версии 3.x, которая имеет следующие особенности:
- Асинхронный подход к обработке сообщений
- Использование роутеров для организации обработчиков
- Улучшенная система фильтров
- Поддержка FSM (Finite State Machine) для управления состояниями диалога
- Встроенная поддержка мини-приложений Telegram

## Примечание

Убедитесь, что ваше мини-приложение Telegram правильно настроено и доступно по указанному URL. 
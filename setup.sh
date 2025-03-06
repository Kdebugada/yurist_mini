#!/bin/bash

# Обновление системы
apt update && apt upgrade -y

# Установка необходимых пакетов
apt install -y nginx python3 python3-pip git

# Создание директории для сайта
mkdir -p /var/www/yurist_mini

# Клонирование репозитория
cd /var/www
git clone https://github.com/Kdebugada/yurist_mini.git

# Настройка nginx
cp nginx.conf /etc/nginx/sites-available/yurist
ln -s /etc/nginx/sites-available/yurist /etc/nginx/sites-enabled/
rm /etc/nginx/sites-enabled/default
nginx -t && systemctl restart nginx

# Установка зависимостей Python
cd /var/www/yurist_mini
pip3 install -r requirements.txt

# Настройка systemd сервиса для бота
cp yurist-bot.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable yurist-bot
systemctl start yurist-bot

# Настройка автоматического обновления из git
echo "*/5 * * * * cd /var/www/yurist_mini && git pull origin main" | crontab -

echo "Установка завершена!" 
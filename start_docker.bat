@echo off
echo Запуск бота в Docker-контейнере...
docker-compose up -d
echo Бот запущен в фоновом режиме!
echo Для просмотра логов используйте команду: docker-compose logs -f
pause 
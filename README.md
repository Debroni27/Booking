# Booking API (FastAPI)

Проект, который позволяет реализовать сервис бронирования, рекомендаций отелей для пользователей по всему миру!


> **Примечание**
>
> Эта реализация которая подходит в первую очередь мне для определенныx бизнес задач.
> Такая струкрура проекта далеко не универсальная для каждого.
> Для более подробного ознакомления с [FastAPI](https://docs.djangoproject.com)
>

## Описание шаблона
Это описание, которое помогает быстро развернуть проект и запустить минимальные сервисы в [Docker](https://docs.docker.com):

1) Для начала создаем нужную директорию для работы с проектом `mkdir {folder_name}` и переходим туда `cd {folder_name}` 
2) Проверяем наличие git `git --version`, в случае его отсутствия установит [Git](https://git-scm.com) 
3) Делаем `git clone https://github.com/Debroni27/Booking.git`, после `git remote -v`, что remote exist
4) Создаем виртуальное окружение и активируем его `python3.* -m venv venv` -> `source/venv/bin/activate`
5) Устанавливаем все зависимости `pip install poetry` -> `poetry install`
6) В корне проекта создаем env файл `touch .env`
-> Для вашего проекта делайте свой environe
7) Проверяем наличие docker и docker-compose `docker --version`, `docker-compose --version`. При отсутствии установить
8) Поочереди начинаем билдить сервисы `docker-compose up --build mongodb`, затем `server`

В итоге у нас есть готовая база в контейнере, есть запущенный django проект

> **Примечание**
1. Папка .github для ci и пуша НЕ в ветку мастера, а скорее для работы с flow
2. Папка fixtures для работы с тестовыми значениями либо чтобы наполнить базу и поиграться
3. Папка remote_services для интергации с внешними API системами
4. Папка `src` хранит структуру проекта, а тесты вынесесны отдельно
5. [Makefile](https://makefiletutorial.com/) - для удобного запуска нужных команд под разные ОС
6. Все взаимодействия внутри контейнера идут от папки `backend`
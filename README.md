# Новостной сервис

Данный проект - это тестовое задание. Суть заключается в разработке back-end сервиса новостей, в котором будет REST API для получения новостей с комментариями.

## Требования

Перед установкой убедитесь, что у вас установлены:

- Python 3.10+
- Docker и Docker Compose
- Make (если отсутствует, команды можно выполнять вручную, заглянув в `Makefile`)

## Установка и запуск

### 1. Клонирование репозитория
```sh
git clone https://github.com/DazeSsS/udv-test-case
cd udv-test-case
```

### 2. Установка зависимостей
Убедитесь, что у ваc создано и активировано виртуальное окружение:
```sh
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Настройка окружения
Создайте файл `.env` в корне проекта и заполните его, опираясь на `.env.example`


### 4. Запуск, подготовка тестовых данных и остановка
```sh
make up # поднимает все контейнеры (БД и приложение)
make populate # заполняет БД исходными данными (хранятся в /src/seed_data/)
make down # удаляет все контейнеры
```

### 5. Дополнительные команды
Все команды и их описание можно посмотреть в `Makefile`, но вот основные:
```sh
make rebuild # Сборка и перезапуск приложения
make clear # Очистка данных из таблиц
make drop # Удаление всех таблиц
make revision m=<описание_миграции> # Создание файла миграций
make migrate # Применение миграций вручную
```

### 6. Доступ к API
После запуска API будет доступен по адресу:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)  
Документация Swagger:  
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

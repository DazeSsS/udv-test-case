revision: # Создание миграций (после выполнения БД остается работать)
	docker compose run --build --rm app alembic revision --autogenerate -m "$m"

migrate: # Применение миграций (после выполнения БД остается работать)
	docker compose run --build --rm app alembic upgrade head

populate: # Заполнить БД тестовыми данными из файлов в /src/seed_data/ (все прошлые данные стираются)
	docker compose run --build --rm app python3 -m src.scripts.populate_db

drop: # Удалить все таблицы из БД
	docker compose run --build --rm app python3 -m src.scripts.drop_db

clear: # Очистить таблицы в БД (служебные не трогаются)
	docker compose run --build --rm app python3 -m src.scripts.clear_db

db: # Запустить БД в контейнере
	docker compose up -d db

rebuild: build down up # Пересобрать и перезапустить приложение

build: # Собрать образ приложения
	docker compose build

up: # Поднять контейнеры
	docker compose up -d

down: # Завершить работу контейнеров
	docker compose down

start: # Возобновить работу контейнеров
	docker compose start

stop: # Остановить работу контейнеров
	docker compose stop

restart: # Перезапустить контейнеры
	docker compose restart

prune: # Очистить старые образы
	docker system prune
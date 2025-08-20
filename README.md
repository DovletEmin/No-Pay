# No-Pay

No-Pay — это веб-приложение на Django и Django REST Framework для работы с каталогом продуктов, корзиной и заказами. Проект поддерживает регистрацию пользователей, JWT аутентификацию и управление заказами через API.

## Особенности

- Регистрация и аутентификация пользователей (JWT)
- Каталог продуктов с категориями
- Управление корзиной (добавление, удаление товаров)
- Создание и оплата заказов
- Автоматическая генерация документации API (Swagger / OpenAPI)

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/username/no-pay.git
cd no-pay
```

2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Примените миграции:

```bash
python manage.py migrate
```

5. Создайте суперпользователя:

```bash
python manage.py createsuperuser
```

6. Запустите сервер разработки:

```bash
python manage.py runserver
```

## API Endpoints

### Аутентификация

- `POST /api/auth/register/` — регистрация пользователя
- `POST /api/token/` — получение JWT
- `POST /api/token/refresh/` — обновление JWT

### Каталог

- `GET /api/catalog/categories/` — список категорий
- `GET /api/catalog/products/` — список продуктов

### Корзина

- `GET /api/cart/` — просмотр корзины
- `POST /api/cart/` — добавить товар в корзину
- `DELETE /api/cart/<product_id>/` — удалить товар из корзины

### Заказы

- `GET /api/orders/` — список заказов пользователя
- `POST /api/orders/` — создать заказ

### Платежи

- `POST /api/payments/charge/` — эмуляция оплаты заказа

### Документация API

- Swagger UI: `/api/swagger/`
- OpenAPI Schema: `/api/schema/`

## Тесты

### Запуск тестов:

```bash
pytest
```

# Lab02_pyaternyashki

## Опис проєкту

Навчальний проєкт на Python, що містить Telegram-бота та консольні програми для роботи з числами, паролями, текстом і списком завдань.

## Можливості

- **Telegram-бот** (`main.py`) — взаємодія з користувачами через Telegram.
- **Гра «Вгадай число»** (`guess_number.py`) — вгадування випадкового числа.
- **Генератор паролів** (`password_generator.py`) — створення випадкових паролів.
- **Лічильник слів** (`word_counter.py`) — аналіз тексту.
- **TODO CLI** (`todo_cli.py`) — додавання, перегляд, виконання та видалення завдань із збереженням у JSON-файл.

## Встановлення

1. Переконайтеся, що у вас встановлено Python 3.
2. Клонуйте репозиторій:

    ```bash
    git clone https://github.com/awaikoi/Lab02_pyaternyashki.git
    cd Lab02_pyaternyashki
    ```

3. Встановіть залежності:

    ```bash
    pip install -r requirements.txt
    ```

## Налаштування Telegram-бота

Створіть файл `.env` у кореневій директорії проєкту та додайте токен бота:

```env
BOT_TOKEN=your_bot_token_here
```

Замініть `your_bot_token_here` на токен, отриманий від [BotFather](https://t.me/BotFather).

## Використання

Запустіть потрібну програму командою:

```bash
python main.py
python guess_number.py
python password_generator.py
python word_counter.py
```

Для перегляду доступних команд менеджера завдань виконайте:

```bash
python todo_cli.py --help
```

Основні команди TODO CLI:

```bash
python todo_cli.py add Вивчити Python
python todo_cli.py list
python todo_cli.py done 1
python todo_cli.py remove 1
```

Завдання зберігаються у файлі `todo.json`.

## Технології

- Python 3
- Git і GitHub
- JSON
- Бібліотеки, зазначені в `requirements.txt`

## Призначення

Проєкт створено з навчальною метою для практичного застосування Python та роботи з системою контролю версій Git.

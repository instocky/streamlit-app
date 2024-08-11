# Streamlit Demo App

For video tutorial: [Streamlit: The Fastest Way To Build Python Apps?](https://www.youtube.com/watch?v=D0D4Pa22iG0&lc=Ugz_mHQgRHlnn1BJqlx4AaABAg)

# Команды для разворачивания приложения

## 1. Создание виртуального окружения
```bash
python -m venv venv
```

## 2. Активация виртуального окружения
### Для Windows:
```bash
.\venv\Scripts\activate
```
### Для macOS и Linux:
```bash
source venv/bin/activate
```

## 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

## 4. Запуск приложения
```bash
streamlit run app.py
```

## Дополнительные команды

### Обновление pip (рекомендуется)
```bash
python -m pip install --upgrade pip
```

### Создание requirements.txt (если его нет)
```bash
pip freeze > requirements.txt
```

### Деактивация виртуального окружения
```bash
deactivate
```
# Используем образ Python 3.11
FROM python:3.11

# Устанавливаем рабочую директорию
WORKDIR /product_manager

# Копируем файлы проекта
COPY ./requirements.txt /product_manager/requirements.txt
COPY ./app /product_manager/app
COPY ./tests /product_manager/tests

# Устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade -r /product_manager/requirements.txt

# Добавляем рабочую директорию и папку приложения в PYTHONPATH
ENV PYTHONPATH=/product_manager:/product_manager/app

# Указываем команду для запуска приложения
CMD ["python", "app/main.py"]
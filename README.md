# product_management
Управление продуктами на ТП
## Оглавление
- [Описание](#описание)
- [Требования](#Предварительные-требования-для-установки-и-запуска)
- [Запуск](#Запуск-api-с-использованием-Dockerfile)
- [Лецензия](#лицензия)
## Описание
Проект для выполнения CRUD операций с продуктами и категориями.
Разработан с использованием технологии FastAPI, которая предоставляет возможности для
создания, получения, удаления, измениния товаров и категорий этих товаров.  
Для проверки правильности работы API были написаны тесты с использованием pytest.  
На момент публикации все тесты работают корректно.  
## Предварительные требования для установки и запуска
- Docker Desktop
- Git
## Запуск api с использованием Dockerfile
1. Клонируйте репозиторий проекта
```sh
git clone https://github.com/MaximPik/product_management.git
```
2. Перейдите в рабочую директорию product_management
```sh
cd product_management
```
3. Соберите образ Docker.
```sh
docker build -t marketplace-crud-app -f Dockerfile .
```
4. Запустите контейнер.
```sh
docker run -d -p 8080:8080 marketplace-crud-app
```
5. Можно использовать.
Откройте браузер и перейдите по адресу http://localhost:8080/docs для доступа к приложению.
## Запуск api с использованием DockerHub
1. Запустите контейнер Docker из Docker Hub
```sh
docker run -d -p 8080:8080 maximpik2/marketplace-crud-app:latest
```
2. Можно использовать.
Откройте браузер и перейдите по адресу http://localhost:8080/docs для доступа к приложению.
## Запуск тестов с использованием Dockerfile
1. Клонируйте репозиторий проекта
```sh
git clone https://github.com/MaximPik/product_management.git
```
2. Перейдите в рабочую директорию product_management
```sh
cd product_management
```
3. Соберите образ Docker.
```sh
docker build -t marketplace-crud-app-tests -f Dockerfile.test .
```
4. Запустите контейнер.
```sh
docker run -d -p 8080:8080 marketplace-crud-app-tests
```
5. Можно использовать.
В консоли будет информация об успешности тестов.

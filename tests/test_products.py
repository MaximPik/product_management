# Тест создания продуктов
def test_create_product(client):
    # Запрос на создание продукта
    response = client.post("/products/", json={"name": "akas",
                                               "description": "nes",
                                               "price": 4,
                                               "category_id": 1
    })

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "akas"
    assert "id" in data
    assert data["description"] == "nes"
    assert data["category_id"] == 1
    assert data["price"] == 4

# Получение продукта по ID
def test_get_product(client):
    # Запрос на создание продукта
    response = client.post("/products/", json={"name": "akas",
                                               "description": "nes",
                                               "price": 4,
                                               "category_id": 1
                                               })
    # ID созданного продукта
    product_id = response.json()["id"]
    # Получение продукта
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == product_id
    assert data["name"] == "anavas"
    assert data["description"] == "TEXT"
    assert data["price"] == 10.3
    assert data["category_id"] == 2

# Получение всех продуктов по name, price или category_id
def test_get_all_products(client):
    #Создание продукта 1
    response = client.post("/products/", json={"name": "anavas",
                                               "description": "TEXT",
                                               "price": 10.3,
                                               "category_id": 2
                                               })
    product_1 = response.json()
    # Создание продукта 2
    response = client.post("/products/", json={"name": "clesh",
                                               "description": "net",
                                               "price": 5,
                                               "category_id": 1
                                               })
    product_2 = response.json()

    #Получение всех продуктов
    response = client.get(f"/products/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2 #получение всех пользователей

    # Получение продукта по name
    response = client.get(f"/products/?name={product_1['name']}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == product_1["name"]
    assert len(data) == 1

    # Получение продукта по price
    response = client.get(f"/products/?name={product_1['price']}")
    assert response.status_code == 200
    data = response.json()
    assert data["price"] == product_1["price"]
    assert len(data) == 1

    # Получение продукта по category_id
    response = client.get(f"/products/?name={product_1['category_id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["category_id"] == product_1["category_id"]
    assert len(data) == 1

def test_update_product(client):
    # Создание продукта
    response = client.post("/products/", json={"name": "anavas",
                                               "description": "TEXT",
                                               "price": 10.3,
                                               "category_id": 2
                                               })
    product = response.json()

    # Обновление
    response = client.put(f"/products/{product['id']}", json={"name": "kaktus",
                                               "description": "neTEXT",
                                               "price": 1,
                                               "category_id": 1
                                               })
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == product['id']
    assert data["name"] == 'kaktus'
    assert data["description"] == "neTEXT"
    assert data["price"] == 1
    assert data["category_id"] == 1

def test_delete_product(client):
    # Создание продукта
    response = client.post("/products/", json={"name": "anavas",
                                               "description": "TEXT",
                                               "price": 10.3,
                                               "category_id": 2
                                               })
    product = response.json()
    assert product is not None # Пользователь создался и существует

    #удалить
    response = client.delete(f"/products/{product['id']}")
    assert response.status_code == 204  # Проверка, что удаление прошло успешно
    product = response.json()
    assert product is None # Продукта не существует

# Создание категории
def test_create_category(client):
    # Запрос на создание продукта
    response = client.post("/category/", json={"name": "vegetables"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "vegetables"
    assert "id" in data

# Получение категории
def test_get_category(client):
    # Запрос на создание категории
    response = client.post("/category/", json={"name": "vegetables"})
    # Запрос на создание категории
    response = client.post("/category/", json={"name": "fruits"})
    # Запрос на создание продукта
    response = client.get("/category/")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_category_id(client):
    # Запрос на создание категории
    response = client.post("/category/", json={"name": "vegetables"})
    # ID созданной категории
    category_id_1 = response.json()["id"]
    # Запрос на создание категории
    response = client.post("/category/", json={"name": "fruits"})
    # Создание продуктов
    response = client.post("/products/", json={"name": "potato",
                                               "description": "delicious",
                                               "price": 1,
                                               "category_id": category_id_1
                                               })
    response = client.post("/products/", json={"name": "carrot",
                                               "description": "tasty",
                                               "price": 2,
                                               "category_id": category_id_1
                                               })
    # Запрос на получение категории
    response = client.get(f"/category/{category_id_1}")
    assert response.status_code == 200
    data = response.json()
    assert len(response.json()) == 2

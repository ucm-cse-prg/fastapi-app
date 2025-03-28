"""
Module for testing product-related API endpoints.

This module includes tests for creating, retrieving, updating, and deleting products.
Each test function interacts with the API endpoints and asserts the expected responses.
"""

import csv
import os

import pytest
from faker import Faker
from httpx import AsyncClient
from pydantic import BaseModel
from rich import print

fake = Faker()

pytestmark = pytest.mark.asyncio


script_dir = os.path.dirname(__file__)

# Load categories from a CSV file for testing purposes.
with open(f"{script_dir}/categories.csv", mode="r") as file:
    reader = csv.DictReader(file)
    categories = [row for row in reader]

# Load products from a CSV file for testing purposes.
with open(f"{script_dir}/products.csv", mode="r") as file:
    reader = csv.DictReader(file)
    products = [row for row in reader]


# Test Category model using Pydantic
@pytest.mark.skip()
class TestCategory(BaseModel):
    """
    Data model representing a product category for testing.

    Attributes:
        name (str): The name of the category.
        description (str): A description of the category.
    """

    name: str = fake.word()
    description: str = fake.sentence()


# Product model using Pydantic
@pytest.mark.skip()
class TestProduct(BaseModel):
    """
    Data model representing a product for testing.

    Attributes:
        id (PydanticObjectId or None): The unique identifier for the product.
        name (str): The name of the product.
        price (float): The price of the product.
        description (str): A description of the product.
        category (TestCategory): The category of the product.
    """

    id: str | None = None
    name: str = fake.word()
    price: float = float(fake.random_number(2)) + 0.99
    description: str = fake.sentence()
    category: TestCategory = TestCategory()


# Create a random product for testing
@pytest.mark.skip()
def create_random_product() -> TestProduct:
    """
    Create a random product for testing.
    This function generates random data for a product and returns a TestProduct instance.

    Returns:
        TestProduct: A new product instance with random data.
    """

    random_product = products[fake.random_int(0, len(products) - 1)]
    random_category = [
        cat for cat in categories if cat["CategoryID"] == random_product["Category"]
    ]

    name: str = random_product["Name"]
    price: float = float(fake.random_number(2)) + 0.99
    description: str = random_product["Description"]
    category: TestCategory = TestCategory(
        name=random_category[0]["Name"], description=random_category[0]["Description"]
    )
    return TestProduct(
        name=name, price=price, description=description, category=category
    )


# Create a list of random products for testing
products = [create_random_product() for i in range(5)]
new_product = products[0]


async def test_create_product(
    client_test: AsyncClient, new_product: TestProduct = new_product
) -> TestProduct:
    """
    Test for creating a new product.

    This test sends a POST request with product data to create a new product.
    It asserts that the API returns a status code 201 and that the returned data matches the sent payload.

    Returns:
        TestProduct: The newly created product with its assigned ID.
    """
    print("\n")
    print("Creating new product: ", new_product.name)
    # Send POST request to create the product
    response = await client_test.post("/products/", json=new_product.model_dump())
    # Assert that the product is created successfully
    print("Response from creating product: ", response.json())
    assert response.status_code == 201
    response = response.json()
    # Validate returned fields
    assert response.get("id") is not None
    assert response.get("name") == new_product.name
    assert response.get("price") == new_product.price
    assert response.get("description") == new_product.description
    new_product.id = response.get("id")
    print(
        "New product has been created: ", new_product.name, "with id: ", new_product.id
    )
    return new_product


async def test_get_product(
    client_test: AsyncClient, new_product: TestProduct = new_product
) -> TestProduct:
    """
    Test for retrieving a product.

    This test sends a GET request to fetch the product by its id.
    It validates that the API returns the product with the correct data.

    Returns:
        TestProduct: The retrieved product.
    """
    print("\n")
    print("Getting product: ", new_product.name)
    # Send GET request to retrieve the product
    response = await client_test.get(f"/products/{new_product.id}")
    assert response.status_code == 200
    response = response.json()
    # Validate returned fields
    assert response.get("id") == new_product.id
    assert response.get("name") == new_product.name
    assert response.get("price") == new_product.price
    assert response.get("description") == new_product.description
    print("Product has been retrieved: ", new_product.name)
    return new_product


async def test_update_product(
    client_test: AsyncClient, new_product: TestProduct = new_product
) -> TestProduct:
    """
    Test for updating an existing product.

    This test sends a PATCH request with updated product data.
    It asserts that the API returns status 200 and that the returned data reflects the updates.

    Returns:
        TestProduct: The updated product.
    """
    print("\n")
    print("Updating product: ", new_product.name)
    # Generate new data for the update
    new_name = fake.word()
    new_description = fake.sentence()
    new_price = fake.random_number(2) + 0.99
    # Send PATCH request to update the product
    response = await client_test.patch(
        f"/products/{new_product.id}",
        json={
            "name": new_name,
            "description": new_description,
            "price": new_price,
        },
    )
    assert response.status_code == 200
    response = response.json()
    # Validate updated fields
    assert response.get("id") == new_product.id
    assert response.get("name") == new_name
    assert response.get("price") == new_price
    assert response.get("description") == new_description
    # Update local product instance data
    new_product.name = new_name
    new_product.description = new_description
    new_product.price = new_price
    print("Product has been updated: ", new_product.name)
    return new_product


async def test_create_product_invalid_price_low(
    client_test: AsyncClient,
) -> None:
    """
    Test for creating a product with a price below the valid threshold.

    Expects a 422 status code due to validation error.
    """
    invalid_product = {
        "name": "ValidName",
        "description": "Valid product description",
        "price": -5.0,  # Invalid: less than 0
        "category": {"name": "Phones", "description": "Mobile phones"},
    }
    # Send POST request with invalid price
    response = await client_test.post("/products/", json=invalid_product)
    assert response.status_code == 422


async def test_create_product_invalid_price_high(
    client_test: AsyncClient,
) -> None:
    """
    Test for creating a product with a price above the valid threshold.

    Expects a 422 status code due to validation error.
    """
    invalid_product = {
        "name": "ValidName",
        "description": "Valid product description",
        "price": 100001,  # Invalid: greater than allowed
        "category": {"name": "Phones", "description": "Mobile phones"},
    }
    # Send POST request with invalid price
    response = await client_test.post("/products/", json=invalid_product)
    assert response.status_code == 422


async def test_create_product_invalid_name(client_test: AsyncClient) -> None:
    """
    Test for creating a product with an invalid name.

    The name includes asterisks and violates the expected regex pattern.
    Expects a 422 status code due to validation error.
    """
    invalid_product = {
        "name": "Invalid * Name",  # Contains asterisk, which is invalid
        "description": "Valid product description",
        "price": 999.99,
        "category": {"name": "Phones", "description": "Mobile phones"},
    }
    # Send POST request with invalid name
    response = await client_test.post("/products/", json=invalid_product)
    assert response.status_code == 422


async def test_update_product_invalid_data(
    client_test: AsyncClient, new_product: TestProduct = new_product
) -> None:
    """
    Test for updating a product with invalid data.

    This test uses invalid update data (name with spaces and negative price)
    and expects a 422 status code.
    """
    invalid_update = {
        "name": "Invalid Name",  # Invalid: name contains space
        "description": "Updated description",
        "price": -20.0,  # Invalid: negative price
    }
    # Send PATCH request with invalid update data
    response = await client_test.patch(
        f"/products/{new_product.id}", json=invalid_update
    )
    assert response.status_code == 422


async def test_update_product_invalid_price_not_ending_in_99(
    client_test: AsyncClient, new_product: TestProduct = new_product
) -> None:
    """
    Test for updating a product with an invalid price.

    The price does not end with '0.99' as required.
    Expects a 422 status code due to validation error.
    """
    invalid_update = {
        "name": "UpdatedName",
        "description": "Updated description",
        "price": 999.00,  # Invalid: price does not end with 0.99
    }
    # Send PATCH request with invalid price
    response = await client_test.patch(
        f"/products/{new_product.id}", json=invalid_update
    )
    assert response.status_code == 422


async def test_delete_product(
    client_test: AsyncClient, new_product: TestProduct = new_product
) -> TestProduct:
    """
    Test for deleting a product.

    This test sends a DELETE request for the specified product
    and asserts that the API returns status code 204 indicating successful deletion.

    Returns:
        TestProduct: The product that was deleted.
    """
    print("\n")
    print("Deleting product: ", new_product.name)
    # Send DELETE request to remove the product
    response = await client_test.delete(f"/products/{new_product.id}")
    assert response.status_code == 204
    print("Product has been deleted: ", new_product.name)
    return new_product


async def test_get_deleted_product(
    client_test: AsyncClient, new_product: TestProduct = new_product
) -> None:
    """
    Test for retrieving a deleted product.

    This test sends a GET request for the deleted product
    and expects a 404 status code as the product should no longer exist.
    """
    print("\n")
    print("Getting deleted product: ", new_product.name)
    # Send GET request to retrieve the deleted product
    response = await client_test.get(f"/products/{new_product.id}")
    assert response.status_code == 404
    print("Product is not found: ", new_product.name)


async def test_delete_nonexistent_product(client_test: AsyncClient) -> None:
    """
    Test for deleting a product that does not exist.

    This test sends a DELETE request for a non-existent product
    and expects a 404 status code as the product cannot be found.
    """
    print("\n")
    print("Deleting non-existent product")
    # Send DELETE request for a non-existent product
    response = await client_test.delete("/products/123456789012345678901234")
    assert response.status_code == 404
    print("Non-existent product deletion failed as expected")


async def test_update_nonexistent_product(client_test: AsyncClient) -> None:
    """
    Test for updating a product that does not exist.

    This test sends a PATCH request for a non-existent product
    and expects a 404 status code as the product cannot be found.
    """
    print("\n")
    print("Updating non-existent product")
    # Send PATCH request for a non-existent product
    response = await client_test.patch(
        "/products/123456789012345678901234", json={"name": "UpdatedName"}
    )
    assert response.status_code == 404
    print("Non-existent product update failed as expected")


async def test_create_multiple_products(
    client_test: AsyncClient, products: list[TestProduct] = products
) -> list[TestProduct]:
    """
    Test for creating multiple products.

    This test sends POST requests to create multiple products.
    It asserts that the API returns status code 201 for each product.

    Returns:
        List[TestProduct]: The list of newly created products with assigned IDs.
    """
    print("\n")
    print("Creating multiple products")
    created_products = []
    for product in products:
        response = await client_test.post("/products/", json=product.model_dump())
        assert response.status_code == 201
        response = response.json()
        assert response.get("id") is not None
        product.id = response.get("id")
        created_products.append(product)
    print("Multiple products have been created")
    print("Created products: ", products)
    return created_products


async def test_get_all_products(
    client_test: AsyncClient, test_products: list[TestProduct] = products
) -> None:
    """
    Test for retrieving all products.

    This test sends a GET request to fetch all products.
    It validates that the API returns a list of products with the expected data.
    """
    print("\n")
    print("Getting all products")
    response = await client_test.get("/products/")
    assert response.status_code == 200
    products = [TestProduct(**p) for p in response.json().get("products")]
    for p in test_products:
        assert p in products
    print("All products have been retrieved")


async def test_internal_server_error(
    client_test: AsyncClient, new_product: TestProduct = new_product
) -> None:
    """
    Test for an internal server error.

    This test manually disconnects the database connection
    and sends a request that triggers an internal server error.
    """
    print("\n")
    print("Testing internal server error")

    from motor.motor_asyncio import AsyncIOMotorClient

    from app.config import get_settings
    from app.mongo import close_mongo, drop_database

    # Connect to the database
    client: AsyncIOMotorClient = AsyncIOMotorClient(get_settings().mongodb_url)
    db = client["test_db"]

    # Update any product in the collection "products"
    await db["products"].update_one({"name": products[0].name}, {"$set": {"price": 0}})

    response = await client_test.get("/products")
    assert response.status_code == 500

    await drop_database()

    response = await client_test.get("/products")
    assert response.status_code == 200
    assert response.json().get("products") == []

    await close_mongo()

    response = await client_test.get("/products")
    print(response.json())
    # assert response.status_code == 500
    print("Internal server error has been triggered")

import typing
from functools import wraps
from typing import Optional

from app.documents import Product
from app.exceptions import InternalServerError
from app.models import Category


# Wrapper function to run action and rais InternalServerError if it fails
@typing.no_type_check
def run_action(action):
    @wraps(action)
    async def wrapper(*args, **kwargs):
        try:
            # Call the wrapped function with provided arguments.
            return await action(*args, **kwargs)
        except Exception as e:
            # Convert APIException into HTTPException with corresponding code and message.
            raise InternalServerError(str(e))

    return wrapper


# List all products
@run_action
async def get_all_products() -> list[Product]:
    products: list[Product] = await Product.find_all().to_list()
    return products


# Get a single product
async def get_product(product: Product) -> Product:
    return product


# Create a new product
async def create_product(
    name: str,
    price: float,
    category: Category,
    description: str = "",
) -> Product:
    new_product: Product = await Product(
        name=name, description=description, price=price, category=category
    ).insert()

    if not new_product:
        raise InternalServerError("Failed to create product")

    return new_product


# Update a product
async def update_product(
    product: Product,
    name: Optional[str] = None,
    description: Optional[str] = None,
    price: Optional[float] = None,
    category: Optional[Category] = None,
) -> Product:
    if name:
        product.name = name
    if description:
        product.description = description
    if price:
        product.price = price
    if category:
        product.category = category

    # Update the product
    await product.save()

    if not product:
        raise InternalServerError("Failed to update product")

    return product


async def delete_product(product: Product) -> None:
    await Product.delete(product)

    if await Product.get(product.id):
        raise InternalServerError("Failed to delete product")
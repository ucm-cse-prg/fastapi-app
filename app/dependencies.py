import typing
from functools import wraps

from fastapi import HTTPException

from app.exceptions import APIException, ProductNotFound
from app.documents import Product
from beanie import PydanticObjectId

@typing.no_type_check
def http_request_dependency(func):
    """
    A decorator to wrap asynchronous functions that interact with HTTP requests.

    This decorator catches APIException errors raised within the wrapped function and converts
    them into FastAPI's HTTPException with the appropriate status code and detail message.

    Args:
        func (Callable): The asynchronous function to wrap.

    Returns:
        Callable: The wrapped function that raises HTTPException on API errors.
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            # Call the wrapped function with provided arguments.
            return await func(*args, **kwargs)
        except APIException as e:
            # Convert APIException into HTTPException with corresponding code and message.
            raise HTTPException(status_code=e.code, detail=str(e))

    return wrapper


# CHALLENGE:
# Consider using dependency injection to handle common operations like retrieving a product by ID.


@http_request_dependency
async def get_product_by_id(product_id: PydanticObjectId) -> Product:
    product: Product | None = await Product.get(product_id)

    if not product:
        raise ProductNotFound(product_id)
    return Product

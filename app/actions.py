import typing
from functools import wraps
from app.exceptions import InternalServerError
from Beanie import PydanticObjectId
from app.documents import Product
from app.models import Category

# Wrapper function to run action and raise InternalServerError if it fails
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


# CHALLENGE:
# Remove the existing CRUD business logic.
# Your task is to implement the action functions that will perform the following:
#
# - Create a new product:
#     * Validate inputs.
#     * Insert the new product into the MongoDB collection using Beanie.
# - Retrieve products:
#     * Get all products or a specific product by ID.
# - Update an existing product:
#     * Apply changes to the product object.
#     * Save the updated product to the database.
# - Delete a product:
#     * Remove the product document from the database.
#
# Define functions like create_product, get_product, update_product, delete_product with appropriate signatures.
#



async def create_product(name: str, price: float, category: CategoryType, description: str = "") -> Product:
    newProdcut: Product = await Product(name=name,description=description, price=price, category=category).insert()

    if not newProduct:
        raise InternalServerError("Failed to create product")

    return newProduct


async def get_product(product: Product) -> Product:

    return product


async def update_product(product: Product,
                         name: Optional[str] = None, 
                         description: Optional[str] = None,
                         price: Optional[float] = None,
                         category: Optional[Category] = None) -> Product:
    if name: 
        product.name = name
    if description:
        product.description = description
    if price:
        product.price = price
    if category:
        product.category = category
    
    await product.save()

    if not product:
        raise InternalServerError("Failed to update product")
    return product

async def delete_product(product: Product) -> Product:
    await delete(product)

    if await Product.get(product.id):
        raise InternalServerError("Failed to delete product")

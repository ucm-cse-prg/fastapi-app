from fastapi import APIRouter, Depends, HTTPException, status
from app.documents import Product
from app.dependencies import get_product_by_id
from app.models import Category
import app.schemas as Schemas
import app.actions as Actions
from app.exceptions import APIException, InternalServerError, ProductNotFound

router = APIRouter()

# CHALLENGE:
# Remove any working CRUD implementations.
# Your task is to implement the following API endpoints using the Pydantic schemas,
# Beanie documents, and actions that you will build:
#
# - GET /products/      -> Retrieve all products.
# - GET /products/{id}  -> Retrieve a product by ID.
# - POST /products/     -> Create a new product.
# - PATCH /products/{id} -> Update an existing product.
# - DELETE /products/{id} -> Delete a product.
#
# For each endpoint:
# - Validate the incoming data using your custom Pydantic schemas.
# - Delegate business logic to functions in the actions module.
# - Return appropriate responses and status codes.
#

@router.get("/{product_id}", response_model=Schemas.GetProductResponse)
async def get_product(product: Product = Depends(get_product_by_id)):
    try:
        return await Actions.get_product(product)
    except APIException as e:
        raise HTTPException(status_code=e.code, detail=e.detail) 

@router.post("/", response_model=Schemas.CreateProductResponse, status_code=201)
async def create_product(product: Schemas.CreateProductRequest) -> Product:
    try:
        return await Actions.create_product(**product.model_dump())
    except APIException as e:
        raise HTTPException(status_code=e.code, detail=e.detail)

@router.patch("/{product_id}", response_model=Schemas.UpdateProductResponse)
async def update_product(
    request_body: Schemas.UpdateProductRequest, product: Product = Depends(get_product_by_id)) -> Product:
    try:
        return await Actions.update_product(product, **request_body.model_dump())
    except APIException as e:
        raise HTTPException(status_code=e.code, detail=e.detail)

@router.delete("/{product_id}",status_code=status.HTTP_204_NO_CONTENT,responses={404: {"description": "Product not found"}})
async def delete_product(product: Product = Depends(get_product_by_id)):
    try:
        await Actions.delete_product(product)
    except APIException as e:
        raise HTTPException(status_code=e.code, detail=e.detail)




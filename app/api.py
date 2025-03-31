from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, status

import app.actions as Actions
import app.documents as Documents
import app.schemas as Schemas
from app.dependencies import product_dependency
from app.exceptions import APIException

router = APIRouter()


@router.get("/", response_model=Schemas.GetAllProductsResponse)
async def get_products() -> dict[Literal["products"], list[Documents.Product]]:
    try:
        # Retrieve all products from the database.
        products: list[Documents.Product] = await Actions.get_all_products()
        return {"products": products}
    except APIException as e:
        # Raise HTTP exception if an API specific error occurs.
        raise HTTPException(status_code=e.code, detail=e.detail)


@router.get("/{product_id}", response_model=Schemas.GetProductResponse)
async def get_product(
    product: Documents.Product = Depends(product_dependency),
) -> Documents.Product:
    try:
        # Retrieve the product using the provided product_id.
        return await Actions.get_product(product)
    except APIException as e:
        # Convert API exception to HTTP exception.
        raise HTTPException(status_code=e.code, detail=e.detail)


@router.post("/", response_model=Schemas.CreateProductResponse, status_code=201)
async def create_product(product: Schemas.CreateProductRequest) -> Documents.Product:
    try:
        # Using the product data to create a new product.
        return await Actions.create_product(**product.model_dump())
    except APIException as e:
        # Convert API exception to HTTP exception.
        raise HTTPException(status_code=e.code, detail=e.detail)


@router.patch("/{product_id}", response_model=Schemas.UpdateProductResponse)
async def update_product(
    request_body: Schemas.UpdateProductRequest,
    product: Documents.Product = Depends(product_dependency),
) -> Documents.Product:
    try:
        # Update the product with the new values provided.
        return await Actions.update_product(product, **request_body.model_dump())
    except APIException as e:
        # Handle API exception by converting it into an HTTP exception.
        raise HTTPException(status_code=e.code, detail=e.detail)


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"description": "Product not found"}},
)
async def delete_product(
    product: Documents.Product = Depends(product_dependency),
) -> None:
    try:
        # Delete the product using the delete_product action.
        await Actions.delete_product(product)
    except APIException as e:
        # Convert API exception to HTTP exception if deletion fails.
        raise HTTPException(status_code=e.code, detail=e.detail)
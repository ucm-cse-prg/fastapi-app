"""
Module for defining API request and response schemas.

This module defines Pydantic models that represent the data structures for products
used in various API endpoints, such as creating, retrieving, and updating products.
These schemas help with data validation and serialization between the client and server.
"""


# CHALLENGE:
# Remove the current Pydantic request and response schemas.
# Your task is to define schemas to validate API communication.
#
# Requirements:
# - Create a CreateProductRequest schema for POST requests.
# - Create a CreateProductResponse schema for returning a created product.
# - Create a GetProductResponse schema for returning a product.
# - Create an UpdateProductRequest and UpdateProductResponse schemas for product updates.
#
# Ensure your schemas reuse the models defined in app/models.py where appropriate.
#
# Example:
#
# from pydantic import BaseModel
#
# class CreateProductRequest(BaseModel):
#     # TODO: Define required fields for creating a product
#     pass
#
# class CreateProductResponse(BaseModel):
#     # TODO: Define response fields including an 'id' field
#     pass

from typing import Optional

from beanie import PydanticObjectId
from pydantic import BaseModel

from app.models import Category, Product


class GetProductResponse(Product, BaseModel):
    id: PydanticObjectId  # Unique identifier for the product


class GetAllProductsResponse(BaseModel):
    products: list[GetProductResponse]  # List of product responses


class CreateProductRequest(Product, BaseModel):
    pass


class CreateProductResponse(GetProductResponse, BaseModel):
    pass


class UpdateProductRequest(Product, BaseModel):
    name: Optional[str] = None  # type: ignore
    description: Optional[str] = None  # type: ignore
    price: Optional[float] = None  # type: ignore
    category: Optional[Category] = None  # type: ignore


class UpdateProductResponse(GetProductResponse, BaseModel):
    pass

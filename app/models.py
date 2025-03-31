"""
Module for defining Pydantic models for the application.

This module defines the data models for Product and Category, which are used
to validate and serialize the data passed between the API client and the server.
"""

# CHALLENGE:
# Remove any existing implementations.
# Your task is to define the Pydantic models representing your data.
#
# Requirements:
# - Define a Category model with fields like name and description.
# - Define a Product model with fields such as name, description, price, and category.
# - Price should be a positive number less than 100000, and ending in ".99", i.e., 9.99, 19.99, etc.
#
# Ensure you use proper data validation and type annotations.
#
# Example:
#
# from pydantic import BaseModel
#
# class Category(BaseModel):
#     # TODO: Define fields and validations for a product category
#     pass
#
# class Product(BaseModel):
#     # TODO: Define fields and validations for a product
#     pass


from pydantic import BaseModel, Field, field_validator

class Category(BaseModel):
    name: str = Field(
        default_factory=str,
        title="Name",
        description="Name of the category",
        max_length=50,
        min_length=2,
        pattern=r"^[\w\s&]+$",
        examples=["Phones", "Accessories"],
    )
    description: str = Field(
        default="",
        title="Description",
        description="Description of the category",
        max_length=200,
        examples=["Mobile phones", "Smartphone watches, headphones, and chargers"],
    )


class Product(BaseModel):
    name: str = Field(
        default_factory=str,
        title="Name",
        description="Name of the product",
        max_length=50,
        min_length=2,
        pattern=r"^[\w\s-]+$",
        examples=["SM-G973F", "iPhone 12"],
    )
    description: str = Field(
        default="",
        title="Description",
        description="Description of the product",
        max_length=200,
        examples=["Samsung Galaxy S10", "The latest iPhone"],
    )
    price: float = Field(
        title="Price",
        description="Price of the product",
        gt=0,
        lt=100000,
        allow_inf_nan=False,
        examples=[799.99, 1299.99],
    )
    category: Category

    @field_validator("price", mode="after")
    @classmethod
    def price_ends_with_99(cls, v: float) -> float:
        if round(v % 1, 2) != 0.99:
            raise ValueError("Price must end with 0.99")
        return v
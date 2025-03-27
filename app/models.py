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



from pydantic import BaseModel, Field, field_validator, ValidationError


class Category(BaseModel):
    '''
    Category is a data model for a Product category

    Attributes:
    name (str) - name of the category
    description (str) - description of the category
    '''
    name: str     

    description: str 

class Product(BaseModel):
    '''
    Product is a data model for a Product

    Attributes:
    name (str) - name of the prodcut
    description (str) - a description of the product
    price (float) - the price of the product
    category (Category) - the category of the product
    '''
    name: str = Field(
    default_factory=str,
    title="Name",
    description="Name of the product",
    max_length=20,
    min_length=2,
    pattern=r"^[\w-]+$",
    examples=["SM-G973F", "iPhone 12"],
    )
    
    description: str

    price: float = Field (
        lt=100000,
        gt=0,
        allow_inf_nan=False,
    )

    category: Category

    @field_validator('price', mode='after')
    @classmethod
    def endsInNinetyNine(cls, value: float) -> float:
        '''
        endsInNinetyNine makes sure that the price ends in .9.99

        arguments:
        value (float) - the value we are validating

        returns:
        value (float) - the value which ends in .99
        '''
        if round(value % 1.00, 2) != .99:
            raise ValueError(f"{value} does not end in .99")
        return value




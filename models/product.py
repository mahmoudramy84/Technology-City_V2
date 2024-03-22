#!/usr/bin/python3
""" holds class product"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Product(BaseModel, Base):
    """Representation of product """
    if models.storage_t == "db":
        __tablename__ = 'products'
        user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_pieces = Column(Integer, nullable=False, default=0)
        price = Column(Integer, nullable=False, default=0)
        reviews = relationship("Review", backref="place")

    else:
        user_id = ""
        review_id = ""
        name = ""
        description = ""
        number_pieces = 0
        price = 0

    def __init__(self, *args, **kwargs):
        """initializes Product"""
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        @property
        def reviews(self):
            """getter attribute returns the list of Review instances"""
            from models.review import Review
            review_list = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.product_id == self.id:
                    review_list.append(review)
            return review_list

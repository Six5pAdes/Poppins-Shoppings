from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Product(db.Model):
    __tablename__ = 'products'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    category = db.Column(db.Enum('Clothing', 'Creativity', 'Furniture', 'Handmade', 'Miscellaneous'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate = datetime.now)

    users = db.relationship('User', back_populates='products')
    reviews = db.relationship('Review', back_populates='products', cascade="all, delete-orphan", foreign_keys="[Review.product_id]")
    order_items = db.relationship('OrderItem', back_populates='products', cascade="all, delete-orphan", foreign_keys="[OrderItem.product_id]")
    order_histories = db.relationship('OrderHistory', back_populates='products', cascade="all, delete-orphan", foreign_keys="[OrderHistory.product_id]")
    wishlists = db.relationship('Wishlist', back_populates='products', cascade="all, delete-orphan", foreign_keys="[Wishlist.product_id]")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'image': self.image,
            'price': float(self.price),
            'category': self.category,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

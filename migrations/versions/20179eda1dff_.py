"""empty message

Revision ID: 20179eda1dff
Revises:
Create Date: 2024-04-24 22:42:26.899383

"""
from alembic import op
import sqlalchemy as sa


import os
environment = os.environ.get('FLASK_ENV')
SCHEMA = os.environ.get('SCHEMA')


# revision identifiers, used by Alembic.
revision = '20179eda1dff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # product_category = sa.Enum('Clothing', 'Creativity', 'Furniture', 'Handmade', 'Miscellaneous', name='product_category')
    # product_category.create(op.get_bind(), checkfirst=True)

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=40), nullable=False),
    sa.Column('last_name', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('price', sa.Float(precision=10, asdecimal=2), nullable=False),
    sa.Column('category', sa.Enum('Clothing', 'Creativity', 'Furniture', 'Handmade', 'Miscellaneous', name='product_category'), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('carts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('is_ordered', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cart_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cart_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['carts.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_histories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wishlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
    if environment == 'production' and SCHEMA:
        op.execute(f'ALTER TABLE users SET SCHEMA {SCHEMA};')
        op.execute(f'ALTER TABLE products SET SCHEMA {SCHEMA};')
        op.execute(f'ALTER TABLE reviews SET SCHEMA {SCHEMA};')
        op.execute(f'ALTER TABLE carts SET SCHEMA {SCHEMA};')
        op.execute(f'ALTER TABLE cart_items SET SCHEMA {SCHEMA};')
        op.execute(f'ALTER TABLE order_histories SET SCHEMA {SCHEMA};')
        op.execute(f'ALTER TABLE wishlists SET SCHEMA {SCHEMA};')


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wishlists')
    op.drop_table('order_histories')
    op.drop_table('cart_items')
    op.drop_table('carts')
    op.drop_table('reviews')
    op.drop_table('products')
    op.drop_table('users')
    # product_category = sa.Enum(name='product_category')
    # product_category.drop(op.get_bind(), checkfirst=True)
    # ### end Alembic commands ###

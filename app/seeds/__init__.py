from flask.cli import AppGroup
from .users import seed_users, undo_users
from .products import seed_products, undo_products
from .reviews import seed_reviews, undo_reviews
from .carts import seed_carts, undo_carts
from .cart_items import seed_cart_items, undo_cart_items
from .order_histories import seed_order_histories, undo_order_histories
from .wishlists import seed_wishlists, undo_wishlists


from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_wishlists()
        undo_order_histories()
        undo_cart_items()
        undo_carts()
        undo_reviews()
        undo_products()
        undo_users()
    seed_users()
    seed_products()
    seed_reviews()
    seed_carts()
    seed_cart_items()
    seed_order_histories()
    seed_wishlists()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_wishlists()
    undo_order_histories()
    undo_cart_items()
    undo_carts()
    undo_reviews()
    undo_products()
    undo_users()
    # Add other undo functions here

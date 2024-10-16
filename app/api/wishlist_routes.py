from flask import Blueprint, jsonify, request, redirect, url_for
from flask_login import login_required, current_user
from app.models import db, Wishlist, Product


wishlist_routes = Blueprint('wishlist', __name__)


# Get all wishlists under the current user
# /api/wishlist/current
@wishlist_routes.route('/current')
@login_required
def fav_by_user():
    wishlists = Wishlist.query.filter_by(user_id=current_user.id).all()
    wishlist_list = [fav.to_dict() for fav in wishlists]

    product_id_list = [wishlist["product_id"] for wishlist in wishlist_list]
    products = Product.query.filter(Product.id.in_(product_id_list)).all()
    product_list = [product.to_dict() for product in products]

    return {'MyWishlists': wishlist_list, 'WishProd': product_list}, 200


# Add to wishlist
# /api/wishlist/new
@wishlist_routes.route('/new', methods=['POST'])
@login_required
def add_fav():
    data = request.json
    product_id = data.get('product_id')
    # existing_fav = Wishlist.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    new_fav = Wishlist(user_id=current_user.id, product_id=product_id)
    if not new_fav:
        return {'message': 'Already added to wishlist'}, 400
    db.session.add(new_fav)
    db.session.commit()
    return {'message': 'Added to wishlist'}, 201


# Delete a wishlist
# /api/wishlist/<int:id>/delete
@wishlist_routes.route('/<int:id>/delete', methods=['DELETE'])
@login_required
def remove_fav(id):
    wishlist = Wishlist.query.get(id)
    if not wishlist:
        return {'message': 'Wishlist item is not found'}, 404
    if wishlist.user_id != current_user.id:
        return redirect(url_for('auth.unauthorized'))
    db.session.delete(wishlist)
    db.session.commit()
    return {'message': 'Successfully Deleted'}, 200

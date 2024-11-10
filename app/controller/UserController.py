from flask import Blueprint

user = Blueprint('user', __name__)

@user.route('/users', methods=['GET'])
def get_users():
    return "hello user"

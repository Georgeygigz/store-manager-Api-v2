#app/api/v1/utils/authorization

from flask_jwt_extended import get_jwt_identity
from functools import wraps

from app.api.v2.models.store_model import Users

users =Users().get_all_users()

def admin_required(func):
    """ Admin Rights."""
    @wraps(func)
    def wrapper_function(*args, **kwargs):
        try:
            cur_user=[user for user in users if user['email']==get_jwt_identity()]
            user_role=cur_user[0]['role']
            if user_role != 'Admin':
                return {'message': 'This activity can be completed by Admin only'}, 403
            return func(*args, **kwargs)
        except Exception as e:
            return {"message":e}
    return wrapper_function


def store_attendant_required(func):
    """Store attedant rights."""
    @wraps(func)
    def wrapper_function(*args, **kwargs):
        cur_user=[user for user in users if user['email']==get_jwt_identity()]
        user_role=cur_user[0]['role']
        if user_role != 'attedant':
            return {'message': 'This activity can be completed by Store Attedant only'}, 403
        return func(*args, **kwargs)
    return wrapper_function
    
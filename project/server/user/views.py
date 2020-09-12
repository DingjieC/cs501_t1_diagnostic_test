# project/server/auth/views.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

user_blueprint = Blueprint('user', __name__)

class RegisterAPI(MethodView):
    """
    User Registration Resource
    """

    def get(self):
        user = db.session.query(User).all()
        ls=[]
        for x in user:
            e = x.email
            ls.append(e)
        return  jsonify({'user': ls}) ,201
        #user_ind = db.session.query(User).all()

        #print(user)
    	#responseObject = {
    	#	's': 'success',
        #    'user': user.email
        #}
    	#return make_response(jsonify(responseObject)), 201



# define the API resources
registration_view = RegisterAPI.as_view('register_api')

# add Rules for API Endpoints
user_blueprint.add_url_rule(
    '/user/index',
    view_func=registration_view,
    methods=['GET']
)


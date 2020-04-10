from flask import Blueprint
from ..views.dummy2 import *

blueprint = Blueprint('blueprint', __name__,
                      template_folder='views')


blueprint.add_url_rule("/",
                       endpoint='home',
                       view_func=home,
                       methods=['GET'])

blueprint.add_url_rule("/api/books/all",
                       endpoint='api_all',
                       view_func=api_all,
                       methods=['GET'])

blueprint.add_url_rule("/api/books",
                       endpoint='api_id',
                       view_func=api_id,
                       methods=['GET'])

blueprint.add_url_rule("/api/books/new",
                       endpoint='book_form',
                       view_func=book_form,
                       methods=['GET', 'POST'])

blueprint.add_url_rule("/api/books/id/<int:x>",
                       endpoint='api_lookup',
                       view_func=api_lookup,
                       methods=['GET', 'PUT', 'DELETE'])

blueprint.add_url_rule("/api/books/recover/<int:x>",
                       endpoint='recover_book',
                       view_func=api_recover,
                       methods=['PUT'])

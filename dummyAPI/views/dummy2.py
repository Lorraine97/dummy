from flask import jsonify, request
from ..models import dummy_db


# home
# @app.route('/', methods=['GET'])
def home():
    return "<h1>Running dummy api</h1><p>Hello This is Xinru!</p>"


# return all books
# @app.route('/api/books/all', methods=['GET'])
def api_all():
    return jsonify(dummy_db.all_books())


# optional param
# @app.route('/api/books', methods=['GET'])
def api_id():
    if len(dummy_db.all_books()) == 0:
        return "Your bookshelf is empty. Please put some books first"
    if 'id' in request.args:
        book_id = int(request.args['id'])
    else:
        return "Error: Need to specify an id to start search."

    result = dummy_db.id_query(book_id)

    return jsonify(result)


# add new book
# @app.route('/api/books/new', methods=['GET', 'POST'])
def book_form():

    # if defined in the route
    if request.args:
        book_id = request.args.get('id')
        book_title = request.args.get('title')
        dummy_db.new_book(book_id, book_title)
        return '''<h1>New book {} has title "{}" </h1>'''.format(book_id, book_title.title())

    # if not defined in the route, ask for the new book info
    else:
        if request.method == 'POST':  # this block is only entered when the form is submitted
            book_id = request.form.get('id')
            book_title = request.form.get('title')
            dummy_db.new_book(book_id, book_title)

            return '''<h1>Book ID: {}</h1>
                    <h1>Book Title: {}</h1>'''.format(book_id, book_title.title())

        return '''<form method="POST">
                    Book ID: <input type="text" name="id"><br>
                    Book Title: <input type="text" name="title"><br>
                    <input type="submit" value="Submit"><br>
                </form>'''


# positional argument x
# @app.route('/api/books/id/<int:x>', methods=['GET', 'PUT', 'DELETE'])
def api_lookup(x):
    num = int(x)
    if request.method == 'GET':
        find = dummy_db.id_query(num)
        return jsonify(find)
    elif request.method == 'PUT':
        if request.args:
            title = request.args.get('title')
            return dummy_db.update_book(num, title)
        else:
            # @TODO
            return 'Please input a title to update'
    elif request.method == 'DELETE':
        return dummy_db.delete_book(x)
    else:
        return 'You have selected book #:{}'.format(x)


# positional argument x
# @app.route('/api/books/recover/<int:x>', methods=['POST'])
def api_recover(x):
    num = int(x)
    return dummy_db.recover_book(num)

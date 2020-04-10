import datetime
from sqlalchemy import exc
from . import db_create as db


class DummyDB(db):
    __tablename__ = "dummydb"

    bid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    timestamp = db.Column(db.DateTime,
                          default=datetime.datetime.utcnow(),
                          onupdate=datetime.datetime.utcnow())
    active = db.Column(db.Boolean, default=True)  # for soft delete


def id_query(id_x):
    try:
        bidquery = db.session.query(DummyDB.bid, DummyDB.title, DummyDB.timestamp, DummyDB.edited). \
            filter(DummyDB.bid == id_x). \
            filter(DummyDB.active)
        return bidquery.all()

    except exc.SQLAlchemyError as e:
        return "There is an error: '%s'" % str(e)


def new_book(book_id, book_title):
    insertion = DummyDB.insert().values(bid=book_id, title=book_title)
    db.session.add(insertion)
    db.session.commit()


def delete_book(book_id):
    try:
        db.session.query(DummyDB). \
            filter(DummyDB.bid == book_id). \
            filter(DummyDB.active). \
            update(DummyDB.active, False)
        db.session.commit()
        return 'Successfully deleted book {}'.format(book_id)
    except exc.SQLAlchemyError:
        # db.session.rollback()
        return 'Book {} not found, cannot delete'.format(book_id)


def update_book(book_id, book_title):
    try:
        db.session.query(DummyDB). \
            filter(DummyDB.bid == book_id). \
            update(DummyDB.title, book_title). \
            update(DummyDB.timestamp, datetime.datetime.utcnow())
        db.session.commit()
        return 'Successfully updated book {} to title: {}'.format(book_id, book_title)
    except exc.SQLAlchemyError:
        # db.session.rollback()
        return 'Book {} not found, cannot update'.format(book_id)


def recover_book(book_id):
    try:
        if id_query(book_id) == exc.SQLAlchemyError:
            return f'Cannot find the book. Please check your book id {book_id}'
        else:
            db.session.query(DummyDB). \
                filter(not DummyDB.active). \
                update(DummyDB.active, True)
            db.session.commit()
            return 'Successfully recovered book {}'.format(book_id)
    except exc.SQLAlchemyError:
        # db.session.rollback()
        return 'Book {} cannot be recovered. Please check if it is active'.format(book_id)


def all_books():
    try:
        bidquery = db.session.query(DummyDB.bid, DummyDB.title, DummyDB.timestamp, DummyDB.edited)
        return bidquery.all()
    except exc.SQLAlchemyError as e:
        return "There is an error: '%s'" % str(e)

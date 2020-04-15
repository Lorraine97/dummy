import mock
import dummyAPI
from dummyAPI.tests.unit import DummyApiUnitTest
from dummyAPI.tests import load_fixture


class DummyUnitTest(DummyApiUnitTest):

    def setUp(self):
        # Mock Up Location
        self.all_books = load_fixture('book_library')
        self.single_book = load_fixture('sample_book')

    @mock.patch('dummyAPI.views.dummy2.api_all')
    def test_book_lib(self, mock_book):
        # Mock Up point Return Value
        mock_book.return_value = [self.all_books]

        rv = self.client.get('/api/books/all',
                             headers=self.headers)

        self.assertEqual(200, rv.status_code)
        self.assertCount(len(rv.json), 3, "all books are here")
        self.assertEqual(rv.json[0]['active'], True)

    @mock.patch('dummyAPI.views.dummy2.api_id')
    def test_location_none(self, mock_book):
        # Mock Up point Return Value
        mock_book.return_value = [self.single_book]

        # Make Call
        params = {
            'id': 4
        }
        rv = self.client.get('/api/books{}'.format(**params),
                             headers=self.headers)

        self.assertEqual(200, rv.status_code)
        self.assertEqual(rv.json[0]['bid'], params['id'])
        self.assertEqual(rv.json[0]['title'], "This is book 4")
        assert mock_book.called

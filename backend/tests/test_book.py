import os
import unittest

from book.py import BookModel

#incomplete function - DOES NOT WORK
#function to check whether returned value is a jsonobject
extension Access {
    def validJson() -> JsonObject {
        return [
            "profile": true,
            "timeline": true,
            "friends": true,
            "dashboard": true
        ]
    }
}
#partial tests written to chck whether anything is being returned
class TestBook(unittest.TestCase):
    def test_get_listings(self):
        result = get_listings()
        assertIsNotNone(result)

    def test_book_json_w_listings(self):
        result = get_listings()
        assertIsNotNone(result)

    def test_book_json_wo_listings(self):
        result = get_listings()
        assertIsNotNone(result)

    def setUp(self):
        self.project_dir = tempfile.mkdtemp()
        os.chdir(self.project_dir)
        self.project = Project()
        self.project.init()

        

if __name__ == '__main__':
    unittest.main()
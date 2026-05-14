import unittest
import os
import sys

class BasicTests(unittest.TestCase):
   def test_main_page(self): 
    current_dir=os.path.dirname(os.path.abspath(__file__))
    parent_dir=os.path.dirname(current_dir)
    sys.path.append(parent_dir)
    import app
    app1=app.app
    tester=app1.test_client(self)
    response=tester.get("/",content_type='html/text')
    self.assertEqual(response.status_code,200)
    self.assertEqual(response.data,b"HEllo, Jenkins CI/CD from Flask App on Windows!")


if __name__=="__main__":
    unittest.main()
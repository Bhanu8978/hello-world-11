
 # test_aoo.py
 import unittest
 from app import hello_world
 

 class TestApp(unittest.TestCase):
    def test_hello_world(self):
        self.asserEqual(hello_world(), "hello, world!")


        if_name_=='_main_':
            unittest.main()
            
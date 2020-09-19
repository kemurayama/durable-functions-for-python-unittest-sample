#coding:utf-8

from unittest import main
from unittest import TestCase

from Hello import main

class HelloTestCase(TestCase):
    
    def test_hello_str(self):
        name = 'Test'
        result = main(name)
        self.assertEqual(f'Hello {name}!',result)

if __name__ == "__main__":
    main()
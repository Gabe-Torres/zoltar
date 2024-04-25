import unittest
from selenium import webdriver

class TestApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_home_page(self):
        self.driver.get("http://127.0.0.1:5000")
        print(self.driver.title)

        body = driver.find_element_by_tag_name('body')
        self.assertIn('Hello, World!', body.text)

if __name__ == '__main__':
    unittest.main()
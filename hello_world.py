import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path=r'.\Programs\chromedriver.exe')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get("https://www.platzi.com")

    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.com')

    @classmethod  
    def tearDown(cls) -> None:
        cls.driver.quit()

    


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello-world-report'))

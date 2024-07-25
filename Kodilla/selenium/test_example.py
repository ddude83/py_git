from selenium import webdriver

def test_example():
    driver = webdriver.Chrome()
    driver.get('http://www.example.com')
    assert driver.title == 'Example Domain'
def test_example(selenium):
    selenium.get('http://www.example.com')
    assert selenium.title == 'Example Domain'
import pytest

# ...
# importy dla User (w tym przykładzie z django.contrib.auth.models)
# ...

@pytest.fixture
def user():
    user = User.objects.create(username='testuser')
    yield user
    user.delete()

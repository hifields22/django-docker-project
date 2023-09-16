# from django.test import TestCase

# Create your tests here.

# Django imports
from django.contrib.auth.models import User
from django.urls import reverse

# pytest imports
import pytest

# Local imports (from your app or project)
# from .forms import UserCreationForm

# Then, the test functions come next...

def test_register_view_uses_correct_template(client):
    response = client.get('/path_to_register/')
    assert response.status_code == 200
    assert 'registration/register.html' in [template.name for template in response.templates]

def test_register_view_displays_form(client):
    response = client.get('/path_to_register/')
    assert b'form' in response.content

def test_successful_user_registration(client):
    users_before = User.objects.count()
    response = client.post('/path_to_register/', data={
        'username': 'testuser',
        'password1': 'complex_password',
        'password2': 'complex_password'
    })
    assert User.objects.count() == users_before + 1
    assert response.status_code == 302
    assert response.url == reverse('login')

def test_failed_user_registration_due_to_password_mismatch(client):
    users_before = User.objects.count()
    response = client.post('/path_to_register/', data={
        'username': 'testuser',
        'password1': 'password_one',
        'password2': 'password_two'
    })
    assert User.objects.count() == users_before
    assert b'form' in response.content
    assert b'The two password fields didn&#39;t match.' in response.content

@pytest.fixture
def create_test_user():
    User.objects.create_user(username='testuser', password='complex_password')

def test_failed_user_registration_due_to_existing_username(client, create_test_user):
    users_before = User.objects.count()
    response = client.post('/path_to_register/', data={
        'username': 'testuser',
        'password1': 'another_password',
        'password2': 'another_password'
    })
    assert User.objects.count() == users_before
    assert b'form' in response.content
    assert b'A user with that username already exists.' in response.content

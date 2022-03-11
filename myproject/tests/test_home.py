from django.test import Client
from myproject.django_assertions import assert_contains

def test_status_code(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200

def test_tile(client: Client):
    resp = client.get('/')
    assert_contains(resp, '<title>PyPro!</title>')


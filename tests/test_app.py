import app
import pytest


@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    client = app.app.test_client()
    yield client


def test_index(client):
    response = client.get('/')
    assert b"Tasks" in response.data


def test_add_task(client):
    response = client.post('/add', data={'todo': 'Test Task'}, follow_redirects=True)
    assert b"Test Task" in response.data


def test_edit_task(client):
    response = client.get('/edit/0')
    assert b"Edit" in response.data


def test_edit_task_save(client):
    response = client.post('/edit/0', data={'todo': 'Updated Task'}, follow_redirects=True)
    assert b"Updated Task" in response.data


def test_check_task(client):
    response = client.get('/check/0', follow_redirects=True)
    assert b'style="text-decoration: line-through"' in response.data


def test_uncheck_task(client):
    response = client.get('/check/0', follow_redirects=True)
    assert b'style="text-decoration: line-through"' not in response.data


def test_delete_task(client):
    response = client.get('/delete/0', follow_redirects=True)
    assert b"Updated Task" not in response.data

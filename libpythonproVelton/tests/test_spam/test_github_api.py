from unittest.mock import Mock

import pytest

from libpythonproVelton import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/13990365?v=4s'
    resp_mock.json.return_value = {
        'login': 'aurohm', 'id': 13990365, 'node_id': 'MDQ6VXNlcjEzOTkwMzY1',
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpythonproVelton.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('aurohm')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('aurohm')
    assert 'https://avatars.githubusercontent.com/u/13990365?v=4' == url

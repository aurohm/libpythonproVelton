from unittest.mock import Mock

import pytest

from libpythonproVelton.spam.main import EnviadorDeSpam
from libpythonproVelton.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Velton', email='veltonmoura@gmail.com'),
            Usuario(nome='Jessie', email='jerssiers@gmail.com')
        ],
        [
            Usuario(nome='Velton', email='veltonmoura@gmail.com')
        ]
    ]
)
def test_qtde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'veltonmoura@gmail.com',
        'Curso Python Pro',
        'Confira os módulos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Velton', email='veltonmoura@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'jerssiers@gmail.com',
        'Curso Python Pro',
        'Confira os módulos'
    )
    enviador.enviar.assert_called_once_with(
        'jerssiers@gmail.com',
        'veltonmoura@gmail.com',
        'Curso Python Pro',
        'Confira os módulos'
    )

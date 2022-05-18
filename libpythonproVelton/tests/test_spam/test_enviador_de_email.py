import pytest

from libpythonproVelton.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_eviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'veltonmoura@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'renzo@python.pro.com.br',
        'Curso Python Pro',
        'TDD e Baby Steps - Turma Moacir Moda'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['', 'veltonmoura']
)
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):  # gerenciador de contexto
        enviador.enviar(
            destinatario,
            'renzo@python.pro.com.br',
            'Curso Python Pro',
            'TDD e Baby Steps - Turma Moacir Moda'
        )

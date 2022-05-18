from libpythonproVelton.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Velton', email='veltonmoura@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='Velton', email='veltonmoura@gmail.com'),
        Usuario(nome='Jessie', email='veltonmoura@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

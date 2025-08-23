import pytest
from juros_composto import calcular_juros_compostos

# passando os parametros
@pytest.mark.parametrize("capital, juros, tempo, situacao_esperada",
                         [
                             (1000, 20, 1, (200, 1200)),
                             (1000, 15.5, 1, (155, 1155))
                         ])


def test_calcular_juros_parametrizados(capital, juros, tempo, situacao_esperada):
    resultado = calcular_juros_compostos(capital, juros, tempo)

    assert resultado == situacao_esperada

# testando os erros

# vendo se é numero negativo
def test_capital_negativa():
    # Definindo a entrada
    capital = -1000.00
    juros = 40
    tempo = 2

    # Executando a função e esperando erro
    with pytest.raises(ValueError, match="O capital investido não pode ser negativo."):
        calcular_juros_compostos(capital, juros, tempo) 

# vendo se é numero negativo
def test_juros_negativo():
    # Definindo a entrada
    capital = 1000.00
    juros = -40
    tempo = 2

    # Executando a função e esperando erro
    with pytest.raises(ValueError, match="A taxa de juros não pode ser negativa."):
        calcular_juros_compostos(capital, juros, tempo) 

# vendo se é numero negativo
def test_tempo_negativo():
    # Definindo a entrada
    capital = 1000.00
    juros = 40
    tempo = -2

    # Executando a função e esperando erro
    with pytest.raises(ValueError, match="O tempo não pode ser negativo."):
        calcular_juros_compostos(capital, juros, tempo) 

# vendo se o capital é uma str
def test_string_capital():
    # Definindo a entrada
    capital = "ola"
    juros = 40
    tempo = 2

    # Executando a função e esperando erro
    with pytest.raises(TypeError, match="O capital investido deve ser um número (int ou float)."):
        calcular_juros_compostos(capital, juros, tempo) 

# vendo se o juros é uma str
def test_string_juros():
    # Definindo a entrada
    capital = 1000
    juros = "ola"
    tempo = 2

    # Executando a função e esperando erro
    with pytest.raises(TypeError, match="A taxa de juros deve ser um número (int ou float)."):
        calcular_juros_compostos(capital, juros, tempo) 

# vendo se o tempo é uma str
def test_string_tempo():
    # Definindo a entrada
    capital = 1000
    juros = 40
    tempo = "ola"

    # Executando a função e esperando erro
    with pytest.raises(TypeError, match="O tempo deve ser um número (int ou float)."):
        calcular_juros_compostos(capital, juros, tempo) 

# vendo se o capital é 0
def test_zero_capital():
    # Definindo a entrada
    capital = 0
    juros = 40
    tempo = 2

    # Executando a função e esperando erro
    with pytest.raises(ValueError, match="O capital deve ser um número maior que 0"):
        calcular_juros_compostos(capital, juros, tempo) 

# vendo se o juros é 0
def test_zero_juros():
    # Definindo a entrada
    capital = 1000
    juros = 0
    tempo = 2

    # Executando a função e esperando erro
    with pytest.raises(ValueError, match="O juros deve ser um número maior que 0"):
        calcular_juros_compostos(capital, juros, tempo) 

# vendo se o tempo é 0
def test_zero_tempo():
    # Definindo a entrada
    capital = 1000
    juros = 40
    tempo = 0

    # Executando a função e esperando erro
    with pytest.raises(ValueError, match="O tempo deve ser um número maior que 0"):
        calcular_juros_compostos(capital, juros, tempo) 

# vendo se foi enviado menos de 3 valores
def test_menos_de_tres_valores():
    # Definindo a entrada
    capital = 1000
    juros = 40

    # Executando a função e esperando erro
    with pytest.raises(TypeError, match="Não é permitido enviar menos que 3 valores"):
        calcular_juros_compostos(capital, juros)
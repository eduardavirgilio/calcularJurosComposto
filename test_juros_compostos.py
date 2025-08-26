import pytest
from juros_composto import calcular_juros_compostos

# passando os parametros
@pytest.mark.parametrize("capital, juros, tempo, situacao_esperada",
                         [
                             (1000, 20, 1, (200, 1200)), #teste normal
                             (1000, 15.5, 1, (155, 1155)), #teste com juros decimal
                             (5000, 2.0, 1, (100, 5100)), #teste com taxa pequena
                             (0, 2.0, 1, (0, 0)), #teste capital como 0
                             (2000, 0, 1, (0 ,2000)), #teste juros como 0
                             (2000, 5.0, 0, (0, 2000)) #teste tempo como 0    
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
    with pytest.raises(TypeError, match=r"O capital investido deve ser um número \(int ou float\)."):
        calcular_juros_compostos(capital, juros, tempo) 

# vendo se o juros é uma str
def test_string_juros():
    # Definindo a entrada
    capital = 1000
    juros = "ola"
    tempo = 2

    # Executando a função e esperando erro
    with pytest.raises(TypeError, match=r"A taxa de juros deve ser um número \(int ou float\)."):
        calcular_juros_compostos(capital, juros, tempo) 

# vendo se o tempo é uma str
def test_string_tempo():
    # Definindo a entrada
    capital = 1000
    juros = 40
    tempo = "ola"

    # Executando a função e esperando erro
    with pytest.raises(TypeError, match=r"O tempo deve ser um número \(int ou float\)."):
        calcular_juros_compostos(capital, juros, tempo) 

# vendo se foi enviado menos de 3 valores
def test_menos_de_tres_valores_tempo():
    # Definindo a entrada
    capital = 3500
    juros = 40

    # Executando a função e esperando erro
    with pytest.raises(TypeError, match="Não é permitido enviar menos que 3 valores"):
        calcular_juros_compostos(capital, juros)

# vendo se foi enviado menos de 3 valores
def test_menos_de_tres_valores_capital():
    # Definindo a entrada
    juros = 40
    tempo = 12

    # Executando a função e esperando erro
    with pytest.raises(TypeError, match="Não é permitido enviar menos que 3 valores"):
        calcular_juros_compostos(juros, tempo)

# vendo se foi enviado menos de 3 valores
def test_menos_de_tres_valores_juros():
    # Definindo a entrada
    capital = 1000
    tempo = 12

    # Executando a função e esperando erro
    with pytest.raises(TypeError, match="Não é permitido enviar menos que 3 valores"):
        calcular_juros_compostos(capital, tempo)
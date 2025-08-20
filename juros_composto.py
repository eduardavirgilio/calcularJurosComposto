def calcular_juros_compostos(capital_investido:float, taxa_juros:float, tempo:int) -> tuple:
    """
    Calcula os juros compostos a partir de um capital inicial, uma taxa de juros e um período de tempo.

    A fórmula usada para calcular os juros compostos é:
        M = P * (1 + r/100)^t
    Onde:
        M = Montante final (capital + juros)
        P = Capital inicial
        r = Taxa de juros (em porcentagem)
        t = Tempo (em períodos)

    O valor dos juros é calculado como a diferença entre o montante final e o capital inicial:
        Juros = M - P

    Parâmetros:
    -----------
    capital_investido : float
        O valor do capital inicial (P). Deve ser um número não negativo.
    
    taxa_juros : float
        A taxa de juros anual (r), expressa em porcentagem (ex: 5 para 5%). Deve ser um número não negativo.

    tempo : float
        O tempo de investimento (t), em anos ou períodos definidos. Deve ser um número não negativo.

    Retorno:
    --------
    tuple
        Retorna uma tupla com dois valores:
        1. O valor dos **juros** calculados.
        2. O **montante final** (capital + juros).
    """

    # Validação do capital investido
    if not isinstance(capital_investido, (int, float)):
        raise ValueError("O capital investido deve ser um número (int ou float).")
    if capital_investido < 0:
        raise ValueError("O capital investido não pode ser negativo.")

    # Validação da taxa de juros
    if not isinstance(taxa_juros, (int, float)):
        raise ValueError("A taxa de juros deve ser um número (int ou float).")
    if taxa_juros < 0:
        raise ValueError("A taxa de juros não pode ser negativa.")

    # Validação do tempo
    if not isinstance(tempo, (int, float)):
        raise ValueError("O tempo deve ser um número (int ou float).")
    if tempo < 0:
        raise ValueError("O tempo não pode ser negativo.")

    # Cálculo dos juros compostos
    montante = capital_investido * (1 + taxa_juros / 100) ** tempo
    juros = montante - capital_investido
    
    return juros, montante

"""
Testes para o modulo calculadora.
"""

import pytest
from calculadora import soma, subtracao, multiplicacao, divisao, percentual, eh_par

# ----------------------------------------------------------------
# soma
# ----------------------------------------------------------------


def test_soma_inteiros_positivos():
    assert soma(3, 4) == 7


def test_soma_com_numero_negativo():
    assert soma(-1, 5) == 4


def test_soma_dois_negativos():
    assert soma(-2, -3) == -5


# ----------------------------------------------------------------
# subtracao
# ----------------------------------------------------------------


def test_subtracao_resultado_positivo():
    assert subtracao(10, 3) == 7


def test_subtracao_resultado_negativo():
    assert subtracao(2, 8) == -6


# ----------------------------------------------------------------
# multiplicacao
# ----------------------------------------------------------------


def test_multiplicacao_inteiros():
    assert multiplicacao(4, 5) == 20


def test_multiplicacao_por_zero():
    assert multiplicacao(7, 0) == 0


def test_multiplicacao_negativos():
    assert multiplicacao(-3, -4) == 12


# ----------------------------------------------------------------
# divisao
# ----------------------------------------------------------------


def test_divisao_resultado_exato():
    assert divisao(10, 2) == 5.0


def test_divisao_resultado_nao_inteiro():
    assert divisao(7, 2) == 3.5


def test_divisao_por_zero_lanca_erro():
    with pytest.raises(ValueError):
        divisao(10, 0)


# ----------------------------------------------------------------
# percentual
# ----------------------------------------------------------------


def test_percentual_valor_correto():
    assert percentual(200, 10) == 20.0


def test_percentual_cem_por_cento():
    assert percentual(50, 100) == 50.0


def test_percentual_negativo_lanca_erro():
    with pytest.raises(ValueError):
        percentual(100, -5)


# ----------------------------------------------------------------
# eh_par
# ----------------------------------------------------------------


def test_eh_par_numero_par():
    assert eh_par(4) is True


def test_eh_par_numero_impar():
    assert eh_par(7) is False


def test_eh_par_zero_e_par():
    assert eh_par(0) is True

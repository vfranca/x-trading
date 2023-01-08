# x-trading
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
from click.testing import CliRunner
from x_trading.x import x


run = CliRunner()


def test_exibe_a_versao():
    res = run.invoke(x, ["--version"])
    assert res.output == "x-trading 0.3.1\n"


def test_calcula_variacoes_percentuais():
    res = run.invoke(x, ["vp", "100.00"])
    assert res.output == "102.00\n101.00\n100.00\n99.00\n98.00\n"


def test_calcula_o_ponto_pivo():
    res = run.invoke(x, ["pp", "200.00", "100.00", "150.00"])
    assert res.output == "250.0\n200.0\n150.0\n100.0\n50.0\n"

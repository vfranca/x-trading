from click.testing import CliRunner
from x_trading.x import x


runner = CliRunner()


def test_pp():
    result = runner.invoke(x, ["pp"])
    assert result.exit_code == 0
    assert result.output == "ponto pivo\n"


def test_vp():
    result = runner.invoke(x, ["vp"])
    assert result.exit_code == 0
    assert result.output == "variacao percentual\n"

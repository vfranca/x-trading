from click.testing import CliRunner
from x_trading.pp import pp


def test_pp():
    runner = CliRunner()
    result = runner.invoke(pp)
    assert result.exit_code == 0
    assert result.output == "ponto pivo\n"

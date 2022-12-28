from click.testing import CliRunner
from x_trading.vp import vp


def test_vp():
    runner = CliRunner()
    result = runner.invoke(vp)
    assert result.exit_code == 0
    assert result.output == "variacao percentual\n"

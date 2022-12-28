import click

# Importa os comandos
from x_trading.pp import pp
from x_trading.vp import vp


# Cria o grupo de comandos x
@click.group()
def x():
    pass


x.add_command(pp)
x.add_command(vp)


if __name__ == "__main__":
    x()

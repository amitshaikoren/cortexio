import click
from . import run_gui_server


@click.group()
def cli():
    pass

@cli.command()
@click.option('-h', '--host',      default='0.0.0.0'  , help="server host")
@click.option('-p', '--port',      default='9000'       , help="server port")
@click.option('-H', '--api_host',  default='127.0.0.1'  , help="API Host")
@click.option('-P', '--api_port',  default='7000'       , help="API port")
def run_server(host,port, api_host, api_port):
    formatted_api_address = f"http://{api_host}:{api_port}";
    try:
        run_gui_server(host, port, formatted_api_address)
    except Exception as error:
        print(f'GUI ERROR: {error}')
        return 1

if __name__ == '__main__':
    cli(prog_name='gui')

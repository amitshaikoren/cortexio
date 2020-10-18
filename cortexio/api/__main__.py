import click
from cortexio.api.api import run_api_server


@click.group()
def cli():
    pass


@cli.command()
@click.option('-h', '--host', default='127.0.0.1')
@click.option('-p', '--port', default='7000')
@click.option('-d', '--database', default='mongodb://127.0.0.1:27017')
def run_server(host, port, database):
    try:
        run_api_server(host, port, database)
    except Exception as error:
        print(f'ERROR: {error}')


if __name__ == '__main__':
    cli(prog_name='api')

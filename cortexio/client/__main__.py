from cortexio.client import client
import click
from cortexio import PROJECT_NAME

@click.group()
def cli():
    pass


@cli.command()
@click.option('-h', '--host', default='127.0.0.1',      help="Server host")
@click.option('-p', '--port', default=8080,             help="Server port")
@click.argument('path')
def upload_sample(host, port, path):
    try:
        client.upload_sample(host, int(port), path)
    except Exception as error:
        print(f'ERROR: {error}')
    pass


if __name__ == '__main__':
    cli(prog_name=PROJECT_NAME)


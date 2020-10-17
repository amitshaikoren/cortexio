from cortexio.server import server
import click
from cortexio import PROJECT_NAME

@click.group()
def cli():
    pass


@cli.command()
@click.option('-h', '--host', default='0.0.0.0',      help="Server host")
@click.option('-p', '--port', default=8080,             help="Server port")
@click.argument('mq_url',   help="Path to message queue")
def run_server(host, port, mq_url):
    try:
        server.run_server(host, port, mq_url=mq_url)
    except KeyboardInterrupt:
        print('Server terminated by user (KeyboardInterrupt)')
    pass


if __name__ == '__main__':
    cli(prog_name=PROJECT_NAME)

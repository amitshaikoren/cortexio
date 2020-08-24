from cortexio.parsers import parser_manager
import click
from cortexio.utils import FileSystemManager as FSM
from cortexio import PROJECT_NAME, DEFAULT_MESSAGEQ_URL


@click.group()
def cli():
    pass


@cli.command()
@click.argument('parser_name', help="Parser to parse with")
@click.argument('raw_data_path', help="Path to raw data to be parsed")
def parse(parser_name, raw_data_path):
    try:
        raw_data = FSM.load(raw_data_path)
        print(parser_manager.parse(parser_name, raw_data))
    except Exception as error:
        print(error)


@cli.command()
@click.argument('parser_name', help="Parser to run")
@click.argument('mq_url', help="URL of dedicated message queue")
def run_parser(parser_name, mq_url):
    try:
        parser_manager.run_parsers(parser_name, mq_url)
    except Exception as error:
        print(error)


@cli.command()
def run_parsers():
    parser_manager.run_parsers(DEFAULT_MESSAGEQ_URL)


if __name__ == '__main__':
    cli(prog_name=PROJECT_NAME)


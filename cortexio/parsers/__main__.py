from cortexio.parsers import parse, run_parsers, consume_publish_with_parser
import click
from cortexio.utils import FileSystemManager as FSM
from cortexio import DEFAULT_MESSAGEQ_URL


@click.group()
def cli():
    pass


@cli.command()
@click.argument('parser_name')
@click.argument('raw_data_path')
def parse(parser_name, raw_data_path):
    try:
        raw_data = FSM.load(raw_data_path)
        print(parse(parser_name, raw_data))
    except Exception as error:
        print(error)


@cli.command()
@click.argument('parser_name')
@click.argument('mq_url')
def run_parser(parser_name, mq_url):
    try:
        consume_publish_with_parser(parser_name, mq_url)
    except Exception as error:
        print(error)


@cli.command()
def run_parsers():
    run_parsers(DEFAULT_MESSAGEQ_URL)


if __name__ == '__main__':
    cli(prog_name="parsers")


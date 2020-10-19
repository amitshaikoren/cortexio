import cortexio.parsers as parsers
import click
from cortexio.utils import FileSystemManager as FSM
from cortexio import DEFAULT_MESSAGEQ_URL, PROJECT_NAME


@click.group()
def cli():
    pass


@cli.command()
@click.argument('parser_name')
@click.argument('raw_data_path')
def parse(parser_name, raw_data_path):
    try:
        raw_data = FSM.load(raw_data_path)
        print(parsers.parse(parser_name, raw_data))
    except Exception as error:
        print(error)


@cli.command()
@click.argument('parser_name')
@click.argument('mq_url')
def run_parser(parser_name, mq_url):
    try:
        parsers.consume_publish_with_parser(parser_name, mq_url)
    except Exception as error:
        print(error)


@cli.command()
@click.option('--mq_url', default=DEFAULT_MESSAGEQ_URL)
def run_parsers(mq_url):
    parsers.run_parsers(mq_url)


if __name__ == '__main__':
    cli(prog_name="parsers")


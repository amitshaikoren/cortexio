from cortexio.saver import saver
import click
from cortexio.utils import FileSystemManager as FSM
from cortexio import PROJECT_NAME, DEFAULT_DATABASE_URL


@click.group()
def cli():
    pass


@cli.command()
@click.option('-d', '--database', default=DEFAULT_DATABASE_URL, help="Parser to parse with")
@click.argument('raw_data_path')
def save(database_url, topic, raw_data_path):
    try:
        raw_data = FSM.load(raw_data_path)
        saver.saver(database_url).save(topic, raw_data)
    except Exception as error:
        print(error)

@cli.command()
@click.option('-d', '--database', default=DEFAULT_DATABASE_URL, help="Parser to parse with")
@click.argument('raw_data_path')
def run_saver(database_url, topic):
    try:
        saver.saver(database_url).run_saver(topic)
    except Exception as error:
        print(error)


if __name__ == '__main__':
    cli(prog_name=PROJECT_NAME)

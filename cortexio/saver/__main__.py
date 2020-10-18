from cortexio.saver import Saver
import click
from cortexio import DEFAULT_DATABASE_URL


@click.group()
def cli():
    pass


@cli.command()
@click.option('-d', '--database', default=DEFAULT_DATABASE_URL)
@click.argument('topic')
@click.argument('input_path')
def save(database, topic, input_path):
    saver = Saver(database)
    with open(input_path, 'r') as f:
        saver.save(topic, f.read())


@cli.command()
@click.argument('db_url')
@click.argument('mq_url')
def run_saver(db_url, mq_url):
    saver = Saver(db_url)
    saver.run_savers(mq_url)


if __name__ == '__main__':
    cli(prog_name='saver')
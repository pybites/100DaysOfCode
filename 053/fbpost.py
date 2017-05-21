import os
import sys

import click
import facebook

token = os.environ.get('FB_POSTCLI_TOKEN') or sys.exit('Please set FB_POSTCLI_PW env var')
graph = facebook.GraphAPI(access_token=token, version='2.7')  # 2.9 (docs) facebook.GraphAPIError ?!

PYBITES = '1305028816183522'  # pybites group id
CONNECTION_NAME = 'feed'


@click.command()
@click.option('--connection', default=PYBITES, help='Where to post to (me, group name/id)')  # TODO: post to page
@click.option('--message', help='The message to post. For now embed any links in here')
def fbpost(connection, message):
    if message is None:
        raise ValueError('I need to know what message to post please')

    graph.put_object(
        parent_object=connection,
        connection_name=CONNECTION_NAME,
        message=message)   # TODO: allow link kwarg


if __name__ == '__main__':
    fbpost()

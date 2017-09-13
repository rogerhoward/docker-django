#!/usr/bin/env python

from flask import Flask, Response, send_file, jsonify, abort, request, redirect
import os
import click
import simplejson as json
from pprint import pprint

app = Flask(__name__)


@app.route('/')
def home():
    return 'well hello'

#------------------------------------------------#
# System status endpoints                        #
#------------------------------------------------#


@app.route('/system/env')
def envvar_dump():
    return jsonify(os.environ())


#------------------------------------------------#
#  Command line options                          #
#------------------------------------------------#

@click.command()
@click.option('--workers', default=3, help='Number of workers to use.')
@click.option('--port', default=5000, help='Port to run the server on.')
@click.option('--flush/--no-flush', default=False, help='Whether to flush the cache on startup. Defaults to not flush.')
@click.option('--debug/--no-debug', default=True, help='Whether to run in debug mode. Defaults to debug enabled.')
def run(workers, port, flush, debug):
    app.run(processes=workers, host='0.0.0.0', port=port, debug=debug)


if __name__ == '__main__':
    run()

from hello import app
from hello.formater import get_formatted
from hello.formater import SUPPORTED, PLAIN
from flask import request


moje_imie = "Krzysiek"
msg = "Aplikacja testowa!"

@app.route('/')
def index():
    output = request.args.get('output')
    name = request.args.get('name')
    if not output:
        output = PLAIN
    if not name:
        name = moje_imie
    return get_formatted(msg, name, output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)

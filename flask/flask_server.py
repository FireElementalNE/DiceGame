# app.py
import argparse
import pprint
from flask import Flask, jsonify, request, render_template
from dice_sim_lib import play
app = Flask(__name__)

@app.route('/game', methods=['POST'])
def hello():
    if request.method == 'POST':
        text = play(request.form['n1'], request.form['n2'], int(request.form['rounds']))
        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint(text)
        return jsonify({'text':text})

    else:
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Flask Server')
	parser.add_argument('-p', '--port', help='Port', required=False, default=7777, type=int)
	parser.add_argument('-d', '--debug', help='debug mode', required=False, action='store_true')
	args = parser.parse_args()
	app.debug = args.debug
	app.run(host='0.0.0.0', port=args.port, threaded=True)
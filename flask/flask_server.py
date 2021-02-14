# app.py
import argparse
import pprint
from flask import Flask, jsonify, request, render_template
from dice_sim_lib import play
app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello():

    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.form['n1'])  # parse as JSON
        text = play(request.form['n1'], request.form['n2'], int(request.form['rounds']))
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(text)
        # print(text)
        return jsonify({'text':text})

    # GET request
    else:
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers

@app.route('/')
def index():
    # render_template("script.js")
    # look inside `templates` and serve `index.html`
    return render_template('index.html')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Flask Server')
	parser.add_argument('-p', '--port', help='Port', required=False, default=7777, type=int)
	parser.add_argument('-d', '--debug', help='debug mode', required=False, action='store_true')
	args = parser.parse_args()
	app.debug = args.debug
	app.run(host='0.0.0.0', port=args.port, threaded=True)
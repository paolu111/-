from flask import Flask


app = Flask(__name__)


@app.route('/index1')
def index():
      return 'running'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9808)
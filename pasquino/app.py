import flask

app = flask.Flask(__name__)


@app.route('/<square>')
def states(square):
    return flask.render_template('index.html', square=square)


@app.route('/')
def index():
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

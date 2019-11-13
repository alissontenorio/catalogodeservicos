from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main_content():
    return render_template('index.html', url_value=None)


@app.route('/telefonia')
def display_telefonia():
    return render_template('telefonia.html')


if __name__ == '__main__':
    app.run(debug=True)
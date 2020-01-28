from flask import render_template
import __init__
import forms

#app = Flask(__name__)
app = __init__.app
formulario = forms.LoginForm

@app.route('/')
def main_content():
    #form = LoginForm()
    return render_template('index.html', url_value=None, form=formulario())
    #return 'main'


@app.route('/telefonia')
def display_telefonia():
    #return ''
    return render_template('telefonia.html', form=formulario())


@app.route('/login', methods=['GET', 'POST'])
def login():
    return("Logado")



if __name__ == '__main__':
    app.run(debug=True)
    #app.config['SECRET_KEY'] = "teste"
    #app.config['SECRET_KEY'] = 'services@L'
    #login_manager = flask_login.LoginManager()
    #login_manager.init_app(app)

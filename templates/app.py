from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

app = Flask(__name__,template_folder = '/Users/shivopamtiwari/Documents/Git_repo/templates')
app.config['SECRET_KEY'] = 'secret_key_here'

class AddNumbersForm(FlaskForm):
    num1 = IntegerField('Number 1', validators=[DataRequired()])
    num2 = IntegerField('Number 2', validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = AddNumbersForm()
    if form.validate_on_submit():
        num1 = form.num1.data
        num2 = form.num2.data
        result = num1 + num2
        return render_template('result.html', result=result)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
from flask import render_template, request
from app import app
from .forms import Nutrition
from .api import process
from .format_results import nice

@app.route('/', methods=['GET', 'POST'])
def info():
    form = Nutrition()
    if request.method == 'POST':
        if form.validate_on_submit():
            food = request.form.get("food")
            amount = request.form.get("amount")
            unit = request.form.get("unit")
            try:
                from_api = process(food, amount, unit)
                potassium = from_api[0]
                sodium = from_api[1]
                potassium_raw = potassium[0]
                potassium_mg = potassium[1][:-13]
                sodium_raw = sodium[0]
                sodium_mg = sodium[1][:-13]
                potassium_nice = nice(potassium_raw, 'Potassium')
                sodium_nice = nice(sodium_raw, 'Sodium')
                return render_template('results.html', k=potassium_nice, k_mg=potassium_mg, na=sodium_nice, na_mg=sodium_mg)
            except IndexError:
                query = '{} {} of {}'.format(amount,unit,food)
                return render_template('wolfram_fail.html',\
                                       query=query)
        else:
            return render_template('form.html',form=form)
    elif request.method == 'GET':
        return render_template('form.html',form=form)
    
@app.errorhandler(500)
def internal(e):
    return render_template('error.html'), 500

@app.route('/test')
def test():
    return render_template('wolfram_fail.html')

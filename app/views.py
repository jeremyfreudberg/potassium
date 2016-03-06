from flask import render_template, request
from app import app
from .forms import Nutrition
from .api import process
from .format_results import nice
@app.route('/', methods=['GET', 'POST'])
def info():
    form = Nutrition()
    if request.method == 'POST':
        food = request.form.get("food")
        element = request.form.get("element")
        amount = request.form.get("amount")
        unit = request.form.get("unit")
        from_api = process(element, food, amount, unit)
        query_raw = from_api[0]
        mg = from_api[1]
        query = nice(query_raw, element)
        return render_template('results.html', query=query, mg=mg)
    elif request.method == 'GET':
        return render_template('form.html',form=form)

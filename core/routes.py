from flask import render_template, request
import datetime
from core import app
from core.models import db, Table
from core.convert import usd_rate

@app.route('/')
def index(dollar):
    dollarr = Table.query.get(dollar)
    ruble = float(dollarr) * usd_rate
    page = request.args.get('page', 1, type=int)
    posts = Table.query.paginate(page=page, per_page=50)
    return render_template('index.html', posts=posts, ruble=ruble)

def telegram(supply):
    if datetime.datetime.now() > Table.query.get(supply):
        

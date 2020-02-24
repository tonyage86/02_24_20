
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

grocery_items = []

class list(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(30), nullable=False)
    store = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.item
        return '<Store %r>' % self.store

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/added')
def added_items():
    return render_template("summary.html", grocery_items=grocery_items)

@app.route('/add', methods=['POST'])
def add():
    item = request.form.get("item")
    store = request.form.get("store")
    if not item or not store:
        return 'please select an item and store'
    grocery_items.append(f"pick up {item} from {store}")
    return redirect("/added")


if __name__ == '__main__':
    app.run(debug=True)



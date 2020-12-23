from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.route("/", methods=['POST','GET'])
def index():
    from models import Writing
    if request.method == "POST":
        content = Writing(content = request.form["content"])
        db.session.add(content)
        db.session.commit()
        return redirect(url_for("index"))
    else:
        quotes = Writing.query.order_by(Writing.date_created).all()
        return render_template("index.html", quotes=quotes)

@app.route("/delete/<int:id>")
def delete(id):
    from models import Writing
    task_to_delete = Writing.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for("index"))
    except:
        return 'There was a problem deleting that task'

@app.route("/update/<int:id>", methods=['POST','GET'])
def update(id):
    from models import Writing
    data = Writing.query.get_or_404(id)
    if request.method == "POST":
        data.content = request.form["content"]
        db.session.commit()
        return redirect(url_for("index"))
    else:
        return render_template('update.html', task = data)



if __name__ == "__main__":
    from models import *
    db.create_all()
    app.run(debug=True)
from datetime import datetime
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # /// la duong dan tuong doi
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Task {}>".format(self.id)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST': # Dinh nghia trong index.html chi co nut Submit la POST
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/") # quay lai root HOME page
        except:
            return "Something wrong."
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "Opps, something was wrong when deleting task."


@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    task_to_update = Todo.query.get_or_404(id)
    if request.method == 'POST':
        try:
            task_to_update.content = request.form['update content']
            db.session.commit()
            return redirect("/")
        except:
            return "Something was wrong when updating task."
    else:
        return render_template("update.html", task=task_to_update)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import sessionmaker
from model import engine, ToDo

app = Flask(__name__)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/', methods=["GET"])
def index():
    tasks = session.query(ToDo).all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=["POST"])
def add():
    task = request.form.get("task")
    task1 = ToDo(title=task.capitalize(), complete=False)
    session.add(task1)
    session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['GET'])
def delete(task_id):
    task = session.query(ToDo).filter(ToDo.id==task_id).first()
    session.delete(task)
    session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['GET'])
def update(task_id):
    task = session.query(ToDo).filter(ToDo.id==task_id).first()
    task.complete = not task.complete
    print(task)
    return redirect(url_for('index'))


if __name__ == ('__main__'):
    app.run(debug=True)
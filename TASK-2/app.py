from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# List to store tasks
tasks = []

# Home route to display tasks
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Route to add a task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))


# Route to delete a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
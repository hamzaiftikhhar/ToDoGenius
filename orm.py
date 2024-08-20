from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, update, delete, values



# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Todo class mapped to the Todo table
class Todo(db.Model):
    __tablename__ = 'Todo'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    taskDesc = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'taskDesc': self.taskDesc,
            'status': self.status,
            'date': self.date
        }

# Create the tables
with app.app_context():
    db.create_all()


@app.route('/', methods=['POST', 'GET'])
def main():
    data = Todo.query.all()
    return render_template('todoList.html', data=data)

@app.route('/database', methods=['POST', 'GET'])
def database():
    data = Todo.query.all()
    serialized_data = [task.serialize() for task in data]
    return jsonify(serialized_data)


@app.route('/addTask', methods=['GET', 'POST'])
def addTask():
    if request.method == 'POST':
        taskStatus = request.form.get('taskStatus')
        taskDesc = request.form.get('taskDesc')
        taskDate = request.form.get('taskDate')
        
        if taskStatus and taskDate and taskDesc:
            new_task1 = Todo(taskDesc=taskDesc, status=taskStatus, date=taskDate)
            db.session.add(new_task1)
            db.session.commit()
            return jsonify({'message': 'Data added successfully'})
        else:
            return jsonify({'message': 'taskDesc or taskDate missing'}), 400
    
    return render_template('todoList.html')

@app.route('/deleteTask', methods=['POST','GET'])
def deleteData():
    id = request.form.get('id')
    user = Todo.query.get(id)
    db.session.delete(user)
    db.session.commit()
    response = 'Data deleted Successfully !'
    return response

# @app.route('/updateTask', methods=['POST','GET'])
# def updateTask():
#     id = request.form.get('id')
#     Desc = request.form.get('Desc')
#     Status = request.form.get('status')
#     Date = request.form.get('date')

#     userdst = Todo.query.filter_by(id)
#     dstdetails = userdst.update({
#                 Todo.taskDesc : Desc,
#                 Todo.status : Status,
#                 Todo.date : Date,
#             })
#     db.session.update(dstdetails)
#     db.session.commit()
#     response = 'Data deleted Successfully !'
#     return response

# @app.route('/updateTask', methods=['POST','GET'])
# def updateTask():
#     id = request.form.get('id')
#     Desc = request.form.get('Desc')
#     Status = request.form.get('status')
#     Date = request.form.get('date')
#     db.session.update(Todo).values(taskDesc = Desc ,status = Status ,date = Date).where(Todo.id == id) or db.session.bulk_update_mappings(Todo).values(taskDesc = Desc ,status = Status ,date = Date).where(Todo.id == id)
#     db.session.commit()
#     response = 'Data deleted Successfully !'
#     return response


@app.route('/updateTask', methods=['POST', 'GET'])
def updateTask():
    id = request.form.get('id')
    Desc = request.form.get('Desc')
    Status = request.form.get('status')
    Date = request.form.get('date')

    task = Todo.query.filter_by(id=id).first()

    if task:
        task.taskDesc = Desc
        task.status = Status
        task.date = Date

        db.session.commit()
        response = 'Task updated successfully!'
    else:
        response = 'Task not found.'

    return response


# Create new Todo entries (run this part separately to avoid re-creating on each request)
def create_sample_data():
    with app.app_context():
        if Todo.query.count() == 0:  # Avoid duplicate entries
            new_task1 = Todo(taskDesc='Dinner Vibes', status='complete', date='08-06-2024')
            new_task2 = Todo(taskDesc='Google meeting', status='Todo', date='08-09-2024')
            db.session.add(new_task1)
            db.session.add(new_task2)
            db.session.commit()
create_sample_data()


# Run this function separately to add sample data
# create_sample_data()

if __name__ == '__main__':
    app.run(debug=True)


#Referesh handle and input ko empty krna after clicking the add button
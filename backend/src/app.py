import flask
from flask import request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = flask.Flask(__name__)
app.config["DEBUG"] = True

conn = psycopg2.connect(
        host="172.18.0.2",
        database="taskapp",
        user="admin",
        password="admin")

cur = conn.cursor(cursor_factory=RealDictCursor)


@app.route("/task", methods=["POST"])
def create_task():
    
    title = request.json['title']
    description = request.json['description']
    due_date = request.json['dueDate']
    is_completed = request.json['isCompleted']

    cur.execute("""INSERT INTO tasks
                      (title, description, created_date, due_date, is_completed)
                   VALUES
                      (%s, %s, now(), %s, %s);""", (title,description,due_date,is_completed,))
    conn.commit();
    return jsonify(
       message="cadastrado com sucesso",
       status= 201
    )

@app.route("/task", methods=["GET"])
def get_tasks():
   cur.execute("SELECT * FROM tasks")
   tasks = cur.fetchall()
   return jsonify(
      tasks
   )

@app.route("/task/<task_id>", methods=["GET"])
def get_task_by_id(task_id):
   cur.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
   tasks = cur.fetchone()
   return jsonify(
      tasks
   )

@app.route("/task/<task_id>", methods=["PUT"])
def update_task(task_id):
    
    title = request.json['title']
    description = request.json['description']
    due_date = request.json['dueDate']
    is_completed = request.json['isCompleted']

    cur.execute("""UPDATE tasks 
                   SET 
                     title = %s, 
                     description = %s,  
                     due_date = %s,  
                     is_completed = %s
                   WHERE id = %s""", (title,description,due_date,is_completed,task_id))
    conn.commit();
    return jsonify(
       message="Atualizado com sucesso",
       status= 201
    )


@app.route("/task/<task_id>", methods=["DELETE"])
def delete_task(task_id):
  cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
  conn.commit()
  return ""

   
if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True, port=5000)
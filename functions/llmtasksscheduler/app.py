from flask import Flask
from schedule import Scheduler
import time

app = Flask(__name__)
scheduler = Scheduler()
queue = []  # File d'attente pour les tâches


@app.route('/task', methods=['POST'])
def add_task():
    task_time = request.form.get('time')  # récupérer l'heure d'exécution spécifiée
    task = request.form.get('task')  # récupérer la tâche à exécuter
    queue.append((task, task_time))
    return "Tâche ajoutée avec succès"


def execute_tasks():
    for task, task_time in queue:
        if time.time() >= task_time:  # Si l'heure actuelle est plus grande ou égale à l'heure d'exécution de la tâche
            exec(task)  # exécuter la tâche
            queue.remove((task, task_time))  # supprimer la tâche de la file d'attente


scheduler.every(1).seconds.do(execute_tasks)  # Exécuter la fonction execute_tasks toutes les secondes

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

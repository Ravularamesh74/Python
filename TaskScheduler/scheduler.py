import json
import time
import threading
from utils import run_command, log

TASK_FILE = "tasks.json"
running = True

class Task:
    def __init__(self, name, task_type, interval, **kwargs):
        self.name = name
        self.task_type = task_type
        self.interval = interval
        self.kwargs = kwargs

    def execute(self):
        log(f"Executing Task: {self.name}")

        if self.task_type == "print":
            print(self.kwargs.get("message", ""))

        elif self.task_type == "command":
            output = run_command(self.kwargs.get("command"))
            print(output)

        log(f"Finished Task: {self.name}")

def load_tasks():
    with open(TASK_FILE, "r") as file:
        data = json.load(file)

    tasks = []
    for t in data:
        tasks.append(Task(
            name=t["name"],
            task_type=t["type"],
            interval=t["interval"],
            message=t.get("message"),
            command=t.get("command")
        ))
    return tasks

def run_task(task):
    while running:
        task.execute()
        time.sleep(task.interval)

def start_scheduler():
    tasks = load_tasks()
    threads = []

    for task in tasks:
        t = threading.Thread(target=run_task, args=(task,))
        t.start()
        threads.append(t)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        global running
        running = False
        log("Shutting down scheduler...")

if __name__ == "__main__":
    start_scheduler()
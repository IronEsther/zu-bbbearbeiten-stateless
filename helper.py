from dataclasses import dataclass
import datetime
from operator import attrgetter

# speicher
todos = []


@dataclass
class todo:
    title: str
    date: datetime.date = None
    isCompleted: bool = False


# BBB-sierung
def add(title, date):
    title = title.replace("b", "bbb").replace("B", "Bbb")
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    todos.sort(key=attrgetter("date"))
    todos.append(todo(title, date))


def get_all():
    return todos


def get(index):
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted


def delete():
    todos.remove = todos

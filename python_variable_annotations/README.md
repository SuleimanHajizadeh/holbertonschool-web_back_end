this readme file for Python - Variable Annotations


🐍 Python — Variable Annotations

A concise guide to understanding and using type annotations in Python.

📌 Overview

Variable annotations allow you to explicitly declare the expected type of a variable, function parameter, or return value.

They improve:

Code readability

Debugging

IDE autocompletion

Static type checking (mypy, pyright, pylint)

Introduced in PEP 526.

🔹 Syntax of Variable Annotations
Basic Examples
age: int = 14
name: str = "Azer"
pi: float = 3.14
is_student: bool = True

Without Initial Value
counter: int
email: str

📦 Annotating Collections

Python uses typing module for complex types.

from typing import List, Dict, Tuple, Set

numbers: List[int] = [1, 2, 3]
person: Dict[str, int] = {"age": 14}
coords: Tuple[int, int] = (10, 20)
unique_ids: Set[str] = {"A", "B", "C"}

🧮 Annotating Functions
Parameters + Return Type
def add(a: int, b: int) -> int:
    return a + b

Multiple types (Union)
from typing import Union

value: Union[int, float] = 3.5

Optional types
from typing import Optional

name: Optional[str] = None

🧱 Annotating Classes
class Student:
    name: str
    grade: int
    
    def __init__(self, name: str, grade: int) -> None:
        self.name = name
        self.grade = grade

🧰 Type Aliases

Useful for long or repeated types.

Vector = list[float]

v: Vector = [1.0, 2.0, 3.5]

🧪 Why Use Type Annotations?
✔ Helps find bugs early

Static type checkers detect incorrect types before runtime.

✔ Makes large projects easier to maintain

Clear expectations for the type of every variable.

✔ Better IDE support

Autocompletion becomes more accurate.

✔ Improves documentation

Your code becomes self-explanatory.

🔒 Are Annotations Enforced at Runtime?

No.
Python does not enforce types during execution.

This is correct code for Python (but not recommended):

x: int = "hello"  # no runtime error

🛠 Running a Type Checker (Optional)
Using mypy:
pip install mypy
mypy your_file.py
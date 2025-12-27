# Milestone 1 – Python Basics

## Learning Objectives
- Gain a solid understanding of Python basics.
- Write clean, well-structured Python code.

## Activities
- Study Python fundamentals: variables, data types, control flow, functions, modules.
- Practice beginner exercises (loops, conditionals, list/dict operations).
- Apply Google Python Style Guide (type hints, docstrings, naming conventions).

## Deliverables
- [x] A short discussion summary of Python basics.
- [x] A set of Python scripts showing basic functionalities (loops, functions, classes).

---

## Discussion Summary: Python Basics

### 1. Variables & Data Types
Variables store data values. Python has no command for declaring a variable; it is created when you assign a value.

| Type | Example | Description |
|------|---------|-------------|
| `str` | `"Hello"` | Text |
| `int` | `42` | Whole numbers |
| `float` | `3.14` | Decimal numbers |
| `bool` | `True` / `False` | Boolean values |
| `list` | `[1, 2, 3]` | Ordered, mutable collection |
| `dict` | `{"key": "value"}` | Key-value pairs |

### 2. Control Flow
Control flow determines the order in which code executes.

- **Conditionals (`if/elif/else`):** Execute code based on conditions.
- **Loops (`for`, `while`):** Repeat code multiple times.
- **`break`/`continue`:** Control loop execution.

### 3. Functions
Functions are reusable blocks of code defined with `def`. They can accept parameters and return values.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

### 4. Modules
Modules are Python files that can be imported to reuse code. Use `import` to include them.

```python
from typing import List
```

### 5. Loops & Conditionals
- **`for` loop:** Iterates over a sequence (list, range, etc.).
- **`while` loop:** Repeats while a condition is true.
- **`if/elif/else`:** Executes code based on conditions.

### 6. List & Dict Operations
- **List:** `.append()`, `for item in list`, list comprehension `[x for x in list]`
- **Dict:** `.items()`, `.keys()`, `.values()`, accessing via `dict["key"]`

### 7. Google Python Style Guide
- **Type Hints:** Specify types for parameters and return values (`def func(x: int) -> str`).
- **Docstrings:** Describe what functions/classes do using `"""triple quotes"""`.
- **Naming:** Use `snake_case` for variables/functions, `CamelCase` for classes.

---

## Project Structure (MVC Pattern)

```
milestone-1/
├── app.py                         # Entry point
├── Models/
│   └── book_model.py              # Book data class
├── Views/
│   └── book_view.py               # CLI user interface
└── Controllers/
    └── book_controller.py         # Application logic
```

## Files Overview

| File | Description |
|------|-------------|
| `app.py` | Main entry point that runs the application |
| `Models/book_model.py` | Defines the `Book` class with title, author, and availability |
| `Views/book_view.py` | Handles all user input/output (menu, prompts, display) |
| `Controllers/book_controller.py` | Connects Model and View, manages application flow |

---

## Resources Used

- **Python Basics:** [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- **MVC Design Pattern:** [GeeksforGeeks - MVC Design Pattern](https://www.geeksforgeeks.org/system-design/mvc-design-pattern/)

---

## Notes

- Implemented a simple **Book Manager** CLI application using the MVC pattern.
- The View is kept independent of the Model (strict separation).
- All code follows the Google Python Style Guide (type hints, docstrings).

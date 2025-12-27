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

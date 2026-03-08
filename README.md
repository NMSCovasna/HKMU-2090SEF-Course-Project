# -WIP-HKMU-2090SEF-Course-Project
Task1&amp;Task2

This Project is maily use for the 2090SEF course project(Preliminary code submission).

<h1>Task 1</h1>  

We are currently working on designing a portable student calendar program using OOP framework, which allows users to select dates and add to-do lists. The complete functionality is still under development and the code is not yet completed.

<img width="1840" height="1176" alt="e5dc419a92061c4cc43c8836638855b4" src="https://github.com/user-attachments/assets/a140bea7-32c6-4ad6-925e-0f54e616d1ca" />
*WIP:GUI Interface*
Only used for verifying the save function: This module aims to deal with the problem that program delete all stored todo list parameters automatically after user closed the program.

<h2>Features</h2>

1."CalendarTodoApp" : Lightweight initialization calendar module
   ``` python
    class CalendarTodoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_NAME)
        self.geometry("920x560")
        self.minsize(860, 500)

        self.store = TodoStore(DATA_FILE)

        today = date.today()
        self.current_year = today.year
        self.current_month = today.month
        self.selected_day = today

        self._build_ui()
        self._render_calendar()
        self._refresh_todo_list()
```
    
    We used the most concise architecture possible to write the GUI. Self-calling fuctions have been used inside it.

2.Encapsulation&Composition in calendar data storing
``` python
class TodoStore:
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.data: dict[str, list[TodoItem]] = {}
        self.ensure_data_dir()
        self.load()

    def ensure_data_dir(self):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def load(self):
        if not self.file_path.exists():
            self.data = {}
            self.save()
            return
```

In order to prevent data from being easily lost when closing the program, we created "TodoStore" and established a long-term storage module using instantiated objects and other methods.


<h2>What's Next</h2>  

<b>Advanced supporting methods</b> is still in planning status.
The current focus is on <b>establishing a timeline</b> in the future and designing a feature that can repeat multiple cycles, rather than displaying it all at once.

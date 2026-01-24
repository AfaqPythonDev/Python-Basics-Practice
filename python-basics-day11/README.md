# Python Basics – Day 11 (Advanced Python 1)

## 📌 Overview
This repository contains my **Day 11 Python practice work**, focused on learning **advanced Python basics** such as modules, imports, utility functions, and program structure.  
The objective of this day was to understand how Python programs are organized and how multiple files work together.

---

## 📚 Topics Covered
- Importing modules  
- `from ... import ...` syntax  
- `as` keyword for aliasing  
- `dir()` function  
- `__name__ == "__main__"`  
- Basic idea of `pip` and virtual environments (concept only)

---

## 📝 Tasks Completed

### 1️⃣ Module Import Practice
- Created a file `mymath.py`
- Defined two functions:
  - `square(n)`
  - `cube(n)`
- Imported the module in the main file
- Took user input
- Printed square and cube values

---

### 2️⃣ from ... import ... Practice
- Imported only the `square` function from `mymath`
- Called it with a different number
- Printed the result

---

### 3️⃣ as Keyword Practice
- Imported `mymath` as `mm`
- Called `mm.cube()`
- Printed the result

---

### 4️⃣ __name__ == "__main__" Practice
- Added a conditional block inside `mymath.py`
- Observed output when:
  - Running `mymath.py` directly  
  - Importing it into another file

---

### 5️⃣ dir() Function Practice
- Imported the built-in `math` module
- Printed `dir(math)` to inspect available functions

---

## 📂 Project Structure

python-basics-day11/
│
├── day11_advanced_python1.py
├── mymath.py
└── README.md


## ▶️ How to Run the Program

1. Make sure Python 3 is installed  
2. Open terminal or command prompt  
3. Run the following commands:

```bash
python mymath.py
python day11_advanced_python1.py
🎯 Learning Outcome
After completing this day, I learned:

How to create and import custom Python modules

How to use different import styles

How aliasing works using the as keyword

How __name__ == "__main__" controls program execution

How to inspect module contents using dir()

🚀 Next Steps
Learn more advanced Python concepts

Practice better program structure

Move towards real-world Python projects

👤 Author
Afaq Ahmad
BS Software Engineering Student
Aspiring Python Backend Developer
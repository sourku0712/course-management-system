# 📚 Course Prerequisite Management System

A **Python-based CLI application** to manage academic courses and their prerequisites. This program allows users to add and remove courses, define prerequisite relationships, detect cycles, and check enrollment eligibility based on completed courses.

---

## 🚀 Features

- ➕ Add new courses
- ❌ Remove existing courses (and clean up prerequisites)
- 🔗 Add prerequisites with **cycle detection**
- 📄 List all direct & indirect prerequisites for a course
- ✅ Check if a student is eligible to enroll based on completed courses
- 🧠 Uses **Depth-First Search (DFS)** for prerequisite traversal

---

## 🛠️ Tech Stack

- **Language:** Python
- **Paradigm:** Procedural Programming
- **Data Structures:**
  - `dict` for course storage
  - `set` for prerequisite relationships

---

## 📂 Project Structure

```
.
├── main.py   # Main application file
└── README.md # Project documentation
```

---

## ▶️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/course-prerequisite-manager.git
   cd course-prerequisite-manager
   ```

2. **Run the program**
   ```bash
   python main.py
   ```

---

## 🧭 Menu Options

```
1. Add a Course
2. Add Prerequisite for a Course
3. Remove a Course
4. List all Prerequisites for a Course
5. Eligibility check to apply for a Course
6. Stop
```

---

## 🧪 Example Workflow

```text
Add Course: CS101 - Intro to Programming
Add Course: CS102 - Data Structures
Add Prerequisite: CS101 → CS102
Check Eligibility: CS102 with completed [CS101]
Result: Eligible to enroll
```

---

## 🔍 Key Concepts Implemented

- **Graph Representation** of courses
- **Cycle Detection** to prevent invalid prerequisite loops
- **Recursive DFS Traversal**
- **Input Validation & Error Handling**

---

## 🌱 Future Enhancements

- 💾 Persistent storage using files or databases
- 🖥️ GUI or Web-based interface
- 📊 Visual graph of course dependencies
- 🔐 User authentication & role-based access

---

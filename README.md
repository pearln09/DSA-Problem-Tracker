# DSA Problem Tracker with Smart Code Evaluator (Python CLI)
An Object-Oriented Programming (OOP) based command-line simulator to solve and evaluate Data Structures & Algorithms (DSA) problems using JSON-defined test cases and secure code execution.

**A. Features:**
- User login and progress tracking
- View DSA problems from structured JSON files
- Submit Python code for automatic evaluation
- Validate code against multiple test cases
- Timeout and runtime error handling using `subprocess`
- Store results and display pass/fail status
- Clean CLI for a smooth user experience

**B. OOP Concepts Used:**
- *Encapsulation*: Separate modules for user data, problem definitions, and code evaluation
- *Inheritance*: Easily extendable evaluator or user types
- *Polymorphism*: Same evaluation interface for different problems and test cases
- *Abstraction*: Hides evaluator internals behind simple user commands

**C. Project Structure:**

```bash
DSA_Problem_Tracker/
├── core/
│   ├── user.py           # User management and progress tracking
│   ├── problem.py        # Loads and displays problems from JSON
│   ├── evaluator.py      # Subprocess-based secure evaluator
├── problems/
│   ├── arrays/
│   │   └── sum_elements.json
├── submissions/
│   └── user_temp.py      # Auto-generated user solution file
├── users.json            # Persistent storage of user statuses
├── main.py               # Main CLI interface
```
**D. Example Problem File (sum_elements.json)**

```json
{
  "id": "sum_array",
  "title": "Sum of Elements",
  "description": "Read an array of integers and print the sum.",
  "test_cases": [
    {
      "input": "1 2 3 4 5",
      "output": "15"
    },
    {
      "input": "10 20",
      "output": "30"
    }
  ]
}
```
**E. Getting Started**

1. Clone the Repo:

```bash
git clone https://github.com/your-username/dsa-problem-tracker.git
cd dsa-problem-tracker
```
2. Create required folder if missing:

```bash
mkdir -p submissions
```
3. Run the CLI tool:

```bash
python main.py
```
**F. Example CLI Usage:**

```bash
--- Welcome to DSA Problem Tracker ---
Enter your username: xyz

Loaded problem: Sum of Elements

1 2 3 4 5
Paste your solution below (end with two enter keys):
arr = list(map(int, input().split()))
print(sum(arr))

Result: Passed
```
**G. User Progress (users.json)**

```json
{
  "xyz": {
    "sum_array": "Passed"
  }
}
```
**H. Built With:**

- Python 3.x
- Object-Oriented Programming (OOP)
- File I/O with JSON
- Subprocess-based code evaluation
- Command-line interface (CLI)

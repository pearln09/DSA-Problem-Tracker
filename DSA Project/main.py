import os
from core.user import User
from core.problem import Problem
from core.evaluator import Evaluator

def list_problems():
    base_path = "problems"
    problems = []
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".json"):
                full_path = os.path.join(root, file)
                problems.append(full_path)
    return problems

def input_user_code():
    print("\nPaste your Python solution below (end with two blank lines):")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return "\n".join(lines)

def main():
    print("=== Welcome to the DSA Problem Tracker CLI ===")
    username = input("Enter your username: ").strip()
    user = User(username)

    while True:
        print("\nMenu:")
        print("1. List Available Problems")
        print("2. Solve a Problem")
        print("3. Show My Progress")
        print("4. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            problems = list_problems()
            if not problems:
                print("No problems found.")
            else:
                for i, prob in enumerate(problems):
                    print(f"[{i}] {prob}")

        elif choice == "2":
            problems = list_problems()
            if not problems:
                print("No problems available.")
                continue

            for i, prob in enumerate(problems):
                print(f"[{i}] {prob}")
            try:
                index = int(input("Enter the number of the problem to solve: "))
                selected_path = problems[index]
            except (ValueError, IndexError):
                print("Invalid selection.")
                continue

            problem = Problem(selected_path)
            problem.show()

            choice = input("\nDo you want to submit your solution? (y/n): ").strip().lower()
            if choice == "y":
                user_code = input_user_code()

                with open("submissions/user_temp.py", "w") as f:
                    f.write(user_code)

                evaluator = Evaluator(problem)
                passed = evaluator.evaluate(user_code)

                result = "Passed" if passed else "Failed"
                print(f"\nYour submission: {result}")
                user.update_status(problem.id, result)

        elif choice == "3":
            user.show_progress()

        elif choice == "4":
            print("Thanks for using the tracker! Goodbye.")
            break

        else:
            print("Invalid choice. Please select from the menu.")

if __name__ == "__main__":
    main()

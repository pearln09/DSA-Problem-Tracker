import json

class Problem:
    def __init__(self, problem_path):
        with open(problem_path, 'r') as f:
            data=json.load(f)
        self.id=data["id"]
        self.title=data["title"]
        self.description=data["description"]
        self.input_format=data["input_format"]
        self.output_format=data["output_format"]
        self.test_cases=data["test_cases"]

    def show(self):
        print(f"Problem: {self.title}")
        print(self.description)
        print("\nInput Format:", self.input_format)
        print("\nOutput Format:", self.output_format)
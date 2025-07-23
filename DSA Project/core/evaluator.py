import subprocess
import tempfile

class Evaluator:
    def __init__(self, problem):
        self.problem = problem
    def evaluate(self, user_code):
        passed=0
        total=len(self.problem.test_cases)

        for case in self.problem.test_cases:
            input_data = case["input"]
            expected = case["output"]
        
            with open("submissions/user_code_temp.py","w") as f:
                f.write(user_code)
        
            try:
                result=subprocess.run(
                    ["python","submissions/user_code_temp.py"],
                    input=input_data.encode(),
                    capture_output=True,
                    timeout=2
                )
                output = result.stdout.decode().strip()
                if output == expected:
                    passed+=1
            except Exception as e:
                print(f"Error: {e}")
                return False
        
        return passed==total
        
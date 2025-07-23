import json

class User:
    def __init__(self, name, filename='users.json'):
        self.name = name
        self.filename = filename
        self.load_user()
    
    def load_user(self):
        try:
            with open(self.filename, 'r') as f:
                users=json.load(f)
        except FileNotFoundError:
            users={}
        self.users=users
        if self.name not in self.users:
            self.users[self.name]={"solved":{}}
            self.save_user()
    
    def update_status(self,problem_id,status):
        self.users[self.name]["solved"][problem_id]=status
        self.save_user()

    def save_user(self):
        with open(self.filename,'w') as f:
            json.dump(self.users,f,indent=4)
    
    def show_progress(self):
        print(f"\n{self.name}'s Solved Problems:")
        for pid, status in self.users[self.name]["solved"].items():
            print(f"{pid}: {status}")
           
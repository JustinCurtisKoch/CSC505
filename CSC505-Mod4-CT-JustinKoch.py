# Module 4: Critical Thinking Assignment (Common Personality Traits)
# Write a Python Script that will print  a brief description and names and number of the important steps in constructing a 'software devloper'. 
# Use Python 'Builder Pattern' for inspiration.

class Developer:
    def __init__(self):
        self.problem_solver = None
        self.communicator = None
        self.learner = None

    def set_problem_solver(self, problem_solver):
        self.problem_solver = problem_solver
        return self

    def set_communicator(self, communicator):
        self.communicator = communicator
        return self

    def set_learner(self, learner):
        self.learner = learner
        return self

    def build(self):
        if self.problem_solver is None or self.communicator is None or self.learner is None:
            raise Exception("Missing required traits")
        return self

    def print_description(self):
        print("An excellent software developer possesses three key traits:")
        print("1. Problem-solving:")
        print(f"  - {self.problem_solver.description}")
        print("2. Communication:")
        print(f"  - {self.communicator.description}")
        print("3. Continuous Learning:")
        print(f"  - {self.learner.description}")

class ProblemSolver:
    def __init__(self, description):
        self.description = description

class Communicator:
    def __init__(self, description):
        self.description = description

class Learner:
    def __init__(self, description):
        self.description = description

# Example usage:
developer = Developer() \
    .set_problem_solver(ProblemSolver("Ability to break down complex problems and find creative solutions.")) \
    .set_communicator(Communicator("Effective communication skills for collaborating with teams and stakeholders.")) \
    .set_learner(Learner("Continuous learning and adaptation to evolving technologies.")) \
    .build()

developer.print_description()

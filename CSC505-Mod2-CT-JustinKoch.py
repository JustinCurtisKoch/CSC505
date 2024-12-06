# Module 2: Critical Thinking Assignment
# Implement the YourLastName class using Python. Prompt user to input the key elements of the diagram and return these objects in a well-formatted output.

# Implement KochClass with attributes for stage name, stage goal, stage activity
class KochClass:
    def __init__(self, stage_name, stage_goal, stage_actvity):
        self.stage_name = stage_name
        self.stage_goal = stage_goal
        self.stage_actvity = stage_actvity

# Use class method to allow user input of stage attributes
    @classmethod
    def user_input(cls):
        stage_name = input("Stage Name: ")
        stage_goal = input("Stage Goal: ")
        stage_activity = input("Stage Activity: ")
        return cls(stage_name, stage_goal, stage_activity)

# Call class and class method
Stage_1 = KochClass.user_input()

# Print attrubutes provided by user input
print(f"-----")
print(f"Description of a stage in the Modified Waterfall Method")
for attribute in Stage_1.__dict__:
    print(f"{attribute}: {getattr(Stage_1, attribute)}")
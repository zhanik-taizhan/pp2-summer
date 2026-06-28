# First parent class
class Teacher:

    def teach(self):
        print("Teaching students")

# Second parent class
class Coach:

    def train(self):
        print("Training players")

# Child class inherits from both parents
class StudentAssistant(Teacher, Coach):

    def help(self):
        print("Helping at university")

# Create object
assistant = StudentAssistant()

assistant.teach()
assistant.train()
assistant.help()
class Main:
    """
    This class will read the config file and will store it as a list
    to be used to other components.
    """
    
    instructions = []
    
    def __init__(self):
        # Read file and save content
        with open("data.config", "r") as file:
            allLines = file.readlines()

        # Store each line that is not a comment or empty
        for line in allLines:
            if len(line.strip()) == 0 or line.strip()[0] == "#":
                continue
            self.instructions.append(line.strip())

    def getInstructions(self):
        return self.instructions

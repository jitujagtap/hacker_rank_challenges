class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        self.initialAge = initialAge
        if initialAge < 0:
            self.initialAge = 0
            print('Age is not valid, setting age to 0.')

    def amIOld(self):
        initialAge = self.initialAge
        if initialAge == 0:
            self.initialAge = initialAge
            print("You are young.")
        elif initialAge < 13:
            self.initialAge = initialAge
            print("You are young.")
        elif initialAge < 18:
            self.initialAge = initialAge
            print("You are a teenager.")
        else:
            self.initialAge = initialAge
            print("You are old.")
        # Do some computations in here and print out the correct statement to the console

    def yearPasses(self):
        # Increment the age of the person in here
        self.initialAge = self.initialAge + 1


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
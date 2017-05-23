#!python3
#Quick example script to create a person based class.

class Person(object):
    def __init__(self, name, age, height, weight, gender, job):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
        self.job = job
	
    #Manual way of displaying job to demo a class function	
    def get_job(self):
        return self.job

    #Calculate BMI (Body Mass Index) = weight * height (in metres squared)
    def bmi(self):
        return (self.weight / ((self.height / 100) ** 2))


#Creating some awesome people using the class
bob = Person("Bob", 30, 180, 80, "Male", "Professional Awesome Programmer Guy")
julian = Person("Julian", 30, 170, 70, "Male", "Professional Smack Talker")


#Technically could have pulled job info with just .job
print(bob.name + ": " + bob.get_job())
print(julian.name + ": " + julian.get_job())

#Calculating BMI using Replacement Field String formatting
print("{} BMI: {}".format(julian.name, julian.bmi()))

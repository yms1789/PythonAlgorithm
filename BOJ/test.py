class Person():
    def __init__(self, name, reg_id, age):
        self.setName(name)
        self.setAge(age)
        self.setReg_id(reg_id)

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getReg_id(self):
        return self.reg_id

    def setName(self, name):
        self.name = name

    def setReg_id(self, reg_id):
        self.reg_id = reg_id

    def setAge(self, ag):
        if 0 <= ag < 350:  # check the correctness of attribute value
            self.age = ag
        else:
            print("*** Error in setting age (name:{}, age:{})".format(self.name, ag))
            self.age = 0  # default value

    def __str__(self):
        return "Person(name={}, reg_id={}, age={})".format(self.getName(),self.getReg_id(), self.getAge())


def printPersonList(L_persons):
    for p in L_persons:
        print(" ", p)


if __name__ == "__main__":
    persons = [
        Person("Kim", 990101, 21), Person("Lee", 980715, 22), Person("Park", 101225, 20),
        Person("Hong", 110315, 19),
        Person("Yoon", 971005, 23), Person("Wrong", 100000, 350)
    ]
    print("persons : ")
    printPersonList(persons)

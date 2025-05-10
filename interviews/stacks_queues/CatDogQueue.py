from datetime import datetime


class catDogType:
    def __init__(self, cat, dog):
        self.cat = []
        self.dog = []
        self.timestamp = []

    def add(self, pet):
        if pet.getType() == "dog":
            self.dog.append(pet)
        elif pet.getType() == "cat":
            self.cat.append(pet)
        else:
            raise Exception("err, not a dog or cat")

    def poll(self):
        if self.cat and self.dog:
            if self.cat[-1].getTimestamp() < self.dog[-1].getTimestamp():
                return self.cat.pop().getPet();
            else:
                return self.dog.pop().getPet();
        elif self.dog:
            return self.dog.pop().getPet()
        elif self.cat:
            return self.cat.pop().getPet()
        else:
            raise Exception("err, queue is empty")

    def pollDog(self):
        if self.dog:
            return self.dog.pop().getPet()
        else:
            raise Exception("err, Dog queue is empty")

    def pollCat(self):
        if self.cat:
            return self.cat.pop().getPet()
        else:
            raise Exception("err, Dog queue is empty")

    def isEmpty(self):
        return self.cat and self.dog

    def isDogQueueEmpty(self):
        return self.dog

    def isCatQueueEmpty(self):
        return self.cat


class Pet:
    def __init__(self, petType):
        self.timestamp = datetime.now()
        self.petType = petType

    def getPetType(self):
        return self.petType

    def getTimestamp(self):
        return self.timestamp

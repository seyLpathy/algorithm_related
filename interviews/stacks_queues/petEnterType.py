class PetEnterType:
    def __init__(self, pet, timestamp):
        self.pet = pet
        self.timestamp = timestamp

    def getPet(self):
        return self.pet

    def getTimestamp(self):
        return self.timestamp

    def getPetType(self):
        return self.getPet().getPetType()

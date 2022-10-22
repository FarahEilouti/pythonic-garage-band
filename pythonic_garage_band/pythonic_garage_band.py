# Base class to handle particular kinds of musicians that will inherit from.
class Musician():

    def __init__(self, name):
        '''
        Base function
        '''
        self.name = name

    def __str__(self):
        return f"my name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def get_instrument(self):
        return f"{self.instrument}"

    def play_solo(self):
        return f"{self.solo}"



class Guitarist(Musician):

    def __init__(self, name):
        '''
        for guitar attribute
        '''

        super().__init__(name)
        self.instrument = "guitar"
        self.solo = "face melting guitar solo"

# for bassist
class Bassist(Musician):

    def __init__(self, name):

        super().__init__(name)
        self.instrument = "bass"
        self.solo = "bom bom buh bom"


class Drummer(Musician):
    def __init__(self, name):

        super().__init__(name)
        self.instrument = "drums"
        self.solo = "rattle boom crash"


class Band():
    
    def __init__(self, name, members):
        '''
        Band instance that have a members attribute 
        which is a list of instances that inherit from Musician base (or super) class.
        '''
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return "This is the Band Class"

    def __repr__(self):
        return f"Name: {self.name}. Members: {self.members}."


    @classmethod
    def to_list(cls):
        return cls.instances

    def play_solos(self):
        return [member.play_solo() for member in self.members]





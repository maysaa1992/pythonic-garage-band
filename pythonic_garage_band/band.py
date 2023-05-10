class Musician():
     def __init__(self,name):
        self.name=name
     def __str__(self):
          pass
     def __repr__(self):
          pass
     def get_instrument(self):
          pass
     def play_solo(self):
        pass
class Guitarist(Musician):
     def __init__(self,name):
          self.name = name
     def __str__(self):
          return f"My name is {self.name} and I play guitar"
     def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
     def get_instrument(self,name="guitar"):
        return name
     def play_solo(self):
        return "face melting guitar solo"
class Band(Musician):
    instances=[]
    def __init__(self,name,members=[]):
        self.name=name
        self.members=members
        Band.instances.append(self)
    def play_solos(lsMember):
        for member in lsMember:
            print(f'Hello {member},Are you want to play a Solo?')
    def __str__(self):
         pass
    def __repr__(self):
            pass
    @classmethod
    def to_list(cls):
      return cls.instances
    def play_solos(self):
      solo = []
      for member in self.members:
        solo.append(member.play_solo())
      return solo
class Bassist(Musician):
   def __init__(self,name):
        self.name=name
   def __str__(self):
          return f"My name is {self.name} and I play bass"
   def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
   def get_instrument(self,name="bass"):
        return name
   def play_solo(self):
       return "bom bom buh bom"
class Drummer(Musician):
      def __init__(self,name):
        self.name=name
      def __str__(self):
          return f"My name is {self.name} and I play drums"
      def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
      def get_instrument(self,name="drums"):
        return name
      def play_solo(self):
        return "rattle boom crash"
class Soldier():
    def __init__(self, name):
        self.name = name

class Guns():
    def __init__(self):
        self.bullets = 15

    def firefight(self):
        print(f"{self.name} skirmish on ground floor ")
        for i in range(self.bullets, -1, -1):
            self.bullets -= 1
            print("tigi-tigitishh =", i)
        print("empty, need reload")
        
    def reload(self):
        self.bullets = 15
        print("reloaded")
        self.firefight()

    def gunplay(self):
        self.firefight()
        self.reload()
        self.firefight()

class Act_of_Shooting(Soldier, Guns):
    def __init__(self, name):
        Soldier.__init__(self, name)
        Guns.__init__(self)

agent = Act_of_Shooting("Ryan")
agent.gunplay()

# Parent class
class Super:
    name = "Name"
    age = 0
    ability = "Ability"
    alignment = "Alignment"

    def info(self):
        msg = "\nName: {}\nAge: {}\nAbility: {}\nAlignment: {}\n".format(self.name,self.age,self.ability,self.alignment)
        return msg

    def help(self):
        msg = self.name + " has done a helpful act!\n"
        return msg

    def hinder(self):
        msg = self.name + " has not been helpful at all!\n"
        return msg
    

# Child class instance
class Hero(Super):
    name = "Tony Stark"
    age = 42
    ability = "Intelligence"
    alignment = "Neutral Good"
    financial_wealth = True
    team = "Avengers"

    # Polymorphism on Parent class method
    def info(self):
        msg = "\nName: {}\nAge: {}\nAbility: {}\nAlignment: {}\nFinancially Wealthy: {}\nTeam: {}\n".format(self.name,self.age,self.ability,self.alignment,self.financial_wealth,self.team)
        return msg
    
    # Child class method
    def snark(self):
        msg = "Giving a sassy, witty retort, " + self.name + " is being quite snarky!\n"
        return msg
    

# Child class instance
class Villain(Super):
    name = "Obadiah Stane"
    age = 61
    ability = "Manipulation"
    alignment = "Neutral Evil"
    hydra_recruit = False
    team = "Unaligned / A.I.M. allied"

    # Polymorphism on Parent class method
    def info(self):
        msg = "\nName: {}\nAge: {}\nAbility: {}\nAlignment: {}\nMember of Hydra: {}\nTeam: {}\n".format(self.name,self.age,self.ability,self.alignment,self.hydra_recruit,self.team)
        return msg
    
    # Child class method
    def destroy(self):
        msg = self.name + " has created a dangerous weapon and is destroying the city!!!\n"
        return msg
    

if __name__ == "__main__":
     hero = Hero()
     vil = Villain()
     print(hero.info())
     print(hero.help())
     print(hero.snark())

     print(vil.info())
     print(vil.hinder())
     print(vil.destroy())

       
   

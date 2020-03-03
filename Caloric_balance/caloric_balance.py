
class CaloricBalance:

    def __init__(self, gender, age, height, weight):
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.balance = -1 * CaloricBalance.getBMR(self, self.gender, self.age, self.height, self.weight)
        return

    def getBMR(self, gender, age, height, weight):
        if gender == 'm' or gender == 'f':
          if gender == 'm':
              answer = 66 + (12.7 * float(height)) + (6.23 * float(weight)) - (6.8 * float(age))
              self.balance = answer
              return answer
          else:
              answer = 655 + (4.7 * float(height)) + (4.35 * float(weight)) - (4.7 * float(age))
              self.balance = answer
              return answer
        return 0.0

    def getBalance(self):
        return self.balance

    def recordActivity(self, caloric_burn_per_pound_per_minute, minutes):
        size = float(caloric_burn_per_pound_per_minute) * float(self.weight)
        flame = size * float(minutes)
        burn = self.balance - flame
        self.balance = burn
        print("your balance has now reached " + str(self.balance) + " good job.")
        return

    def eatFood(self, calories):
        growth = self.balance + int(calories)
        self.balance = growth
        print("your balance has now reached " + str(self.balance) + " good job.")
        return

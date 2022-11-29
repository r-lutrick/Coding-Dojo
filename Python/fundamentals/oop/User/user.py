class User:
    def __init__(self, fn, ln, eml, age):
        self.first_name = fn.capitalize()
        self.last_name = ln.capitalize()
        self.email = eml
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info (self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print(f"{self.first_name} is already enrolled")

    def spend_points(self,amount):
        if (self.gold_card_points - amount) >= 0:
            self.gold_card_points -= amount
        else:
            print(f"Insuffiecient points\nCurrent Ammount: {self.gold_card_points}")

first_user = User("aang", "avatar", "theAvatar@gmail.com", 21)
second_user = User("zuko", "prince", "fireBendThis@icloud.com", 24)


first_user.enroll()
first_user.enroll()
print(f"The {first_user.last_name}, {first_user.first_name} flew to the market to get some fresh fish for Appa")
print(f"{first_user.first_name} has {first_user.gold_card_points} pts and found a lustrious fish for 50 pts")
first_user.spend_points(50)
print(f"Chacchiinnggg! Now {first_user.first_name} has {first_user.gold_card_points} pts and Appa is happy Bison")
print(f"Upon seeing the {first_user.last_name} get a fish for points instead of money enrolled as well to get some food!")
second_user.enroll()
print(f"With the {second_user.gold_card_points} pts, the {second_user.last_name} rushed to purchase some food for 80 pts!")
second_user.spend_points(80)
print(f"Now {second_user.last_name} {second_user.first_name} has {second_user.gold_card_points}")

first_user.display_info()
second_user.display_info()
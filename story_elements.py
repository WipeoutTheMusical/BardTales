import random

class storyElements:
    def __init_(self, badGuy, goodGuy, damsel, treasure, location, fortress)
        self.badGuy = badGuy
        self.goodGuy = goodGuy
        self.damsel = damsel
        self.treasure = treasure
        self.location = location
        self.fortress = fortress

    def pickElements(self):
        badGuys = ['Dragon', 'Space Dragon', 'Radioactive Octopus', 'Centaur Stack', 'Bundle of Plastic Straws', 'Box of Cheddar Cheese Crackers', 'Karen']
        goodGuys = ['Princess', 'Space Prince', 'Space Princess', 'Prince' , 'Bounty Hunter', 'Wizard']
        damsels = ['Princess', 'Litter of Kittens', 'Sea Turtle', 'Expensive Smartphone', 'Bag of Dice']
        treasures = ['Eye of Mahnicuh', 'Call of Lemmy', 'Rod of Beatings', 'Remote of Television', 'Ball of Radiance']
        locations = ['Reasonably Priced Condo', 'Lavish Mansion', 'Generic Castle', 'A Pillow Fortress', 'Overpriced Apartment']
        fortresses = ['Spooky Spaceship', 'Creepy Call Center', 'Ominous Office Supply Store', 'Hair-raising Hospital', 'Dreadful DMV Office'] 

        badGuy = random.choice(badGuys)
        goodGuy = random.choice(goodGuys)
        damsel = random.choice(damsels)
        treasure = random.choice(treasures)
        location = random.choice(locations)
        fortress = random.choice(fortresses)

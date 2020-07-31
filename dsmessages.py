# dsmessages.py

import random


class DSMessages:
    fullmsg = ["Good Luck", "I did it!", "Here", "I can't take this...", "Praise the Sun!"]
    segments = ["**** ahead", "Be wary of ****", "Try ****", "Need ****", "Imminent ****...", "Weakness: ****", "****",
                "****", "****?"]

    inserts = ["Enemy", "Tough enemy", "Hollow", "Soldier", "Knight", "Sniper", "Caster", "Giant", "Skeleton", "Ghost",
               "Bug", "Poison bug", "Lizard", "Drake", "Flier", "Golem", "Statue", "Monster", "Strange creature",
               "Demon", "Darkwraith", "Dragon", "Boss", "Saint", "Wretch", "Charmer", "Miscreant", "Liar", "Fatty",
               "Beanpole", "Merchant", "Blacksmith", "Master", "Prisoner", "Bonfire", "Fog wall", "Humanity", "Lever",
               "Switch", "Key", "Treasure", "Chest", "Weapon", "Shield", "Projectile", "Armour", "Item", "Ring",
               "Sorcery scroll", "Pyromancy scroll", "Miracle scroll", "Ember", "Trap", "Covenant", "Amazing key",
               "Amazing treasure", "Amazing chest", "Amazing weapon", "Amazing shield", "Amazing projectile",
               "Amazing armour", "Amazing item", "Amazing ring", "Amazing sorcery scroll", "Amazing pyromancy scroll",
               "Amazing miracle scroll", "Amazing ember", "Amazing trap", "Close-ranged battle", "Ranged battle",
               "Eliminating one at a time", "Luring it out", "Beating to a pulp", "Lying in ambush", "Stealth",
               "Mimicry", "Pincer attack", "Hitting them in one swoop", "Fleeing", "Charging", "Stabbing in the back",
               "Sweeping attack", "Shield breaking", "Head shots", "Sorcery", "Pyromancy", "Miracles", "Jumping off",
               "Sliding down", "Dashing through", "Rolling", "Backstepping", "Jumping", "Attacking",
               "Holding with both hands", "Kicking", "A plunging attack", "Blocking", "Parrying", "Locking-on", "Path",
               "Hidden path", "Shortcut", "Detour", "Illusionary wall", "Shortcut", "Dead end", "Swamp", "Lava",
               "Forest", "Cave", "Labyrinth", "Safe zone", "Danger zone", "Sniper spot", "Bright spot", "Dark spot",
               "Open area", "Tight spot", "Hidden place", "Exchange", "Gorgeous view", "Fall", "Front", "Back", "Left",
               "Right", "Up", "Down", "Feet", "Head", "Back", "Head", "Neck", "Stomach", "Back", "Arm", "Leg", "Heel",
               "Rear", "Tail", "Wings", "Anywhere", "Strike", "Thrust", "Slash", "Magic", "Fire", "Lightning",
               "Critical hits", "Bleeding", "Poison", "Strong poison", "Curses", "Divine", "Occult", "Crystal",
               "Chance", "Hint", "Secret", "Happiness", "Sorrow", "Life", "Death", "Undead", "Elation", "Grief", "Hope",
               "Despair", "Light", "Dark", "Bravery", "Resignation", "Comfort", "Tears"]

    def randommsg(self):
        # segmented 175:5 full message
        msgtype = random.randint(1, 180)

        if msgtype <= 175:
            # generate a segmented message
            segment = random.choice(self.segments)
            insert = random.choice(self.inserts)

            return segment.replace("****", insert)
        else:
            return random.choice(self.fullmsg)


if __name__ == "__main__":
    a = DSMessages()
    print(a.randommsg())

# counter.py

class Counter:
    def __init__(self):
        try:
            count_file = open("count", "r+")
            str_number = count_file.readline()
            if str_number == "":
                self.count = 0
            else:
                self.count = int(str_number)
        except IOError as err:
            self.count = 0
        
        print(f"Counter initialized as {self.count}")

    
    def increment(self): 
        self.count += 1


    def decrement(self):
        if self.count > 0:
            self.count -= 1


    def reset(self):
        self.count = 0


    def set(self, number):
        self.count = int(number)
        if self.count < 0:
            self.count = 0

    def modify(self, mod):
        if mod[0] == "+":
            self.count += int(mod[1:])
        elif mod[0] == "-":
            self.count -= int(mod[1:])
        
        if self.count < 0:
                self.count = 0

    def write_count(self):
        count_file = open("count", "w+")
        count_file.write(str(self.count))


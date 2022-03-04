class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("change Player's back numnber : From %d to %d" %(self.back_number,new_number))
        self.back_number = new_number


jinhyun = SoccerPlayer("Jinhyun", "MF",10)
print("Player's back number : ", jinhyun.back_number)
jinhyun.change_back_number(5)
print("Player's back number: ", jinhyun.back_number)
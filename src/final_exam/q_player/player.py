class Player:
    def __init__(self,d1,d2,p=True):
        self.d1 = d1
        self.d2 = d2
    
    def check_come_out_roll(self):
        dsum = self.d1 + self.d2
        if self.d1 < 0 or self.d1 > 6 and self.d2 < 0 or self.d2 > 6:
            return 'Invalid Range'
        elif dsum == 7 or dsum == 11:
            return 'Winner'
        elif dsum == 7 or dsum == 11 and p==False:
            return'Loser'
        elif dsum == 2 or dsum == 3 or dsum == 12 and p==True:
            print('Loser')
        elif dsum == 2 or dsum == 3 or dsum == 12 and p==False:
            print('Winner')
        else:
            return dsum
        

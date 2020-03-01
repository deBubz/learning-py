class Card():
    def __init__(self, name):
        self.card_name = name
        self.card_desc = ''
        self.card_bonuses = list()
    
    def sh_detail(self) -> str:
        msg = self.card_name + '\n'
        msg = msg + '\t' + self.card_desc + '\n'
        for b in self.card_bonuses:
            msg = msg + '\t** ' + b + '\n'
        return msg
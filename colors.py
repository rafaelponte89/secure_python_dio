class Colors():
   'This classe changes the colors'

   def __init__(self):
         self.colors_dict= {
        'RED':'[1;31m',
        'BLUE' : "[1;34m",
        'BLACK': '[1;30m',
        'CYAN' : "[1;36m",
        'GREEN' : "[0;32m",
        'RESET' : "[0;0m",
        'BOLD' : "[;1m",
        'REVERSE' : "[;7m",
        'YELLOW': '[1;33m',
        'YELLOW_BK' : '[1;42m',
        'BLACK_BK': '[1;40m',
        'GRAY_BK': '[1;100m',
        'RED_BK': '[1;41m',
        'BLUE_BK': '[1;44m'
        }
   def colorIO(self,text,color,bk='RESET'):
       try:
            self.color = (str)(color.upper())
            self.text = (str)(text)
            self.bk = str(bk.upper())
            if(self.colors_dict[self.color]):
                return '\033'+self.colors_dict[self.bk] + \
                        '\033'+self.colors_dict[self.color] + \
                       self.text + '\033'+self.colors_dict['RESET']
       except KeyError:
           return self.text + '\033' + self.colors_dict['RESET']
class Instrument:
    def play(self):
        pass

class Guitar(Instrument):
    def play(self):
        return "Strumming the guitar."

class Violin(Instrument):
    def play(self):
        return "Playing the violin."
    
class Drums(Instrument):
    def play(self):
        return "Beating the drums."
    

orchestra = [Guitar(), Violin(), Drums()]

for instrument in orchestra:
    print(instrument.play())

class Human:
    def _init_(self,name,occupation):
        self.name = name
        self.occupation = occupation
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name,"plays tennis")
        elif self.occupation == "actor":
            print(self.name,"short film")
    
    def speaks(self):
        print(self.name,"How are you man?")




tom = Human("tom cruise","actor")
tom.do_work()
tom.speaks()

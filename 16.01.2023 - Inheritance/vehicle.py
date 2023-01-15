class Vehicle():
    brand = ""
    model_name = ""
    manufacture_date = ""

    def buy(self):
        print("You are buying", self.__class__.__name__, self.model_name)
class Bike:

    model = ""
    enginecc = 0
    mileage = 0
    color = ""

    def __init__(self, m, cc, mi, co):
        self.model =m
        self.enginecc = cc
        self.mileage = mi
        self.color = co

    def get_model(self):
        return self.model
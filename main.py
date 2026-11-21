class Qahramon:
    def __init__(self, ism, jon):
        self.ism = ism
        self.jon = jon

    def malumot(self):
        print(f"Ism: Kirito, HP: {self.jon}")

    def hujum(self):
        print("Hujim qilyabdi")

class Jangchi(Qahramon):
    def __init__(self, ism, jon, qurol):
        super().__init__(ism, jon)
        self.qurol = qurol

    def malumot(self):
        super().malumot()
        print(f"Qurol: {self.qurol}")

    def hujum(self):
        super().hujum()
        print(f"Qurolbilan: {self.qurol}")

a = Jangchi("Knight", 100, "Qilich")
a.malumot()
a.hujum()

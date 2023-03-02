
class ValueInFile:
    def __init__(self, values):
        self.values = values

    def format_values(self):
        v_str = ""
        for d, v, a, r in zip(self.values[0][::10], self.values[1][::10], self.values[2][::10], self.values[3][::10]):
            v_str += str(d) + "\t" + str(v) + "\t" + str(a) + "\t" + str(r) + "\n"
        return v_str

    def write_in(self):
        file = open("values_cancer.txt", "w")
        values = self.format_values()
        file.write(values)
        file.close()

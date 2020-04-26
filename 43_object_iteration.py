class Tailer:
    def __init__(self, cloth_type, style, measurements=None):
        self.cloth_type = cloth_type
        self.style = style
        if measurements is None:
            self.measurements = []
        self.measurements = measurements

    def create_dress(self):
        pass

    def stich(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        pass


if __name__ == "__main__":
    my_shirt = Tailer("shirt", "hip", [56, 50, 21, 10, 12])

    for vars, value in my_shirt.__dict__.items():
        print(f'{vars} --> {value}')

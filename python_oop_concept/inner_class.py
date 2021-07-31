class Outer:
    def __init__(self):
        self.inner = self.Inner()

    def reveal(self):
        self.inner.inner_display('Calling inner class from outer class')

    class Inner:
        def inner_display(self, msg):
            print(msg)

if __name__ == '__main__':
    # Calling inner class from outer class
    outer = Outer()
    outer.reveal()

    # calling inner class directly
    Outer().Inner().inner_display('Calling inner class directly')
from chef import Chef

# this is the way ChineseChef can inherit all functions of Chef class
class ChineseChef(Chef):

    # overwriting the make_special_dish function from Chef class
    def make_special_dish(self):
        print("The chef has made orange chicken")

    def make_fried_rice(self):
        print("The chef has made fried rice")
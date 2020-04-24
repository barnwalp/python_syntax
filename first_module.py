# Whenever python run a file, it sets a few special variables before it even
# run any code. __name__ is one such variable. when python runs a python file
# directly, it sets this name variable equals to main.

# When we import a module, python sets this __name__ variable, to the name of
# the file so in this case it is first_module
print(f'First Module\'s Name: {"{}".format(__name__)}')

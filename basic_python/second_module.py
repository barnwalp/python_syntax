# it will set __name__ to first_module
import first_module

first_module.main()

print(f'printing from second_module: {__name__}')

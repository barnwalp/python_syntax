# exec.py

# read entire file
with open('module.py') as f:
    source = f.read()

print(f'source = {source!r}')

# parse
from ast import parse

ast = parse(source)

print(f'ast = {ast!r}')

# construct code object
code = compile(ast, 'module.py', mode='exec')

print(f'code = {code!r}')

# evaluate module
namespace = {}
exec(code, namespace)

print(f'namespace = {namespace.keys()}')


# construct module
class mod:
    def __init__(self, name, bases, body):
        self.name, self.bases = name, bases
        self.__dict__.update(body)


module = mod('module', (), namespace)
print(f'module = {dir(module)!r}')

# use module
# bind
f = module.f
print(f'f(1,2) = {f(1, 2)}')

# import module
import math


# does not execute code
# brings the name 'math'
# into scope
# --> math = sys.modules['math']

import collections

Box = collections.namedtuple('Box', ['width', 'height'])

box = Box(10, 20)
print(f'width: {box.width}, height: {box.height}')

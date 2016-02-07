import sys; sys.path.append('../')
from mgz.converter import mgz2json

mgz2json('./examples/TheViper_MbL_1.mgz', './converted/TheViper_MbL_1.json', include_sync=False)
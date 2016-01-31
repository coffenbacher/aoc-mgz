import sys; sys.path.append('../')
from mgz import header, body

# Open the recording
f = open('./examples/TheViper_MbL_1.mgz', 'rb')

# Load header information from file
results = header.parse_stream(f)

# Print out the map dimensions
print results.map_info.size_x, results.map_info.size_y

# Read 100 operations from the file
f.seek(results.header_length)
for i in range(5):
    r = body.operation.parse_stream(f)
    f.seek(r.end)
    print r.type
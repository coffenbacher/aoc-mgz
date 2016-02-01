import sys; sys.path.append('../')
from mgz import header, body

# Open the recording
f = open('./examples/TheViper_MbL_1.mgz', 'rb')

# Load header information from file
results = header.parse_stream(f)

# Print out the map dimensions
print results.map_info.size_x, results.map_info.size_y

# Read all actions from the file
f.seek(0, 2)
eof = f.tell() # Get file size

f.seek(results.header_length) # Seek to the start of the body
actions = []

while f.tell() < eof:
    r = body.operation.parse_stream(f)
    f.seek(r.end)
    actions.append(r)
    
print actions[0:10]
    

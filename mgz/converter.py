import json
from . import header, body

def mgz2json(filename, output, include_sync=True, pretty=True):
    f = open(filename, 'r')
    parsed_header = header.parse_stream(f)
    
    # Get file size
    f.seek(0, 2)
    eof = f.tell()

    # Seek to the start of the body
    f.seek(parsed_header.header_length)

    # Load actions
    actions = []
    while f.tell() < eof:
        r = body.operation.parse_stream(f)
        f.seek(r.end)
        actions.append(r)
        
    if not include_sync:
        actions = filter(lambda a: a['type'] != 'sync', actions)
    # Write output
    d = {'header': parsed_header, 'actions': actions}
    out = open(output, 'w')
    out.write(json.dumps(d, ensure_ascii=False, indent=4 if pretty else None))
    out.close()
    
    return True
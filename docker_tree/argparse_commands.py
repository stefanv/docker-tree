# From
# http://stackoverflow.com/questions/10448200/how-to-parse-multiple-sub-commands-using-python-argparse

def parse_commands(parser, namespace):
  namespaces = []
  extra = namespace.extra
  while extra:
    n = parser.parse_args(extra)
    extra = n.extra
    namespaces.append(n)

  return namespaces

ls = ['TATA', 'ATAT', 'AATA', 'ATAA',
      'AATT', 'ATTT', 'AAAT', 'TATT', 'ATTA', 'TTTA', 'TAAA', 'TTAT',
      'TTAA', 'TAAT']
less = ['CGTGCAA', 'ATGGCGT', 'CAATGGC',
        'GGCGTGC', 'TGCAATG']


def de_brj(st, k):
    edges = []
    nodes = set()
    for i in range(len(st) - k + 1):
        edges.append((st[i:i + k - 1], st[i + 1:i + k]))
        nodes.add(st[i:i + k - 1])
        nodes.add(st[i + 1:i + k])
    return nodes, edges


def visualize(st, k):
    nodes, edges = de_brj(st, k)

    dot_str = 'diagraph DeBruijn graph {\n'
    for node in nodes:
        dot_str += '  %s [label="%s"] ;\n' % (node, node)
    for src, dst in edges:
        dot_str += '  %s -> %s ;\n' % (src, dst)
    return dot_str + '}\n'


print(visualize(''.join(less), 3))

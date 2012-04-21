def nfsmaccepts(current, edges, accepting, visited):
    if current in accepting:
        return ""
    else:
        for edge in edges:
            if edge[0] == current:
                letter = edge[1]
                for option in edges[edge]:
                    if not option in visited:
                        word = nfsmaccepts(option, edges, accepting, visited + [current])
                        if not word == None:
                            return letter + word
        return None

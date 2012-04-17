def fsmsim(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        # Quiz: You fill this out
        # Is there a valid edge?
        if (current, letter) in edges:
        # If so take it
            return fsmsim(string[1:], edges[(current, letter)], edges, accepting)
        # If not return False
        else:
            return False
        # Hint: recursion

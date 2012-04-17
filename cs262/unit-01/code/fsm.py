def fsmsim(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        # Quiz: You fill this out
        # Is there a valid edge?
        # If so take it
        # If not return False
        # Hint: recursion

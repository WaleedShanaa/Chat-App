def sum(max):
    if max>0:
        return(max*sum(max-1))
    return 1


print(sum(5))

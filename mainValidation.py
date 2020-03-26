from mainConfiguration import SearchPattern

def determineSearchFunctionality(arg):
    # print(arg)
    try:
        if( 0 == len(arg) ):
            return SearchPattern.UNDEFINED
        elif ( arg.lower().startswith('loc') ) :
            # print('searching location')
            return SearchPattern.LOCATION
        elif ( arg.lower().startswith('part') ) :
            # print('searching part no')
            return SearchPattern.PARTNO
        else:
            return SearchPattern.UNDEFINED
    except():
        return SearchPattern.UNDEFINED
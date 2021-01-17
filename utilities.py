
def slurp(filePath):
    '''
    Method used to read file into the lexer.
    Arguments:
        - filePath: path of the file to be processed
    '''
    fh = open(filePath, mode="r")
    contents = fh.read()
    fh.close()
    return contents
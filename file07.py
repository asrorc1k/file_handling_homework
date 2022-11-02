def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    
# Read data from file
a=0
    for i in f:
        if i in '0123456789':
            a+=int(i)
    return a
f = open('txt_file/data07.txt')
f = f.read()
print(main(f))
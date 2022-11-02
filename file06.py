def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
# Read data from file
k=[]
for i in f:
    k.append(len(i))
return k
f = open('txt_file/data06.txt')
f = f.read().split()
print(main(f))
Footer
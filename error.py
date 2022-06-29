def Symbolerror(new_line : str):
    symbols = '!@#%^&*()_+-=~`{}[];"\'<>,.?/\|'
    for i in symbols:
        if i in new_line:
            print("ERROR : Invalid symbols found")
            exit()

def Coloncheck(new_line : str):
    i = ':'
    if i in new_line:
        new_check= [i for i in new_line.split()]
        if(i==':'):
            if i in new_check[0] and len(new_check[0])>1 and new_check[0][-1]==':':
                pass
            else:
                print("ERROR : Invalid symbols found")
                exit()

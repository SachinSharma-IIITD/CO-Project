if(error_flag==0):
    for vvii in fullii:
        if vvii[0]=='add':
            print(Addition(vvii[1:]))
        elif vvii[0]=='sub':
            print(Subtraction(vvii[1:]))
        elif vvii[0]=='mov' and '$' in i[2]:
            print(MoveImmediate(vvii[1:]))
        elif vvii[0]=='mov':
            print(MoveRegister(vvii[1:]))
        elif vvii[0]=='mul':
            print(Multiply(vvii[1:]))
        elif vvii[0]=='div':
            print(Divide(vvii[1:]))
        elif vvii[0]=='rs':
            print(Rightshift(vvii[1:]))
        elif vvii[0]=='ls':
            print(Leftshift(vvii[1:]))
        elif vvii[0]=='xor':
            print(Exclusiveor(vvii[1:]))
        elif vvii[0]=='or':
            print(Or(vvii[1:]))
        elif vvii[0]=='and':
            print(And(vvii[1:]))
        elif vvii[0]=='not':
            print(Invert(vvii[1:]))
        elif vvii[0]=='cmp':
            print(Compare(vvii[1:]))
        elif vvii[0]=='ls':
            print(Leftshift(vvii[1:],converter(str(var[vvii[1:][2]]))))
        elif vvii[0]=='st':
            print(Leftshift(vvii[1:],converter(str(var[vvii[1:][2]]))))
        elif vvii[0]=='jmp':
            print(UnconditionalJump(vvii[1:],converter(str(var[vvii[1:][1]]))))
        elif vvii[0]=='jlt':
            print(JumpIfLessThan(vvii[1:],converter(str(var[vvii[1:][1]]))))
        elif vvii[0]=='jgt':
            print(JumpIfgreaterThan(vvii[1:],converter(str(var[vvii[1:][1]]))))
        elif vvii[0]=='je':
            print(JumpIfEqual(vvii[1:],converter(str(var[vvii[1:][1]]))))
        elif vvii[0]=='hlt':
            print('0101000000000000')

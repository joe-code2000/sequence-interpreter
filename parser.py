from opcodes import OPCODES, OPERANDS

def getLastValue (array):
    if(len(array) > 0):
        return array[len(array)-1]
    else:
        return None
    
def parser(string = "", evalute = False ,term = 1):
    string = string.replace(" ","");
    string_len = len(string)
    token_array = []
    token_index = 0;

    num_str = "";

    for token in string:

        match token_index:
            case 0:
                if(token == "("):
                    token_array.append(OPCODES.BRKOP)
                elif(token == "-"):
                    token_array.append(OPCODES.SUB)
                elif(token == "+"):
                    token_array.append(OPCODES.ADD)
                elif(token == "n"):
                    token_array.append(OPCODES.ADD)
                    if(evalute):
                        token_array.append(term)
                    else:
                        token_array.append("n")

                elif(token != "n") and (OPERANDS.__contains__(token) == False):
                    num_str += token
                else:
                    print(f"Error parsing, unexpected token {token} in position {token_index}")
            case _:

                if(OPERANDS.__contains__(token)):
                    if(num_str != ""):
                        token_array.append(float(num_str))
                        num_str = ""

                    if(token == "("):
                        if OPERANDS.__contains__(string[token_index-1]) == False:
                            token_array.append(OPCODES.MUL)
                        token_array.append(OPCODES.BRKOP)

                    elif(token == ")"):
                        
                        token_array.append(OPCODES.BRKCL)
                        if(token_index+1 != string_len):
                            if (OPERANDS.__contains__(string[token_index+1]) == False):
                                token_array.append(OPCODES.MUL)
                            if string[token_index+1] == "(":
                                token_array.append(OPCODES.MUL)
                                
                    elif(token == "^"):
                        if OPCODES.getOpcodes().__contains__(getLastValue(token_array)):
                            token_array.pop()
                        token_array.append(OPCODES.PWR)

                    elif(token == "/"):
                        if OPCODES.getOpcodes().__contains__(getLastValue(token_array)):
                            token_array.pop()
                        token_array.append(OPCODES.DIV)

                    elif(token == "*"):
                        if OPCODES.getOpcodes().__contains__(getLastValue(token_array)):
                            token_array.pop()
                        token_array.append(OPCODES.MUL)

                    if(token == "-"):
                        if getLastValue(token_array) == OPCODES.SUB:
                            token_array.pop()
                            # if OPCODES.getOpcodes().__contains__(getLastValue(token_array)) == False:
                            token_array.append(OPCODES.ADD)
                            if getLastValue(token_array) == OPCODES.BRKCL:
                                token_array.append(OPCODES.ADD)
                        elif getLastValue(token_array) == OPCODES.ADD:
                            token_array.pop()
                            # if OPCODES.getOpcodes().__contains__(getLastValue(token_array)) == False:
                            token_array.append(OPCODES.SUB)
                            if getLastValue(token_array) == OPCODES.BRKCL:
                                token_array.append(OPCODES.SUB)
                        else:
                            token_array.append(OPCODES.SUB)

                    if(token == "+"):
                        if OPCODES.getOpcodes().__contains__(getLastValue(token_array)) == False:
                            token_array.append(OPCODES.ADD)
                        if getLastValue(token_array) == OPCODES.BRKCL:
                            token_array.append(OPCODES.ADD)

                elif(token != "n") and (OPERANDS.__contains__(token) == False):
                    num_str += token
                elif(token == "n"):
                    if(num_str != ""):
                        token_array.append(float(num_str))
                        num_str = ""
                    if(OPERANDS.__contains__(string[token_index-1]) == False):
                        token_array.append(OPCODES.MUL)
                    if(evalute):
                        token_array.append(term)
                    else:
                        token_array.append("n")

        token_index += 1

    if(num_str != ""):
        token_array.append(float(num_str))
        num_str = ""
    
    return token_array

def decomposer(token_array):
    decompose_array = []
    recurse = 1
    index = 0
    idx = 0

    while(recurse > 0):
        temp_array = []
        temp_array_1 = []
        temp_array_2 = []
        brackets = 0
        if len(decompose_array) == 0:
            for opcode in token_array:
                if brackets == 0:
                    if len(temp_array) > 0:
                        index += 1
                        recurse += 1
                        temp_array_1.append(OPCODES.EVAL)
                        temp_array_1.append(index)
                        temp_array_2.append(temp_array)
                        temp_array = []
                    if opcode != OPCODES.BRKOP and OPCODES.BRKCL:
                        temp_array_1.append(opcode)

                if opcode == OPCODES.BRKCL:
                    brackets -= 1

                if brackets > 0:
                    temp_array.append(opcode)
                
                if opcode == OPCODES.BRKOP:
                    brackets += 1
            if len(temp_array) > 0:
                temp_array_2.append(temp_array)
                temp_array = []
                temp_array_1.append(OPCODES.EVAL)
                index += 1
                recurse += 1
                temp_array_1.append(index)
        
            decompose_array.append(temp_array_1)
            temp_array_1 = []

            for arr in temp_array_2:
                if len(arr) > 0:
                    decompose_array.append(arr)
        else:
            temp_array = []
            temp_array_1 = []
            temp_array_2 = []
            brackets = 0
            for opcode in decompose_array[idx]:
                if brackets == 0:
                    if len(temp_array) > 0:
                        index += 1
                        recurse += 1
                        temp_array_1.append(OPCODES.EVAL)
                        temp_array_1.append(index)
                        temp_array_2.append(temp_array)
                        temp_array = []
                    if opcode != OPCODES.BRKOP and OPCODES.BRKCL:
                        temp_array_1.append(opcode)

                if opcode == OPCODES.BRKCL:
                    brackets -= 1

                if brackets > 0:
                    temp_array.append(opcode)
                
                if opcode == OPCODES.BRKOP:
                    brackets += 1
            
            if len(temp_array) > 0:
                temp_array_2.append(temp_array)
                temp_array = []
                temp_array_1.append(OPCODES.EVAL)
                index += 1
                recurse += 1
                temp_array_1.append(index)
            
            decompose_array[idx] = temp_array_1
            temp_array_1 = []

            for arr in temp_array_2:
                if len(arr) > 0:
                    decompose_array.append(arr)
            
        
        idx += 1
        recurse -= 1

    return decompose_array
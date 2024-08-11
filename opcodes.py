from enum import Enum


class OPCODES(Enum):
    EVAL = "EVAL"
    BRKOP = "BRKOP"
    BRKCL = "BRKCL"
    PWR = "PWR"
    DIV = "DIV"
    MUL = "MUL"
    SUB = "SUB"
    ADD = "ADD"

    # Returns all the opcodes in the enumaration
    @classmethod
    def getOpcodes(cls):
        return [x for x in cls]
    
    # Checks if a provided opcode is part of the enumaration
    @classmethod
    def isOpcode(cls,opcode):
        return [x for x in cls].__contains__(opcode)
    
# List of operands
OPERANDS = ["+","-","*","/","^","(",")"]

# A function that returns the precidence priority of an opcode. 
# Priorities are from 0-4 with 0 having the hightest priority and 4 having the lowest
def getPrecidenceOpcode(opcode):
    match opcode:
        case OPCODES.EVAL:
            return({"group":0,"OPCODE":opcode})
        case OPCODES.BRKOP:
            return({"group":1,"OPCODE":opcode})
        case OPCODES.BRKOP:
            return({"group":1,"OPCODE":opcode})
        case OPCODES.PWR:
            return({"group":2,"OPCODE":opcode})
        case OPCODES.DIV:
            return({"group":3,"OPCODE":opcode})
        case OPCODES.MUL:
            return({"group":3,"OPCODE":opcode})
        case OPCODES.ADD:
            return({"group":4,"OPCODE":opcode})
        case OPCODES.SUB:
            return({"group":4,"OPCODE":opcode})
    return None

def calcPrecidence(token_array):
    array = []
    index = 0
    for opcode in token_array:
        match opcode:
            case OPCODES.EVAL:
                array.append({"index":index,"group":0,"OPCODE":opcode})
            case OPCODES.BRKOP:
                array.append({"index":index,"group":1,"OPCODE":opcode})
            case OPCODES.BRKOP:
                array.append({"index":index,"group":1,"OPCODE":opcode})
            case OPCODES.PWR:
                array.append({"index":index,"group":2,"OPCODE":opcode})
            case OPCODES.DIV:
                array.append({"index":index,"group":3,"OPCODE":opcode})
            case OPCODES.MUL:
                array.append({"index":index,"group":3,"OPCODE":opcode})
            case OPCODES.ADD:
                array.append({"index":index,"group":4,"OPCODE":opcode})
            case OPCODES.SUB:
                array.append({"index":index,"group":4,"OPCODE":opcode})
        index += 1
    return array

def getPrecidenceIndex(array,index):
    for x in array:
        if x["index"] == index:
            return x
    return None


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


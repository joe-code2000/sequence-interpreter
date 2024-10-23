import math
import time
from opcodes import OPCODES, getPrecidenceOpcode, getPrecidenceIndex, calcPrecidence
import parser
import utilities


class SequenceInterpreter(object):
    def __init__(self) -> None:
        self.stack = [];

    def execute(self,num_1,opcode,num_2):
        result = 0
        match opcode:
            case OPCODES.PWR:
                if num_1 >= 0:
                    result = math.pow(num_1,num_2)
            case OPCODES.MUL:
                result = num_1 * num_2
            case OPCODES.DIV:
                result = num_1 / num_2
            case OPCODES.ADD:
                result = num_1 + num_2
            case OPCODES.SUB:
                result = num_1 - num_2
        return result
    
    def interpret(self,values,recurse=False):
        result = 0
        stack = self.stack

        if recurse:
            groups = utilities.sorter([x["group"] for x in calcPrecidence(values)],reverse=True,distinct=True)
            res = values
        else:
            groups = utilities.sorter([x["group"] for x in calcPrecidence(values[0])],reverse=True,distinct=True)
            res = values[0]
        
        if len(groups) == 0 and len(values) > 0:
            if type(values[0]) == list and len(values[0]) > 0:
                result = values[0][0]
            else:
                result = values[0]
        
        while len(groups) > 0:
            precidences = calcPrecidence(res)
            index = 0
            temp_array = []
            skip = 0
            opcode_skip = 0
            for opcode in res:
                if OPCODES.getOpcodes().__contains__(opcode):
                    if getPrecidenceOpcode(opcode)["group"] == utilities.getLastValue(groups):
                        pr = getPrecidenceIndex(precidences,index)

                        match opcode:
                            case OPCODES.EVAL:
                                execute = self.interpret(stack[utilities.peek(res,pr["index"])],recurse=True)
                                temp_array.append(execute)
                                skip += 1
                            case _:
                                if len(temp_array) > 0:
                                    num_1 = utilities.getLastValue(temp_array)
                                    num_2 = utilities.peek(res,pr["index"])
                                    if num_2 == OPCODES.SUB:
                                        num_2 = self.execute(0,num_2,utilities.peek(res,pr["index"]+1))
                                        opcode_skip += 1
                                    temp_array.pop()
                                    temp_array.append(self.execute(num_1,opcode,num_2))
                                    skip += 1
                                else:
                                    temp_array.append(self.execute(0,opcode,utilities.peek(res,pr["index"])))
                                    skip += 1
                    else:
                        if opcode_skip == 0:
                            temp_array.append(opcode)
                        elif opcode_skip > 0:
                            opcode_skip -= 1
                else:
                    if skip == 0:
                        temp_array.append(opcode)
                    elif skip > 0:
                        skip -= 1

                index +=1
            res = temp_array
            result = res[0]
            groups.pop()

        return result
    
    def preprocess(self,arr,term):
        copy = arr.copy()

        index = 0
        for el in arr:
            if(isinstance(el,list)):
                copy[index] = self.preprocess(el,term)
            elif(isinstance(el,str)):
                if(el.lower() == "n"):
                    copy[index] = term

            index += 1
        
        return copy

    def run(self,equation,terms=1,step=1):
        print(equation)
        results = []
        i = 1

        while i <= terms:
            parsed = parser.parser(equation, evalute=True, term=i)
            values = parser.decomposer(parsed)
            self.stack = values
            results.append(self.interpret(values))
            i += step

        return results
    
# interpreter = SequenceInterpreter();

# res = interpreter.run("n^3", terms= math.pow(10,6))

# print(res)
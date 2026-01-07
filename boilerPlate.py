from string import Template
import sys
from typing import List
import string

CHARACTERS = string.ascii_letters

VALID_RETURN_TYPES = {
    "int",
    "float",
    "bool",
    "str",
    "list",
    "tuple",
    "dict",
    "set",
    "None",
    "list[int]",
    "list[str]",
    "list[float]",
    "list[bool]",
    "list[list[int]]",
    "list[list[str]]",
    "list[list[float]]",
    "list[list[bool]]",
    "tuple[int]",
    "tuple[str]",
    "tuple[float]",
    "tuple[bool]",
    "tuple[int, int]",
    "tuple[int, str]",
    "tuple[int, float]",
    "tuple[int, bool]",
    "tuple[str, int]",
    "tuple[str, str]",
    "tuple[str, float]",
    "tuple[str, bool]",
    "tuple[float, int]",
    "tuple[float, str]",
    "tuple[float, float]",
    "tuple[float, bool]",
    "tuple[bool, int]",
    "tuple[bool, str]",
    "tuple[bool, float]",
    "tuple[bool, bool]",
    "Optional[ListNode]"
}


"""
sys.argv[1] -> link to problem
sys.argv[2] -> folder to save file
sys.argv[3] -> return type
----------------------
sys.argv[3] -> arg1
.
.
.
sys.argv[n] -> argN
----------------------
"""
def is_valid_return_type(type_str: str) -> bool:
    return type_str in VALID_RETURN_TYPES

def extract_problem_name_from_url(url:str) -> str:
    
    url_parts_problem = url.split("problems")
    problem_name_part = url_parts_problem[1]
    
    problem_name = problem_name_part.split("/")[1]
    if problem_name is None or not problem_name:
        raise ValueError("It was not possible to obtain problem name")
    
    return problem_name

def createBoilerPlate(methodName:str,linkProblem:str,returnType:str,params:str,folder:str):
    if not is_valid_return_type(returnType):
        raise ValueError("Return type invalid")
    
    methodName = methodName.replace("-","_").replace(" ","")
    template = Template("""#Link to problem: $linkProblem
#Time complexity:
#Space complexity: 
                       
class Solution:
    def $methodName(self,$params) -> $returnType:
        pass

                                        
solution = Solution()
print(solution.$methodName())
print(solution.$methodName())
""")

    code = template.substitute(methodName=methodName,linkProblem=linkProblem,returnType=returnType,params=params)

    with open(f"./{folder}/{methodName}.py", "w") as f:
         f.write(code)   

if len(sys.argv) > 3:
    link_problem = sys.argv[1]
    problem_name = extract_problem_name_from_url(link_problem)
    folder_to_save = sys.argv[2]
    return_type = sys.argv[3]
    
    params = sys.argv[4:]
    converted_params = []
    for i,p in enumerate(params):
        if not is_valid_return_type(p):
            raise ValueError("The param type is not valid")

        param = f"{CHARACTERS[i]}:{p}"
        converted_params.append(param)

    converted_params_str = ','.join(converted_params)

    createBoilerPlate(problem_name,link_problem,return_type,converted_params_str,folder_to_save)

else:
    raise ValueError("To generate boiler plate is necessary at least 4 arguments")



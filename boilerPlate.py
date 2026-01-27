from string import Template
import string
from enum import Enum

class TYPE_PROBLEM(Enum):
    DEFAULT = 1
    LINKED_LIST = 2
    TREES = 3

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
    "tuple[int,int]",
    "tuple[int,str]",
    "tuple[int,float]",
    "tuple[int,bool]",
    "tuple[str,int]",
    "tuple[str,str]",
    "tuple[str,float]",
    "tuple[str,bool]",
    "tuple[float,int]",
    "tuple[float,str]",
    "tuple[float,float]",
    "tuple[float,bool]",
    "tuple[bool,int]",
    "tuple[bool,str]",
    "tuple[bool,float]",
    "tuple[bool,bool]",
    "Optional[ListNode]",
    "Optional[Node]",
    "Optional[TreeNode]"
}

def is_valid_return_type(type_str: str) -> bool:
    return type_str in VALID_RETURN_TYPES


def getTemplate(type:TYPE_PROBLEM) -> Template:
    if type == TYPE_PROBLEM.DEFAULT:
        return Template("""#Link to problem: $linkProblem
#Time complexity:
#Space complexity: 
                       
class Solution:
    def $methodName(self,$params) -> $returnType:
        pass

                                        
solution = Solution()
print(solution.$methodName())
print(solution.$methodName())
""")
    
    elif type == TYPE_PROBLEM.LINKED_LIST:
        return Template("""#Link to problem: $linkProblem
#Time complexity:
#Space complexity: 
                        
from typing import Optional
from help.linked_list_definition import ListNode
from help.seed_linked_list import seed, print_linked_list
                       
class Solution:
    def $methodName(self,$params) -> $returnType:
        pass

                                        
solution = Solution()
head = seed()
head_after = solution.$methodName(head)
print_linked_list(head_after)
    
head = seed()
head_after = solution.$methodName(head)
print_linked_list(head_after)
""")
    elif type == TYPE_PROBLEM.TREES:
        return Template("""#Link to problem: $linkProblem
#Time complexity:
#Space complexity: 
                        
from typing import Optional
from help.treeNodeDefinition import TreeNode
from help.seed_binary_tree import seed_binary_tree, print_binary_tree
                       
class Solution:
    def $methodName(self,$params) -> $returnType:
        pass

                                        
solution = Solution()
head = seed_binary_tree()
head_after = solution.$methodName(head)
print_binary_tree(head_after)
    
head = seed_binary_tree()
head_after = solution.$methodName(head)
print_binary_tree(head_after)
""")
def extract_problem_name_from_url(url:str) -> str:
    
    url_parts_problem = url.split("problems")
    problem_name_part = url_parts_problem[1]
    
    problem_name = problem_name_part.split("/")[1]
    if problem_name is None or not problem_name:
        raise ValueError("It was not possible to obtain problem name")
    
    return problem_name

def createBoilerPlate(methodName:str,linkProblem:str,returnType:str,params:str,folder:str):
    type_problem = TYPE_PROBLEM.DEFAULT
    if folder.startswith("linked_list"):
        type_problem = TYPE_PROBLEM.LINKED_LIST
    elif folder.startswith("tree"):
        type_problem = TYPE_PROBLEM.TREES

    if not is_valid_return_type(returnType):
        raise ValueError("Return type invalid")
    
    methodName = methodName.replace("-","_").replace(" ","")
    template = getTemplate(type_problem)

    code = template.substitute(methodName=methodName,linkProblem=linkProblem,returnType=returnType,params=params)

    with open(f"./{folder}/{methodName}.py", "w") as f:
         f.write(code)   

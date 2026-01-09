import json 
import os
import requests
from weasyprint import HTML
from boilerPlate import CHARACTERS
from boilerPlate import createBoilerPlate
from boilerPlate import is_valid_return_type
from boilerPlate import extract_problem_name_from_url

PATH_TO_SAVE_PDF = "./problems"
BASE_URL = "https://leetcode-api-pied.vercel.app/problem"
TEMPLATE_URL = "./template.html"
PATH_OUTPUT_HTML = "./temp.html"

def download_problem_metadata(name_problem:str) -> json:
    if not name_problem:
        raise ValueError("The problem name was not provided")

    url_problem = f"{BASE_URL}/{name_problem}"

    response = None
    try:
        response = requests.get(url_problem)
        if response.status_code < 200 or response.status_code >= 300:
            raise ValueError("The response from the api was not success != 200")
    except Exception as e:
        raise ValueError(f"The following error occurred when trying to get response from the api: {e}")
    
    try:
        return response.json()
    except Exception as e:
        raise ValueError("The following error occurred when trying to convert response api to json {}",e)    

def seed_metadatas_to_template(metadatas:json) -> None:
    if not os.path.isfile(TEMPLATE_URL):
        raise ValueError("The template file was not found")
    
    if not metadatas or not metadatas["questionFrontendId"] or not metadatas["title"] or not metadatas["content"]:
        raise ValueError("The metadatas received was not valid or some field is missing")

    with open(TEMPLATE_URL, "r", encoding="utf-8") as f:
        html = f.read()

    html = html.replace("{{ questionFrontendId }}", metadatas["questionFrontendId"])
    html = html.replace("{{ title }}", metadatas["title"])
    html = html.replace("{{ content }}", metadatas["content"])

    with open(PATH_OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)

def generate_pdf(problem_name:str) -> None:
    if not os.path.isfile(PATH_OUTPUT_HTML):
        raise ValueError("The html file to generate pdf was not found")
    
    os.makedirs(PATH_TO_SAVE_PDF,exist_ok=True)

    path_pdf = f"{PATH_TO_SAVE_PDF}/{problem_name}.pdf"
    
    try:
        HTML(PATH_OUTPUT_HTML).write_pdf(path_pdf)
    except Exception as e:
        raise ValueError(f"The following error occurred when trying to generate pdf from html file {e}")
    finally:
       if os.path.exists(PATH_OUTPUT_HTML):
            os.remove(PATH_OUTPUT_HTML)

def get_return_type() -> str:
    return_type = input("Return type: ")
    while not is_valid_return_type(return_type):
        print("invalid Type ....")
        return_type = input("Return type: ")
    
    return return_type

def get_params() -> str:
    i = 1
    converted_params = []
    while True:
        return_type = input(f"The the {i}th param or any positive number to stop: ")
        if return_type.isdigit():
            break
        while not is_valid_return_type(return_type):
            print("invalid Type ....")
            return_type = input(f"The {i}th param or any positive number to stop: ")
        
        param = f"{CHARACTERS[i - 1]}:{return_type}"
        converted_params.append(param)
        
        i += 1
    
    return ','.join(converted_params)

def generate_boiler_plate(problem_name,link_problem):
    folder = input("Save problem script at folder: ")

    while not os.path.isdir(folder):
        print("folder does not exists ....")
        folder = input("Save problem script at folder: ")
    
    return_type = get_return_type()

    params = get_params()

    createBoilerPlate(problem_name,link_problem,return_type,params,folder)

def start():
    link_problem = input("Link to problem: ")
    problem_name = extract_problem_name_from_url(link_problem)

    generate_boiler_plate(problem_name,link_problem)

    problem_metadatas = download_problem_metadata(problem_name)
    seed_metadatas_to_template(problem_metadatas)
    generate_pdf(problem_name)


start()
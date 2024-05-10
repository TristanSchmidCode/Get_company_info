import requests

class Get_Info():
    path1 = "https://api.company-information.service.gov.uk/company/"
    
    path2 = "https://api.company-information.service.gov.uk/advanced-search/companies"
    
    #the maxumum number of results you want to get when searching for companies. 
    #must be a string that has a value between 1 and 5000
    max_hit_size = "50"


    #returns a dictionary containing the information of the given company
    def get_company_info(companyNum:str )-> str:

        fail_to_find_string ="{\"errors\":[{\"type\":\"ch:service\",\"error\":\"company-profile-not-found\"}]}"
        this_path = Get_Info.path1 + companyNum

        api_key = Get_Info.get_api_key()
        json_string = requests.get(this_path, auth=(api_key,'')).text
        assert not json_string == fail_to_find_string, "No companies were found with the given company number"
        
        return json_string
    
    def get_companys_with_Sic_Code(sic_codes)-> str:
        param = {}
        param["sic_codes"] = sic_codes
        param["size"] = Get_Info.max_hit_size
        json_string = requests.get(Get_Info.path2, auth=(Get_Info.get_api_key(),''),params= param).text
       
        assert type(json_string) == str, "No companies registered with given sic code(s)"
        return json_string

    def get_companys_with_name(name:str) -> str:
        param ={}
        param["company_name_includes"] = name
        param["size"] = Get_Info.max_hit_size

        json_string = requests.get(Get_Info.path2, auth=(Get_Info.get_api_key(),''),params= param).text
        assert type(json_string) == str, "No companies registered with name requirement"
        return json_string
            

    def find_companys_with_parameters(param) -> str:
        if type(param) == list:
            placeholder_dict = {}
            for par in param:
                placeholder_dict[par[0]] = par[1]
            param = placeholder_dict
        else:
            param = {param[0]: param[1]}

        api_key = Get_Info.get_api_key()
        param["size"] = Get_Info.max_hit_size

        json_string = requests.get(Get_Info.path2, auth=(api_key,''),params= param).text
        
        assert type(json_string) == str, "No companies registered with given parameters"

        return json_string

    
    def get_api_key()-> str:
        path = "api_key.txt"
        with open(path, 'r') as file:
            txt = file.read().rstrip()
    
        file.close()
        return txt
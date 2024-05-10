import requests

class Get_Info():
    path1 = "https://api.company-information.service.gov.uk/company/"
    
    path2 = "https://api.company-information.service.gov.uk/advanced-search/companies"

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
        json_string = Get_Info._access_advanced_api(sic_codes)
        assert (json_string is str), "No companies registered with given sic code(s)"

        return json_string

    def get_companys_with_name(name:str) -> str:
        param ={}
        param["company_name_includes"] = name
        json_string = Get_Info._access_advanced_api(param)
        assert (json_string is not str), "No companies registered with name requirement"

        return json_string
            

    def _access_advanced_api (param) -> str:
        api_key = Get_Info.get_api_key()

        json_string = requests.get(Get_Info.path2, auth=(api_key,''),params= param).text
        return json_string

    
    def get_api_key()-> str:
        path = ".gitignore"
        with open(path, 'r') as file:
            txt = file.read().rstrip()
    
        file.close()
        return txt
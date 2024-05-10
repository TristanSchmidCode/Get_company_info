import requests
import json
from my_classes.User_input import Input

class Print():

    write_path = "companyhouse_info.json"
    def print_companie(json_string: str):
        info = json.loads(json_string)
        
        print("Choose the information you want to save")
        print("   (1)Name")
        print("   (2)Company number")
        print("   (3)Addresse(s)")
        print("   (4)Sic Codes")
        print("   (5)All information")

        
        chosen_funtion = Input.input_int("Write the corasponding number: ", 5)

        dict_to_write = {}
        if chosen_funtion == "1":
            dict_to_write["company_name"] = info["company_name"]
        elif chosen_funtion == "2":
            dict_to_write["company_number"] = info["company_number"]
        elif chosen_funtion == "3":
            adresses = {}
            try: #while loop is run until i > amount of registerd offices
                i = 1
                while True:
                    adresses["address_line_" + str(i)] =info["registered_office_address"]["address_line_" + str(i)]
                    i +=1
            except KeyError:      
                dict_to_write["adresses"] = adresses    
        if chosen_funtion == "4":
            dict_to_write["sic_codes"]  = info["sic_codes"]
        if chosen_funtion == "5":
            dict_to_write = info    
 
        file = open(Print.write_path,"w")
        file.write(json.dumps(dict_to_write,indent=4))
        file.close() 
              
    def write_company_list(json_string: str):

        companies = json.loads(json_string) 

        #a dictionary holding all companies with with the specifications given
        #the key is the company name, and value is company number 
        comp_list = {}
        comp_list["items"] = {}
        comp_list["total_hits"] = companies["hits"]


        print(companies is dict)      
        for company in companies["items"]:
            comp_list["items"][company["company_name"]] = company["company_number"]
        file = open(Print.write_path,"w")
        file.write(json.dumps(comp_list, indent= 4))

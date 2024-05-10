from my_classes.User_input import User_input
from my_classes.User_input import Input
from my_classes.Print import Print
from my_classes.Get_Info import Get_Info
Testing = False


def main():
    not_finished = True
    while (not_finished):
        function_and_input= User_input.functionType()

        try:
            if function_and_input[0] == "Get Company Details":
               Print.print_companie(Get_Info.get_company_info(function_and_input[1]))
            elif function_and_input[0] == "get_companys_with_Sic_Code":
                Print.write_company_list(Get_Info.get_companys_with_Sic_Code(function_and_input[1]))  
            elif function_and_input[0] == "get_companys_with_name": 
                Print.write_company_list(Get_Info.get_companys_with_name(function_and_input[1]))
            
        except AssertionError as fail:
            print("\n")
            print(fail)
        
        if not Input.input_bool("continue using the program? (Y/N): "):
            break
            
        




    #file.write(json_search_result)

if __name__== "__main__":
    main()

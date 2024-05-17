from my_classes.User_input import User_input
from my_classes.User_input import Input
from my_classes.Print import Print
from my_classes.Get_Info import Get_Info
Testing = False


def main():
    not_finished = True
    while (not_finished):
        try:
            function= User_input.function_type()
            if function == "1":
                company_num = User_input.get_company_details()
                Print.print_companie(Get_Info.get_company_info(company_num))
            elif function == "2":
                param = User_input.get_parameters()
                Print.write_company_list(Get_Info.find_companys_with_parameters(param))  
        except AssertionError as fail:
            print("\n")
            print(fail)
        
        if not Input.input_bool("continue using the program? (Y/N): "):
            break
            
        




    #file.write(json_search_result)

if __name__== "__main__":
    main()

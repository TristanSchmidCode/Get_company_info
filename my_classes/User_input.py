import requests
class Input:
    #Makes sure the input is a bool
    def input_bool(prompt: str) ->bool:
        
        true_inputs =["yes", "yeah", "y"]
        false_inputs =["no", "nah", "n"]
        user_input = input(prompt).lower()
        if true_inputs.__contains__(user_input):
            return True
        if false_inputs.__contains__(user_input):
            return False
        #If the input was neither a yes or no, goes again
        Input.input_bool(prompt)

    #Makes sure the user inputs an int that is within the given bounds
    def input_int(prompt: str, max_value: int = 100)-> str:
        return_string = input(prompt)
        #tests if the string is an int, goes again
        try:
             test_int = int(return_string)
        except ValueError:
            print("Invalid input, requires intigers only.")
            return Input.input_int(prompt,max_value)
        #if the int is out of bounds goes again
        if (test_int > max_value) or (test_int < 0):
            return Input.input_int(prompt, max_value)
        #if all the passes are checked, returns the string       
        return return_string

class User_input:
    def get_parameters():
        print("Chose which parameter you want to search with\n")
        print("(1)Get Companies with sic code(s)")
        print("(2)Get Comapnies with name requirement")
        print("(3)Get Companies with all the above")
        print("type 1, 2 or 3")
        function = Input.input_int("Choose Function:", 3)

        if function == "1":
            return (User_input._get_companys_with_sic_codes())
        elif function == "2":
            return (User_input.__get_companys_with_name())
        elif function == "3":
            param_list = []

            sic_codes = User_input._get_companys_with_sic_codes() 
            #the api breakes if you use an empty array, so this prevnents the user from sending one
            if sic_codes != False:
                param_list.append(sic_codes)
            param_list.append(User_input.__get_companys_with_name())

            return (param_list)
    def function_type():

        print("\nYou are using (\"Get companie info\")")
        print("You can use the following functions:\n")
        print("(1)Get Company Details")
        print("(2)Get Companys with parameters")
        print("Type 1 or 2")
        
        function = Input.input_int("Choose Function:", 2)
        if function == "1":
            return function
        if function == "2":
            return function
        else:     
            assert False, "(" +function + ") is not a function"
        
        
    
    def get_company_details():
        print("Write the company number of the company you want the Details of")
        comp_number = Input.input_int("Company number: ", 99999999)
        
        return comp_number
    
    #returns false if you gave no sic codes
    def _get_companys_with_sic_codes():
        print("You Chose get_companys_with_Sic_Code.\nType done when finished")
        done = False
        sic_codes =[]
        while not done:

            code = input("Sic Code: ")
            if (len(code) != 5) or (not code.isnumeric()):
                if code.lower() == "done":
                    done = True

            else:
                sic_codes.append(code)
         
        if sic_codes.__len__ () == 0:
            return False
        
        return "sic_codes",sic_codes

    def __get_companys_with_name():
        print("Write a line of text that must be found in the name of all companies given")
        return "company_name_includes",input("Name requerment: ")
    
        
        
    

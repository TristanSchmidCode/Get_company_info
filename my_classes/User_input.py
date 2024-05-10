import requests
testing = False

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
        if test_int > max_value | test_int < 0:
            return Input.input_int(prompt, max_value)
        #if all the passes are checked, returns the string       
        return return_string

class User_input:
    def functionType():

        print("\nYou are using (\"Get companie info\")")
        print("You can use the following functions:\n")
        print("(1)Get Company Details")
        print("(2)Get Companies with sic code(s)\n")
        print("(3)Get Comapnies with name requirement")
        print("Type 1, 2 or 3")
        
        function = Input.input_int("Choose Function:", 2)

        if function == "1":
            return ("Get Company Details", User_input.get_company_details())
        elif function == "2":
            return ("get_companys_with_Sic_Code", User_input.get_companys_with_sic_codes())
        elif function == "3":
            return ("get_companys_with_name", User_input.get_companys_with_name())
        
        assert False, +"(" +function + ") is not a function"
        
        
    
    def get_company_details():
        print("Write the company number of the company you want the Details of")
        if (testing):
            comp_number = "11955470"
        else:
            comp_number = Input.input_int("Company number: ", 99999999)
        
        return comp_number
    
    def get_companys_with_sic_codes():
        print("You Chose get_companys_with_Sic_Code.\nType done when finished")
        done = False
        value =[]
        while not done:
            string = input("Sic Code: ")
            try:
                value.append(int(string))
            except ValueError:
                if string.lower() == "done":
                    done = True
        

        return value

    def get_companys_with_name():
        print("Write a line of text that must be found in the name of all companies given")
        return input("Name requerment: ")
    
        
        
    

def checkdatatype(input_value):
    try:
        if type(eval(input_value))==int:
            print(input_value,'is a integer datatype')
   
        elif type(eval(input_value))==float:
            print(input_value,'is a float datatype')

        elif type(eval(input_value))==complex:
            print(input_value,'is a complex datatype')

        elif type(eval(input_value))==list:
            print(input_value,'is a list datatype')

        elif type(eval(input_value))==tuple:
            print(input_value,'is a tuple datatype')
   
        elif type(eval(input_value))==dict:
            print(input_value,'is a dictionary datatype')
   
        elif type(eval(input_value))==set:
            print(input_value,'is a list datatype')

        elif type(eval(input_value))==frozenset:
            print(input_value,'is a frozenset datatype')

        elif type(eval(input_value))==bool:
            print(input_value,'is a boolean datatype')

        elif type(eval(input_value))==bytes:
            print(input_value,'is a bytes datatype')

        elif type(eval(input_value))==bytearray:
            print(input_value,'is a bytearray datatype')

        elif type(eval(input_value))==memoryview:
            print(input_value,'is a memoryview datatype')

        elif input_value=='None':
            print('How you are consider None, select the option below')
            print('1.Keyword')
            print('2.String\n')
            choose=int(input('Choose the option: '))
            print('\n')
            if choose==1:
                if type(eval(input_value))==type(None):
                    print(input_value,'is NoneType')
            elif choose==2:
                if type(input_value)==str:
                    print(input_value,'is String datatype')
            else:
                print('*** Invalid option ***')
       
    except(SyntaxError,NameError):
        if type(input_value)==str:
            print(input_value,'is a string datatype')
            
dtf=input("Enter valid value to check the datatype: ")
checkdatatype(dtf)
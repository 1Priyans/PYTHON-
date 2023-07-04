_ = '''
Final Syntax:
-----------------------
try:
    -----------------------------------------
     Block of statements which will
     generate Exceptions
     ----------------------------------------
    except <exception-class-name-1>:
        ---------------------------------------
        Block of statements provides
        user-friendly Error Message
        -------------------------------------
    except <exception-class-name-2>:
        ---------------------------------------
        Block of statements provides
        user-friendly Error Message
        -------------------------------------
    -------------------------------------
    except <exception-class-name-n>:
        ---------------------------------------
        Block of statements provides
        user-friendly Error Message
        -------------------------------------
    except :
        ----------------------------------
        ----------------------------------
    else:
        -----------------------------------
        Block of statements
        generates Result
        -----------------------------------
    finally:
        ---------------------------------------
        Block of statements
        executes compulsorily
        ----------------------------------------

        (OR)
    try:
        -----------------------------------------
        Block of statements which will
        generate Exceptions
        -----------------------------------------
    except (exception-class-name-1,exception-class-name-2,......exception-class-name-n):
        ---------------------------------------
        Block of statements provides
        user-friendly Error Message for all exceptions
        -------------------------------------
    except :
        ----------------------------------
        ----------------------------------
    else:
        -----------------------------------
        Block of statements
        generates Result
        -----------------------------------
    finally:
        ---------------------------------------
        Block of statements
        executes compulsorily
        ----------------------------------------'''
# Example:
# Program for Demonstrating keywords for handling the Exception
try: # (try Block or Execution Monitoring Block)
    print("Program Execution Started")
    s1 = input("Enter First Value: ")
    s2 = input("Enter Second Value: ")
    # Convert str  data into int type
    a = int(s1)
    b = int(s2)
    # Calculating Division of Two Numbers
    c = a / b

except ValueError: # (except Block or Execution Processing ing Block
    print("Do not Enter  AlphaNumeric, Str and Symbols")
except ZeroDivisionError:
    print("Do Not Enter Zero in Denominator")

else: # (else Block or Result Generated Block)
    print("Else Block ----> Result Block")
    print("Division of {}/{} = {}".format(a, b, c))
    print("Program Execution Ended")

finally: # (finally Block or Resources Relinquishing Block)
    print("I am from finally Block")

                                        # OR

# Program for Demonstrating keywords for handling the Exception
try: # (try Block or Execution Monitoring Block)
    print("Program Execution Started")
    s1 = input("Enter First Value: ")
    s2 = input("Enter Second Value: ")
    # Convert str  data into int type
    a = int(s1)
    b = int(s2)
    # Calculating Division of Two Numbers
    c = a / b

except (ValueError, ZeroDivisionError): # (except Block or Execution Processing Block
    print("Do not Enter  AlphaNumeric, Str and Symbols")
    print("Do Not Enter Zero in Denominator")

else:  # (else Block or Result Generated Block)
    print("Else Block ----> Result Block")
    print("Division of {}/{} = {}".format(a, b, c))
    print("Program Execution Ended")

finally:  # (finally Block or Resources Relinquishing Block)
    print("I am from finally Block")

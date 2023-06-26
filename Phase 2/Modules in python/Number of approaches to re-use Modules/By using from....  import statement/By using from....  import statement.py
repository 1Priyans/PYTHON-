__Properties = """
=======================================
2) By using from....  import statement
=======================================
=>Here "from" "import" are the key words
=>The purpose of from....  import statement is that " To refer or access the variable names, function names and class 
  names in current program directly without writing module name as alias name of Module name." 
=> we can use  from.... import statement in 3 ways.
-------------------
Syntax-1:       from module name import Variable Names,Function Names, Class Names
------------------ 
=>This syntax imports the Variable Names,Function Names, Class Names of a module.

Example:      from calendar  import  month
                     from aop import addop,subop
		     from mathinfo   import pi,e
		     from icici import bname,addr, simpleint

-----------------------------------------------------------------------------------------------------------
Syntax-2:   from module name import Variable Names as alias name,Function Names as 
                  alias  name ,  Class Names as alias names.
-----------------------------------------------------------------------------------
=>This syntax imports the Variable Names,Function Names, Class Names of a module with Unique alias Names

Example:      from calendar  import  month as m
                     from aop import addop as a,subop as s, mulop as m,
		     from mathinfo   import pi as p ,e as k
		     from icici import  bname as b,addr as n , simpleint  as si
---------------------------------------------------------------------------------------------------------------------	
Syntax-3:       from module name import  *
---------------
=>This syntax imports ALL Variable Names,Function Names, Class Names of a module.
=>This syntax is not recommmended to use bcoz it imports required Features of Module and also import un-interrested 
  features also imported and leads more main memory space.

Example:       from calendar   import  *
                       from aop import  *
		       from mathsinfo  import  *

=>Hence after importing all the variable names, Function names and class names by using "from ....import statement", 
  we must access variable names, Function names and class names Directly without using   Module Names or alias names.

			Variable Name
			Function Name
			Class  Name

=>Hence with "import statement"  we can give alias name for module names only but not for Variables Names, Function Names 
  and Class Names.  Where as with "from ... import statement " we can give alias names for Variables Names, Function Names 
  and Class Names but not for Module Name."""
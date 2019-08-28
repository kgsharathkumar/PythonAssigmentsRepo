'''1. Write and Execute a python program to
	a) Read a value from User via Cmd Line.
	b) Check that enterd value is Celsius or Kelvin number?
	c) If given number is in Celsius, Convert a degree Celsius to Kelvin and fahrenheit.
	d) If given number is in Kelvin, Convert a Kelvin to Celsius and fahrenheit. '''

''' Formulas -
    #Convert celsius to fahrenheit
    (CelsiusVal × 9/5) + 32 = FahrenheitValue(in F)
    
    #Convert celsius to Kelvin
    CelsiusVal + 273.15 = KelvinVal(in K)
    
    #Convert Kelvin to celsius
    CelsiusVal = KelvinVal-273.15
    
    #Convert Kelvin to Fahrenheit
    FahrenheitValue = ((9/5)*(KelvinVal-273.15)+32)
    
'''
''' Most used methods -
    1. input()
    2. int()
    3. float()
    4. str()
'''

temp = input("Enter Temperature: ")
degree = float(temp[:-1])
unit = temp[-1]
print("The Value Entered by User is "+str(degree))

if unit == "C":
    print("The user Entered value is in Celsius ")
    #convert to fahrenheit
    result = degree*1.8+32
    print("The Temperature in Fahrenheit is:",result)
    #Conver to Kelvin
    result_k = degree+273.15
    print("The Temperature in Kelvin is:",result_k)
elif unit == 'K':
    print("The user Entered value is in Kelvin ")
    #Convert temperature from kelvin to celsius
    result_c = float(degree)-273.15
    print("The Temperature in Celsius is:",result_c)
    #convert temperature from kelvin to Fahrenheit
    #(°C × 9/5) + 32
    result_f = (result_c*(9/5))+32
    #result1 = ((9/5)*(degree-273.15)+32)
    print("The Temperatue in Fahrenheit is:", result_f)

else:
    print("NA")
    quit()

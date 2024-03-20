    # Task 1: Simple Logic Puzzles

A = True      #Given Values
B = False
C = True

Results = (A and B) or (C)

print(f"The desired outcome is: {Results}")


A = True    #Given Values
B = False
C = True

Result = (A and B) or (not C)

print(f"The desired outcome is: {Result}")




    # Task 2: Validating Calculations

#Random Expression
Arithmetic_expressionm = 3 + 6 * 9 - 2    

#Calculation Without Parenthesis
result_normal = 3 + 6 * 9 - 2     

#Calculation With Parenthesis
result_with_parentheses = 3 + (6 * 9) - 2    

#Comparing Results
if result_normal == result_with_parentheses:    
    print("The two results match.")
else:
    print("The two results do not match.")

#Final Results Match
print(f"Result without parentheses: {result_normal}")
print(f"Result with parentheses: {result_with_parentheses}")




    #Task 3: Mix and Match

Expression = (12 * 3 - 8) <= (21 + 7) and (24 / 4) == (14 - 8)    #(36 - 8 = 28) <= (28) and (24 / 4 = 6) == 14 - 8 = 6)

print(f"The outcome of the expression is: {Expression}")    #Prediction is Correct


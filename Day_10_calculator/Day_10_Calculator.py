from art import logo
def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2
operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}
def calculator():
  print(logo)
  num1=float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue=True
  while should_continue:
    operation_symbol=input("Pick an operation: ")
    num2=float(input("What's the next number?: "))
    function=operations[operation_symbol]
    answer=function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    choice=input("Type 'y' to continue calculating with {answer} or or type 'r' to restart or type 'n' to exit....")
    if choice=="y":
        num1=answer
    elif choice=="r":
        calculator()
    elif  choice=="n":
        should_continue=False
    else:
        print("Please enter the correct choice..")
        calculator()
calculator()
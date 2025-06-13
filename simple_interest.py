#simple interest
def calculate_simple_interest(principal,rate,time):
  """
  Calculate simple interest
  :param principal: Initial amount
    :param rate: Annual interest rate (in percent)
    :param time: Time period in years
    :return: Simple interest
  """
  return (principal*rate*time)/100
#example usage
if __name__="__main__":
  P=1000
  R=5
  T=2
  interest=calculate_simple_interest(P,R,T)
  print(f"Simple Interest: ${interest}")
  

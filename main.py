from time import perf_counter

def expt(x, n):
  if n < 0:
    raise ValueError("n = {} is less than zero".format(n))
  if n <= 1: 
    return x
  elif n%2 == 0:
    result = expt(x, n//2)
    return result * result
  else:
    return x * expt(x, n - 1)
def old_expt(x,n):
  if n < 0:
    raise ValueError("n = {} is less than zero".format(n))

  result = 1
  for _ in range(n):
    result *= x
      
      
  return result
    
'''def main():
  average_time = 0
  for _ in range(100):
    current_time = perf_counter()
    print("5 ** 5 = {} and 7 ** 3 = {}".format(expt(17,17), expt(17, 17)))
    elapsed_time = perf_counter() - current_time
    #print("elapsed time: {}".format(elapsed_time))
    average_time += elapsed_time
  average_time /= 100
  print(average_time)'''

def main():
  
  
  i = 1
  n_trial = 10
  
  f = open("expt_data.csv", "w")
  f.write("exponent,min_runtime_old,min_runtime_new\n")
  for i in range(1,10000):
    old_minimum_time = 9999
    minimum_time = 9999

    for _ in range(n_trial):
      old_current_time = perf_counter()
      e = ("5 ** 5 = {}".format(old_expt(17,i)))
      old_elapsed_time = perf_counter() - old_current_time
      
      if old_minimum_time > old_elapsed_time:
        old_minimum_time = old_elapsed_time
      
    for _ in range(n_trial):
      current_time = perf_counter()
      e = ("5 ** 5 = {}".format(expt(17,i)))
      elapsed_time = perf_counter() - current_time
      if minimum_time > elapsed_time:
        minimum_time = elapsed_time
    print(i,old_elapsed_time)
    

    f.write(f"{i},{old_elapsed_time},{elapsed_time}\n")
  f.close()
  print(old_minimum_time)
  

if __name__ == '__main__':
  main()
  
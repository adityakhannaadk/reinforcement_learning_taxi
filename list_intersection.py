#Aditya Khanna @adityakhannaadk
#An incredibly simple string comparison method.
#Returns a positive integer.

def compare(a,b):
  lista = a.lower.split(" ")
  listb = b.lower.split(" ")
  return len(list(set(lista).intersection(listb)))
       

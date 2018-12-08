#Aditya Khanna @adityakhannaadk
def compare(a,b):
  lista = a.split(" ")
  listb = b.split(" ")
  return len(list(set(lista).intersection(listb)))
       

def readlines():
  
  file = open('text1.txt', "r")
  for line in file:
   if line[0] == 'M':
     print(line)
    
  file.close()
  
readlines()

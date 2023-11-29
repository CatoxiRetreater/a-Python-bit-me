def count_word():
  file = open('text3.txt', 'r')
  count = 0
  
  for line in file:
    words = line.split()
    for word in words:
      if word == 'Mai':
        count += 1
    print(count)
    
  file.close()
  
count_word()

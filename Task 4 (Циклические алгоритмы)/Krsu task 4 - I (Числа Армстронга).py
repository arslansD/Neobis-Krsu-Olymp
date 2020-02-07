for element in range (100, 1000):
  summary=0
  for elem in str(element):
    summary=int(elem)**3 + summary
  if summary==element:
    print(element)

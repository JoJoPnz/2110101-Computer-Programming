x = input()
if len(x) != 2 :
  print('Error')
elif x in ['01','02','51','53','55','58'] :
  print('OK')
elif 20<=int(x)<=40 :
  print('OK')
else :
  print('Error')
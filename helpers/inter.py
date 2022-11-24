def interprete(vec_red):
  inter=[]
  for vec in vec_red: 
    inter.append("Programacion" if vec >= 0.5 else "Texto")    
  return inter
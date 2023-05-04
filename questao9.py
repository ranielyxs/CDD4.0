while True:

   idade=int(input("Idade:"))
   meses=int(input("Meses:"))
   dias=int(input("Dias:"))

   soma= (365*idade + 30*meses + dias)
   print("A quantidade de dias vividos até agora é:",soma,"dias")

   resp= input("Deseja calcular novamente?")
   if resp!="sim":
       break

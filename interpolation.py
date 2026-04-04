 #!/usr/bin/env python3
 """ Mensagem para email (spam) com espaços especificos editáveis com % 

	User: JAODASJAPA
	created:03/04
	version:1.0

"""

 cliente: Maria, João, Júlia, Gabriel, Marli

 for cliente in cliente:
 
	 email_tmpl = """

     Olá, %(nome)s
    
     Tem interesse em comprar %(produto)s?
    
     Este produto é ótimo para resolver
     %(texto)s
    
     Clique agora em %(link)s
    
     Apenas %(quantidade)d disponiveis!
    
	 Preço promocional %(preço).2f

 """

clientes = ["Maria", "Joao", "Bruno"]

for cliente in clientes: 
	print(email_tmpl
	 % {
	 	 "nome": cliente,
		 "produto": "caneta",
		 "texto": "Escrever muito bem",
		 "link": "https://canetaslegais.com",
	 	 "quantidade": 1,
	  	 "preço": 50.5,
	 	}
	 )

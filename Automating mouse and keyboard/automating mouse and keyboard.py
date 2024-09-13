import json
from pynput import keyboard
from pynput import mouse
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Controller as KeyboardController
import threading
import time

stop_loop = False
def importar_estoque_json():
	try:
		with open('estoque.json', 'r') as file:
			content = file.read()
			if content:
				estoque.update(json.loads(content))
	except (FileNotFoundError, json.JSONDecoderError):
		pass

def on_click(x, y, button, pressed):
	global gravar_coordenadas
	if pressed:
		coordenada = (x, y)
		
		if gravar_coordenadas == True:
			coordenadas.append(coordenada)
			print(coordenadas)
		
		if gravar_coordenadas == False:
			pass




def on_press(key):
	global gravar_coordenadas
	global processo_insercao
	global stop_loop
	try:
		#print(key.char)
		
		if key == keyboard.Key.tab:
			print('Gravando coordenadas...')
			
			gravar_coordenadas = True

		
		if key == keyboard.Key.shift:
			print('Gravação interrompida!')
			gravar_coordenadas = False
		
		if key == keyboard.Key.enter:
			print('Iniciar processo de inserção')
			automacao_thread.start()
			
			#mover_e_clicar(coordenadas)
		
		if key == keyboard.Key.shift:
			print('Parar o processo de inserção')
			processo_insercao = False
			stop_loop = True
			
			print(f'{processo_insercao} ctrl parar')
	
	
	except AttributeError:
		print(f'Tecla especial: {key}')
		
def on_release(key):
	try:
		if key == keyboard.Key:
			print(f'Encerrado')
			return False
	except:
		pass
		




def mover_e_clicar(coordenadas):
	global stop_loop
	tim = 0.3
	mouse = MouseController()
	teclado = KeyboardController()
	itens = 0
	for item_dic, info_dic in estoque.items():
		print(stop_loop)
		if stop_loop:
			break
			
		if itens == 10:
			break
		coordenada_codigo = coordenadas[0]
		coordenada_item = coordenadas[1]
		coordenada_marca = coordenadas[2]
		coordenada_localizacao = coordenadas[3]
		coordenada_preco_venda = coordenadas[4]
		coordenada_custo = coordenadas[5]
		coordenada_quantidade = coordenadas[6]
		coordenada_confirmar = coordenadas[7]
		
		#Codigo
		mouse.position = coordenada_codigo
		time.sleep(tim)
		mouse.click(Button.left,1)
		time.sleep(tim)
		teclado.type(info_dic['codigo'])
		
		#Item
		mouse.position = coordenada_item
		time.sleep(tim)
		mouse.click(Button.left, 1)
		time.sleep(tim)
		teclado.type(item_dic)
		
		#marca
		mouse.position = coordenada_marca
		time.sleep(tim)
		mouse.click(Button.left,1)
		time.sleep(tim)
		if info_dic['marca'] == '':
			teclado.type('sem marca')
		else:
			teclado.type('metalbo')
		
		#Localização
		mouse.position = coordenada_localizacao
		time.sleep(tim)
		mouse.click(Button.left,1)
		time.sleep(tim)
		teclado.type('sem localização')
		
		#preco_venda
		mouse.position = coordenada_preco_venda
		time.sleep(tim)
		mouse.click(Button.left,1)
		time.sleep(tim)
		teclado.type(str(info_dic['valor']))
		
		#Custo
		mouse.position = coordenada_custo
		time.sleep(tim)
		mouse.click(Button.left,1)
		time.sleep(tim)
		teclado.type(str(info_dic['custo']))
		
		#quantidade
		mouse.position = coordenada_quantidade
		time.sleep(tim)
		mouse.click(Button.left,1)
		time.sleep(tim)
		teclado.type(str(info_dic['quantidade']))
		
		#confirmar
		mouse.position = coordenada_confirmar
		time.sleep(tim)
		mouse.click(Button.left,1)
		time.sleep(2)

		itens += 1

def start_listeners():
	print('inicializado')
	listener = keyboard.Listener(on_press=on_press, on_release=on_release)
	listener.start()
	

	listener_mouse = mouse.Listener(on_click=on_click)
	listener_mouse.start()
	
	listener.join()
	listener_mouse.join()
	
def mover_e_clicar_process():
	processo = mover_e_clicar(coordenadas)
	#processo.start()
	

		
estoque = {}
coordenadas = [(533, 144), 
(531, 172), 
(522, 257), 
(509, 312), 
(508, 340), 
(506, 368), 
(502, 396), 
(508, 422)]
gravar_coordenadas = False
processo_insercao = True		
			

importar_estoque_json()	
listener_thread = threading.Thread(target=start_listeners)
listener_thread.start()

automacao_thread = threading.Thread(target=mover_e_clicar_process)



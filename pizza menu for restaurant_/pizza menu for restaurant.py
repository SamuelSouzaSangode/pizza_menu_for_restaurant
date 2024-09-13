import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel,
QPushButton, QRadioButton, QButtonGroup, QTabWidget, QGroupBox,
QVBoxLayout, QHBoxLayout, QGridLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.initializeUI()
		
	def initializeUI(self):
		self.setMinimumSize(700, 700)
		self.setWindowTitle('6.1 - Food Order GUI')
		self.setUpMainWindow()
		self.show()
		
	def setUpMainWindow(self):
		self.tab_bar = QTabWidget()
		
		self.pizza_tab = QWidget() #Janela 1
		self.pizza_tab.setObjectName('Tabs') #Estilo da janela 1
		
		self.wings_tab = QWidget() #Janela 2
		self.wings_tab.setObjectName('Tabs') #Estilo da janela 2
		
		#Acrescentando os nomes dos botões referentes as janelas
		self.tab_bar.addTab(self.pizza_tab, 'Pizza')
		self.tab_bar.addTab(self.wings_tab, 'Wings')
		
		#Chamando os métodos que tem os conteúdos de cada janela Tab
		self.pizzaTab()
		self.wingsTab()
		
		'''Lado Direito'''
		#É o fundo, apenas estético, sem função real
		#Fundo do lado direito parte superior ate a parate inferior
		self.side_widget = QWidget()
		self.side_widget.setObjectName('Tabs')
		

		order_label = QLabel('Seu Pedido')
		order_label.setObjectName('Header')
		
		#Fundo no lado esquerdo, apenas no modo de prepato e ingredients
		#É ajusatdo de acordo com a quantidade de ingredientes		
		items_box = QWidget()
		items_box.setObjectName('Side')
		
		pizza_label = QLabel('Tipo de Pizza: ')
		
		#Mostra a forma de preparo escolhido, começa zerado
		self.display_pizza_label = QLabel('')
		toppings_label = QLabel('Ingredientes: ')
		
		#Mostra os ingredientes escolhidos, começa zerado
		self.display_toppings_label = QLabel('')
		
		extra_label = QLabel('Extra:')
		
		#Mostra os ingredientes extra escolhidos, comeca zerado
		self.display_wings_label = QLabel('')
		
		#Organizando toda a parte direita
		#-tipo de pizza
		#-ingreditens 
		#-Extra 
		#-Widgets
		
		items_grid = QGridLayout()
		items_grid.addWidget(pizza_label, 0, 0,
			Qt.AlignmentFlag.AlignRight)
		items_grid.addWidget(self.display_pizza_label, 0, 1)
		items_grid.addWidget(toppings_label, 1, 0, 
			Qt.AlignmentFlag.AlignRight)
		items_grid.addWidget(self.display_toppings_label, 1, 1)
		items_grid.addWidget(extra_label, 2, 0,
			Qt.AlignmentFlag.AlignRight)
		items_grid.addWidget(extra_label, 2, 0)
		items_grid.addWidget(self.display_wings_label, 2, 1)
		items_box.setLayout(items_grid)
		'''Ao colocar o items_box.setLayout() ao invés 
		de self.setLayout() isso faz com que o layout 
		seja feito dentro do QWidget(). Dessa forma ele
		aumenta e diminui o tamanho automaticamente '''
		
		side_v_box = QVBoxLayout()
		side_v_box.addWidget(order_label)
		#Nesse cado o layout é o items_box
		side_v_box.addWidget(items_box)
		#Esse espaço serve para deixar tudo na parte de cima
		side_v_box.addStretch()
		self.side_widget.setLayout(side_v_box)
		'''Ao colocar self.side_widget.setLayout(), colocar o layout
		todo la de cima dentro do widget side'''
		

		
		#Adicionando tudo na janela principal da pagina
		main_h_box = QHBoxLayout()
		main_h_box.addWidget(self.tab_bar, 1)#Eslaticiadade = Numero
		main_h_box.addWidget(self.side_widget)
		self.setLayout(main_h_box)
		
	def pizzaTab(self):
		tab_pizza_label = QLabel('MONTE SUA PRÓPRIA PIZZA')
		tab_pizza_label.setObjectName('Header')
		
		#Onde a descrição vai ser colocada e a imagem
		description_box = QWidget()
		description_box.setObjectName('ImageBorder')
		
		pizza_image_path = 'pizza.png'
		try:
			with open(pizza_image_path):
				objeto = QLabel(self)
				imagem = QPixmap(pizza_image_path)
				imagem_redimensionada = imagem.scaled(100, 100)
				objeto.setPixmap(imagem_redimensionada)
		except:
			pass
			
		pizza_desc = QLabel()
		pizza_desc.setObjectName('ImageInfo')
		pizza_desc.setText(
			'''<p>Faça uma pizza customizada para você. Comece com 
			sua crosta favorita e adicione os ingredientes mais a 
			quantidade perfeita de queijo e molho.</p>''')
		
		#Garante que o texto seja quebrado em varias linhas caso necess	
		pizza_desc.setWordWrap(True)
		#Marge esquerda, superior, direita, inferior do label
		pizza_desc.setContentsMargins(10, 10, 10, 10)
		
		#Montar o layout da imagem e da descrição da pizza
		pizza_h_box = QHBoxLayout()
		pizza_h_box.addWidget(objeto)
		pizza_h_box.addWidget(pizza_desc, 1)
		description_box.setLayout(pizza_h_box)
		
		#Cria a caixinha bonita
		crust_gbox = QGroupBox()
		crust_gbox.setTitle('ESCOLHA A FORMA')#Título da caixa bonita
		
		self.crust_group = QButtonGroup()#Grupo de botoes
		gb_v_box = QVBoxLayout() #O Layout
		
		crust_list = ['Jogado à mão', 'Plano', 'Recheado']
		
		#Fazendo o laco que vai 
		#-Criar os botoes
		#-Adicionar os botoes no layout
		#-Adicionar os botoes no grupo de botoes
		
		for cr in crust_list:
			crust_rb = QRadioButton(cr) #Criamos os botoes com a lista
			gb_v_box.addWidget(crust_rb)#Colocamos no Layout
			self.crust_group.addButton(crust_rb)#Colocamos no grupo 
		
		#Coloca o layout organizado dentro da caixa
		crust_gbox.setLayout(gb_v_box)
			
		#Criando o grupo box que vão os ingredientes
		toppings_gbox = QGroupBox()
		toppings_gbox.setTitle('ESCOLHA OS INGREDIENTES')
		
		#Criando o grupo de botoes da seleção dos ingredientes
		self.toppings_group = QButtonGroup()
		gb_v_box = QVBoxLayout()
		
		toppings_list = ['Pepperoni', 'Salsa', 'Bacon',
						'Canadian Bacon', 'Befe', 'Picles', 
						'Oliva', 'Tomate', 'Pimentão Verde',
						'Cogumelo', 'Cebola', 'Espinafle', 
						'Queijo']
						
		for top in toppings_list:
			toppings_rb = QRadioButton(top)
			gb_v_box.addWidget(toppings_rb)
			self.toppings_group.addButton(toppings_rb)
		
		#Permite marcar vários botoes 
		self.toppings_group.setExclusive(False)
		toppings_gbox.setLayout(gb_v_box)
		
		add_to_order_button1 = QPushButton('Adicionar ao pedido')
		add_to_order_button1.clicked.connect(self.displayPizzaInOrder)
		
		#Criando o Layout geral Tab(Página 1)
		page1_v_box = QVBoxLayout()
		page1_v_box.addWidget(tab_pizza_label)
		page1_v_box.addWidget(description_box)
		page1_v_box.addWidget(crust_gbox)
		page1_v_box.addWidget(toppings_gbox)
		page1_v_box.addStretch()
		page1_v_box.addWidget(add_to_order_button1, alignment=Qt.AlignmentFlag.AlignRight)
		#Setar a janela 1, self.pizza_tab
		self.pizza_tab.setLayout(page1_v_box)
		
	def wingsTab(self):
		tab_wings_label = QLabel('TENTE COM SUAS ASAS')
		tab_wings_label.setObjectName('Header')
		
		description_box = QWidget()
		description_box.setObjectName('ImageBorder')
		pizza_image_path = 'pizza.png'
		
		try:
			with open(pizza_image_path):
				objeto = QLabel(self)
				imagem = QPixmap(pizza_image_path)
				imagem_redimensionada = imagem.scaled(100, 100)
				objeto.setPixmap(imagem_redimensionada)	
		except:
			pass
			
		wings_desc = QLabel()
		wings_desc.setObjectName('ImageInfo')
		wings_desc.setText(
		'''<p>6 pedaços de um rico sabor, carne branca que fará
		você voltar para mais</p>''')
		wings_desc.setWordWrap(True)
		wings_desc.setContentsMargins(10, 10, 10, 10)
		
		wings_h_box = QHBoxLayout()
		wings_h_box.addWidget(objeto)
		wings_h_box.addWidget(wings_desc, 1)
		description_box.setLayout(wings_h_box)
		
		wings_gbox = QGroupBox()
		wings_gbox.setTitle('ESCOLHA O SEU SABOR')
		
		self.wings_group = QButtonGroup()
		gb_v_box = QVBoxLayout()
		flavors_list = [
					'Buffalo', 'Doce Azedo', 'Teriyaki', 'Barbecue']
					
		for fl in flavors_list:
			flavor_rb = QRadioButton(fl)
			gb_v_box.addWidget(flavor_rb)
			self.wings_group.addButton(flavor_rb)
			
		wings_gbox.setLayout(gb_v_box)
		
		add_to_order_button2 = QPushButton('Adicionar pedido')
		#add_to_order_button2.clicked.connect(self.displayWingsInOrder)
		
		page2_v_box = QVBoxLayout()
		page2_v_box.addWidget(tab_wings_label)
		page2_v_box.addWidget(description_box)
		page2_v_box.addWidget(wings_gbox)
		page2_v_box.addWidget(add_to_order_button2, 
			alignment=Qt.AlignmentFlag.AlignRight)
		page2_v_box.addStretch()
		self.wings_tab.setLayout(page2_v_box)
		
	def displayPizzaInOrder(self):
		#Grupo de botões, se um deles estiver marcado
		if self.crust_group.checkedButton():
			#Texto = texto do botao marcado
			text = self.crust_group.checkedButton().text()
			self.display_pizza_label.setText(text)
			
			#Função que retorna uma lista com os textos dos botoes 
			toppings = self.collectToppingsInList()
			toppings_str = '\n'.join(toppings)#Adiciona organizado linha
			self.display_toppings_label.setText(toppings_str)
			self.update()
			
	def collectToppingsInList(self):
		'''O laço percore a lista que contem o grupo de botões e cada
		botao é o button, button.text() pega os textos desse botoes, se 
		marcado, button.text() entrará na lista que será devolvido pela
		função
		
		'''
		toppings_list =[button.text() for button in list(self.toppings_group.buttons()) if button.isChecked()]
		print(toppings_list)
		return toppings_list
		
		
		
		
		
		
		
		
if __name__ == '__main__':
	style_sheet = '''
		QWidget{
			background-color: #C92108;
		}
		
		QWidget#Tabs{
			background-color: #FCEBCD;
			border-radius: 4px
		}
		
		QWidget#ImageBorder{
			background-color: #FCF9F3;
			border-width: 2px;
			border-style: solid;
			border-radius: 4px;
			border-color: #FABB4C
		}
		
		QWidget#Side{
			background-color: #EFD096;
			border-radius: 4px
		}
		
		QLabel{
			background-color: #EFD096;
			border-width: 2px;
			border-style: solid;
			border-radius: 4px;
			border-color: #EFD096
		}
		
		QLabel#Header{
			background-color: #EFD096;
			border-width: 2px;
			border-style: solid;
			border-radius: 4px;
			border-color: #EFD096;
			padding-left: 10px;
			color: #961A07
		}
		
		QLabel#ImageInfo{
			background-color: #FCF9F3;
			border-radius: 4px
		}
		
		QGroupBox{
			background-color: #FCEBCD;
			color: #961A07
		}
		
		QRadioButton{
			background-color: #FCF9F3;
		}
		
		QPushButton{
			background-color: #C92108;
			border-radius: 4px;
			padding: 6px;
			color: #FFFFFF
		}
		
		QPushButton:pressed{
			background-color: #C86354;
			border-radius: 4px;
			padding: 6px;
			color: #DFD8D7
		}
		'''
		
		
		

		
	
	
	app = QApplication(sys.argv)
	app.setStyleSheet(style_sheet)
	window = MainWindow()
	sys.exit(app.exec())

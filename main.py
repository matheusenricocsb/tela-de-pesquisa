from tkinter.ttk import Style
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItem, QStandardItemModel

pizzas = ('marguerita','mussarela', 'calabresa','portuguesa','frango e catupiry','camarão','napolitana','brigadeiro','três queijos','romeu e julieta','atum','carne do sol')
modelo = QStandardItemModel(len(pizzas),1)
modelo.setHorizontalHeaderLabels(['Pizzas'])

for linha, pizza in enumerate(pizzas): # [(1, 'Gol°), (2, "Celta*) ]
    elemento = QStandardItem (pizza)
    modelo.setItem(linha, 0, elemento)

filtro=QSortFilterProxyModel()
filtro.setSourceModel(modelo)
filtro.setFilterKeyColumn(0)
#filtro.setFilterCaseSensitivity(Qt.CaseInsensitive)

app=QtWidgets.QApplication([])
tela=uic.loadUi("layout.ui")
tela.tableView.setModel(filtro)
tela.tableView.horizontalHeader().setStyleSheet("font-size:40px;color:rgb(50,50,255);")
tela.lineEdit.textChanged.connect(filtro.setFilterRegExp)

tela.show()
app.exec()
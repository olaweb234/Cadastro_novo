from PyQt5 import  uic,QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtWidgets import QMessageBox, QTreeWidgetItem
import datetime
usuarios = []



def logar():
    nome = principal.line_nome.text()
    senha = principal.line_senha.text()
    if nome !='admin'or  senha !='admin':
        QMessageBox.warning(principal, 'Erro', 'senha ou nome incorreto.')
    else: 
        main.show()
        main.BT_SALVAR.clicked.connect(salvar)
        main.bt_remover.clicked.connect(remover_user)
       
        

def remover_user():
    item = main.pg_user.currentItem()
    if item:
        nome = item.text(0)
        data_criacao = item.text(1)
        
        global usuarios
        index = main.pg_user.indexOfTopLevelItem(item)
        if index != -1:
            main.pg_user.takeTopLevelItem(index)
        QMessageBox.information(main, 'Sucesso', f'Usuário "{nome}" removido com sucesso!')
    else:
        QMessageBox.warning(main, 'Erro', 'Nenhum usuário selecionado.')

def salvar():
    nome = main.line_nome.text()
    senha = main.line_senha.text()
    confirmacao = main.line_confimacao.text()

    if senha != confirmacao:
        QtWidgets.QMessageBox.information(main,'ERRO','Senhas diferentes')
    else:
       
        
        usuarios.append({'nome':nome,'senha':senha})
        QtWidgets.QMessageBox.information(main,'sucesso','Salvo')
        mostrar_usuarios()

def mostrar_usuarios():
    main.pg_user.clear()

    for usuario in usuarios:
        item= QTreeWidgetItem([usuario['nome'],'Data de criação'])
        main.pg_user.addTopLevelItem(item) 
        data_criacao = datetime.datetime.now().strftime("%Y-%m-%d ")
        usuario_item = QtWidgets.QTreeWidgetItem(main.pg_user)
        usuario_item.setText(1, data_criacao)
    

app = QtWidgets.QApplication([])  
principal=uic.loadUi("login.ui")
main= uic.loadUi('principal.ui')
principal.Bt_logar.clicked.connect(logar)

principal.show()
app.exec()

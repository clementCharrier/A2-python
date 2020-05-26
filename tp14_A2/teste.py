# import sys
# from PySide2.QtWidgets import QApplication, QPushButton
#
# def appui_bouton():
#     print("Appui sur le bouton")
#
# app = QApplication.instance()
# if not app:
#     app = QApplication(sys.argv)
#
# # creation du bouton
# bouton = QPushButton("mon bouton avec une gestion d'appui")
# # on connecte le signal "clicked" a la fonction appui_bouton
# bouton.clicked.connect(appui_bouton)
# print("sexe")
# # le bouton est rendu visible
# bouton.show()
#
# app.exec_()

chaine="clement"
l=len(chaine)
chaine2=chaine[:l-1]
print(chaine2)

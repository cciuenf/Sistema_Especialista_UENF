#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Specialist(QtGui.QWidget):

    def __init__(self):
        super(Specialist, self).__init__()
        self.initUI()


    def initUI(self):
        self.Programa = QtGui.QWizard()
        self.Programa.addPage(self.createIntroPage())
        self.Programa.addPage(self.createQuestionsPage())
        self.Programa.addPage(self.createConfigurationPage())
        self.Programa.addPage(self.createConclusionPage())
        self.Programa.addPage(self.createNomesPage())
        self.Programa.setWindowTitle("Sistema Especialista")
        self.Programa.show()
        sys.exit(self.Programa.exec_())


    def createIntroPage(self):
        page = QtGui.QWizardPage()
        page.setTitle("Ajuda")

        label = QtGui.QLabel("Esse sistema especialista ira te auxiliar a decidir qual a melhor \
                            configuracao de hardware para o seu computador que  \
                            melhor se adequada as suas necessidades .")
        label.setWordWrap(True)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        page.setLayout(layout)

        return page


    def createQuestionsPage(self):
        page = QtGui.QWizardPage()
        page.setTitle("Questionario")
        page.setSubTitle("Deseja usar seu computador para ...")

        self.Processador = QtGui.QLineEdit( )
        self.GPU = QtGui.QLineEdit()
        self.RAM = QtGui.QLineEdit()
        self.HD = QtGui.QLineEdit()
        self.Processador.setReadOnly(1)
        self.GPU.setReadOnly(1)
        self.RAM.setReadOnly(1)
        self.HD.setReadOnly(1)

        self.conclusao = QtGui.QTextEdit( )
        self.conclusao.setReadOnly(1)

        self.caixa_jogos = QtGui.QCheckBox("Jogar Games de ultima geracao")
        self.connect(self.caixa_jogos, QtCore.SIGNAL('stateChanged(int)'), self.atualizaResultado)
        self.caixa_filmes = QtGui.QCheckBox("Editar Filmes em High Definition ")
        self.connect(self.caixa_filmes, QtCore.SIGNAL('stateChanged(int)'), self.atualizaResultado)
        self.caixa_download = QtGui.QCheckBox("Downloads de Filmes em High Definition ")
        self.connect(self.caixa_download, QtCore.SIGNAL('stateChanged(int)'), self.atualizaResultado)
        self.caixa_basico = QtGui.QCheckBox("Acesso a e-mails e/ou Digitacao")
        self.connect(self.caixa_basico, QtCore.SIGNAL('stateChanged(int)'), self.atualizaResultado)
        self.caixa_fotos = QtGui.QCheckBox("Armazenar/Editar Albuns de Fotos")
        self.connect(self.caixa_fotos, QtCore.SIGNAL('stateChanged(int)'), self.atualizaResultado)
        self.caixa_servidor = QtGui.QCheckBox("Servidor")
        self.connect(self.caixa_servidor, QtCore.SIGNAL('stateChanged(int)'), self.atualizaResultado)
        self.caixa_design = QtGui.QCheckBox("Trabalhar como Designer")
        self.connect(self.caixa_design, QtCore.SIGNAL('stateChanged(int)'), self.atualizaResultado)


        layout = QtGui.QGridLayout()
        layout.addWidget(self.caixa_jogos, 0, 0)
        layout.addWidget(self.caixa_download, 1, 0)
        layout.addWidget(self.caixa_basico, 2, 0)
        layout.addWidget(self.caixa_servidor, 3, 0)
        layout.addWidget(self.caixa_fotos, 4, 0)
        layout.addWidget(self.caixa_filmes, 5, 0)
        layout.addWidget(self.caixa_design, 6, 0)
        page.setLayout(layout)

        return page


    def createConfigurationPage(self):
        page = QtGui.QWizardPage()
        page.setTitle("Resultado")
        page.setSubTitle("Sugiro a seguinte configuracao ...")

        Processador_label = QtGui.QLabel('Processador :')
        GPU_label = QtGui.QLabel('Placa de Video :')
        RAM_label = QtGui.QLabel('Memoria Ram :')
        HD_label = QtGui.QLabel('Disco Rigido :')

        layout = QtGui.QGridLayout()
        layout.addWidget(Processador_label,1,0)
        layout.addWidget(self.Processador,1,1)
        layout.addWidget(GPU_label,2,0)
        layout.addWidget(self.GPU,2,1)
        layout.addWidget(RAM_label,3,0)
        layout.addWidget(self.RAM,3,1)
        layout.addWidget(HD_label,4,0)
        layout.addWidget(self.HD,4,1)
        page.setLayout(layout)

        return page

    def createConclusionPage(self):
        page = QtGui.QWizardPage()
        page.setTitle("Conclusao")


        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.conclusao)
        page.setLayout(layout)

        return page

    def createNomesPage(self):
        page = QtGui.QWizardPage()
        page.setTitle("Universidade Estadual Norte Fluminense")
        page.setSubTitle("Topicos em Inteligencia Artifial III")

        label_professora = QtGui.QLabel("Professora : Annabell Tamariz")
        label_elisson = QtGui.QLabel("Nome : Elisson Michael")
        label_pedro = QtGui.QLabel("Nome : Pedro Henrique")


        layout = QtGui.QVBoxLayout()
        layout.addWidget(label_professora)
        layout.addWidget(label_elisson)
        layout.addWidget(label_pedro)
        page.setLayout(layout)

        return page

    def atualizaResultado(self,valor):

        resultado = ''
        if self.caixa_basico.isChecked():
            resultado += 'Qualquer configuracao de computador hoje em dia, mesmo as mais baratas, acessam a internet e processam digitacao de textos e trabalhos satisfatoriamente.'
        if self.caixa_fotos.isChecked():
            resultado +='Qualquer computador hoje em dia armazena e edita fotos satisfatoriamente.'
        if self.caixa_jogos.isChecked():
            resultado += 'Para rodar os jogos com uma boa taixa de quadros,  o seu computador vai precisar de uma boa placa de video.'
        if self.caixa_filmes.isChecked():
            resultado += 'Editar Filmes em alta definicao exigem um computador de alta perfomance como um todo.'
        if self.caixa_design.isChecked():
            resultado += 'Editar Banners,Posters ou grandes imagens requerem um computador de alta perfomance como um todo.'
        if self.caixa_basico.isChecked() or self.caixa_fotos.isChecked():
            self.Processador.setText('3.0 Ghz')
            self.GPU.setText('Nao e necessario')
            self.RAM.setText('1 GB a 2 GB - 800 Mhz')
            self.HD.setText('160 GB a 250 GB - 5400 RPM')
        if self.caixa_download.isChecked():
            resultado += 'Filmes sao arquivos digitais que ocupam bastante espaco digital, o seu computador vai precisar de um disco rigido com grande capacidade de armazenamento.'
            self.Processador.setText('Dual-Core - 1.6 Ghz')
            self.GPU.setText('OFFBoard - 128 bits - 256 MB ')
            self.RAM.setText('2 GB - 800 Mhz')
            self.HD.setText('1 TB - 7200 RPM')
        if self.caixa_jogos.isChecked() or self.caixa_filmes.isChecked() or self.caixa_design.isChecked():
            self.Processador.setText('Quad-Core - 1.6 Ghz')
            self.GPU.setText('OFFBoard - 256 bits - 1 GB ')
            self.RAM.setText('4 GB - 800 Mhz')
            if self.caixa_download.isChecked():
                self.HD.setText('1 TB - 7200 RPM')
            else:
                self.HD.setText('320 GB a 500 GB - 7200 RPM')
        if self.caixa_servidor.isChecked():
            resultado += 'Servidores precisam ser rapidos e processar grandes quantidades de informacoes, portanto o seu computador vai precisar de um processador rapido.Tambem no quesito velocidade seu computador precisara manter os arquivos mais acessador e usados em memoria RAM, que e mais rapida do que o disco rigido, por isso seu computador vai precisar de uma memoria RAM com grande capacidade de armazenamento.'
            self.Processador.setText('Quad-Core - 1.6 Ghz')
            if self.caixa_jogos.isChecked() or self.caixa_filmes.isChecked() or self.caixa_design.isChecked():
                self.GPU.setText('OFFBoard - 256 bits - 1 GB ')
            elif self.caixa_download.isChecked():
                self.GPU.setText('OFFBoard - 128 bits - 256 MB ')
            else:
                self.GPU.setText('Nao e necessario')
            self.RAM.setText('8 GB a 12 GB - 1600 Mhz')
            self.HD.setText('1 TB a 2 TB - 7200 RPM')

        self.conclusao.setText(resultado)



if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)

    especialista = Specialist()


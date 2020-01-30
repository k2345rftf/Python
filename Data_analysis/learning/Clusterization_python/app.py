      # This Python file uses the following encoding: utf-8
import sys
import model
from interface import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene
from scipy.cluster.hierarchy import dendrogram
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from random import sample

class App(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.solve.clicked.connect(self.solver)
        self.ui.review.clicked.connect(self.reviewer)

    def solver(self, event):
        self.name = self.ui.filename.text()
        if self.name == '':
            return self.ui.Error_label.setText("Поле пустое")
        if (self.name[len(self.name)-5:len(self.name)] is ".xlsx") or (self.name[len(self.name)-4:len(self.name)] is ".csv"):
            return self.ui.Error_label.setText("Не верный тип файла")

        self.scene = QGraphicsScene()
#        axes = self.figure.gca()
        self.size_graf = self.ui.graphicsView.size()
        self.height = self.size_graf.height()
        self.width = self.size_graf.width()
        print(self.height)
        self.figure=plt.figure(figsize = (10,10))
        if self.ui.kmethod.isChecked():
            self.k = self.ui.set_k.value()
            self.data = model.Model(self.name, 'k_method', self.k)

            pca = PCA(n_components=2).fit(self.data.data)
            pca_2d = pca.transform(self.data.data)
            self.h = []
            self.s = tuple(set(self.data.rez))
            self.a = ['g', 'k', 'r', 'y', 'g', 'b','c','m']
            self.n = [
            "o",
            "v",
            "^",
            "<",
            ">",
            "1",
            "2",
            "3",
            "4",
            "8",
            "s",
            "p",
            "*",
            "h",
            "H",
            "+",
            "x",
            "D",
            "d"]
            for i in range(len(self.s)):
                self.h.append([self.s[i], sample(self.a,1)[0],sample(self.n,1)[0]])
            for i in range(0, pca_2d.shape[0]):
                for j in range(len(self.h)):
                    if self.h[j][0] == self.data.rez[i]:
                        plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c=self.h[j][1], marker=self.h[j][2])
                        break
        elif self.ui.single.isChecked():
            self.data = model.Model(self.name, 'single', 0)
            self.b = []
            for i in range(len(self.data.rez)):
                self.b.append(str(i+1))
            dendrogram(self.data.rez)
            self.figure.label = self.b
#            plt.show()
        elif self.ui.ward.isChecked():
            self.data = model.Model(self.name, 'ward', 0)
            self.b = []
            for i in range(len(self.data.rez)):
                self.b.append(str(i+1))
            dendrogram(self.data.rez)
            self.figure.label = self.b
#            plt.show()
        elif self.ui.median.isChecked():
            self.data = model.Model(self.name, 'median', 0)
            self.b = []
            for i in range(len(self.data.rez)):
                self.b.append(str(i+1))
            dendrogram(self.data.rez)
            self.figure.label = self.b
#            plt.show()
        elif self.ui.centroid.isChecked():
            self.data = model.Model(self.name, 'centroid', 0)
            self.b = []
            for i in range(len(self.data.rez)):
                self.b.append(str(i+1))
            dendrogram(self.data.rez)
            self.figure.label = self.b
#            plt.show()
        elif self.ui.weighted.isChecked():
            self.data = model.Model(self.name, 'weighted', 0)
            self.b = []
            for i in range(len(self.data.rez)):
                self.b.append(str(i+1))
            dendrogram(self.data.rez)
            self.figure.label = self.b
#            plt.show()
        elif self.ui.average.isChecked():
            self.data = model.Model(self.name, 'average', 0)
            self.b = []
            for i in range(len(self.data.rez)):
                self.b.append(str(i+1))
            dendrogram(self.data.rez)
            self.figure.label = self.b
#            plt.show()
        elif self.ui.complete.isChecked():
            self.data = model.Model(self.name, 'complete', 0)
            self.b = []
            for i in range(len(self.data.rez)):
                self.b.append(str(i+1))
            dendrogram(self.data.rez)
            self.figure.label = self.b
#            plt.show()
        else:
            self.data = model.Model(self.name, 'dbscan', 0)
#            axes.dendrogram()
            pca = PCA(n_components=2).fit(self.data.data)
            pca_2d = pca.transform(self.data.data)
            self.h = []
            self.s = tuple(set(self.data.rez))
            self.a = ['g', 'k', 'r', 'y', 'g', 'b','c','m']
            self.n = [
            "o",
            "v",
            "^",
            "<",
            ">",
            "1",
            "2",
            "3",
            "4",
            "8",
            "s",
            "p",
            "*",
            "h",
            "H",
            "+",
            "x",
            "D",
            "d"]
            for i in range(len(self.s)):
                self.h.append([self.s[i], sample(self.a,1)[0],sample(self.n,1)[0]])
            for i in range(0, pca_2d.shape[0]):
                for j in range(len(self.h)):
                    if self.h[j][0] == self.data.rez[i]:
                        plt.scatter(pca_2d[i, 0], pca_2d[i, 1], c=self.h[j][1], marker=self.h[j][2])
                        break


        self.canvas = FigureCanvas(self.figure)
        self.scene.addWidget(self.canvas)
        self.ui.graphicsView.setScene(self.scene)
        self.canvas.draw()

    def reviewer(self, event):
        self.dial = QFileDialog()
        self.filen = self.dial.getOpenFileName(self, 'Open file','*\klaster_python','*.xlsx')[0]
        self.ui.filename.setText(self.filen)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = App()
    view.show()
    sys.exit(app.exec_())

# This Python file uses the following encoding: utf-8
from sklearn import datasets
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import linkage

from sklearn.cluster import DBSCAN
import pandas as pd


class Model:
    def __init__(self, filename, method, k):
        if filename[len(filename)-5:len(filename)] == ".xlsx":
            self.data = pd.read_excel(filename)
        else:
            self.data = pd.read_csv(filename)

        if method == 'k_method':
            self.rez = self.k_method(self.data, k)
        elif method == 'dbscan':
            self.rez = self.dbscan(self.data)
        else:
            self.rez = self.ierarh(self.data,method)

    def k_method(self,data,kk):
        self.d = data
        self.k = kk
        self.model = KMeans(n_clusters=self.k)
        self.model.fit(self.d)

        return self.model.predict(self.d)

    def ierarh(self,data,methods):
        self.samples = self.data.values
        self.mergings = linkage(self.samples, method=methods)
        return self.mergings

    def dbscan(self,data):
        self.d = data
        self.dbs = DBSCAN()


        self.dbs.fit(self.d)
        return self.dbs.fit_predict(self.d)


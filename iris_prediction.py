#!/usr/bin/env python

__autor__ = 'Saimadhu Polamuri'
__website__ = 'www.dataaspirant.com'
__createdon__ = '26-May-2015'

__links__ = "http://matplotlib.org/users/screenshots.html"
# Required pakages
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

class IrisPrediction():

	""" predicting iris type using iris data set """

	def __init__(self):

		""" Initialization function for IrisPrediction class """
		
		self.irisdataset = datasets.load_iris()				# Loading iris dataset to irisdataset variable

	def print_irisdata(self):

		""" prints the irisdataset like X_Parameters and Y_parameters( Target variable) """

		print ">>>>>>>>>>>>>>>>>>>>Iris features values<<<<<<<<<<<<<<<<<<<<"
		print self.irisdataset.data
		print ">>>>>>>>>>>>>>>>>>>>Iris Target values<<<<<<<<<<<<<<<<<<<<"
		print self.irisdataset.target

	def separate_data(self):

		features_dict = {}
		features_dict['sepal_length'] = np.array(self.irisdataset.data[:,0])
		features_dict['sepal_width'] = np.array(self.irisdataset.data[:,1])
		features_dict['petal_length'] = np.array(self.irisdataset.data[:,2])
		features_dict['petal_width'] = np.array(self.irisdataset.data[:,3])
		features_dict['target'] = np.array(self.irisdataset.target)
		colors_dict = {0:'red',1:'blue',2:'green'}
		colors_list = [colors_dict[i] for i in features_dict['target']]
		features_dict['colors'] = np.array(colors_list)
		
		return features_dict

	def target_data_graph(self,target_data):

		fig = plt.figure()
		labels = 'Iris_type-1', 'Iris_type-2', 'Iris_type-3'
		target_labels = list(set(target_data))
		target_labels_size = [list(target_data).count(label) for label in target_labels]
		colors = ['yellowgreen', 'blue', 'red']
		plt.pie(target_labels_size,labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)

		plt.axis('equal')
		#plt.show()
		fig.savefig("target_data.jpg")

	def data_graph(self,x_name,y_name,x_points,y_points,colors_list,title_text,file_name):
		
		fig = plt.figure()
		plt.scatter(x_points,y_points,color = colors_list)
		fig.suptitle(title_text, fontsize=20)
		plt.xlabel(x_name, fontsize=18)
		plt.ylabel(y_name, fontsize=16)
		fig.savefig(file_name+'.jpg')
		#return fig
		#fig.show()
	def call_data_graph(self,values_dict):
		x_name = 'sepal_length'
		y_name = 'sepal_width'
		x_points = values_dict['sepal_length']
		y_points = values_dict['sepal_width']
		colors_list = values_dict['colors']
		title_text = "sepal_length VS sepal_width Graph"
		self.data_graph(x_name,y_name,x_points,y_points,colors_list,title_text,'sepal_width-sepal_lenght_graph')
		x_name = 'petal_length'
		y_name = 'petal_width'
		x_points = values_dict['petal_length']
		y_points = values_dict['petal_width']
		title_text = "petal_length VS petal_width Graph"
		self.data_graph(x_name,y_name,x_points,y_points,colors_list,title_text,'petal_width-petal_lenght_graph')
		






def main():

	""" Inheriting IrisPrediction calss """
	irisprediction = IrisPrediction()
	#irisprediction.print_irisdata()
	dict_values = irisprediction.separate_data()
	#irisprediction.call_data_graph(dict_values)
	#irisprediction.target_data_graph(dict_values['target'])

if __name__ == "__main__":
	main()

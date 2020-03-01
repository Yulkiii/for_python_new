import numpy
# scipy.special for the sigmoid function expit()
#from scipy import expit
# library for plotting arrays
import matplotlib.pyplot
# ensure the plots are inside this notebook, not an external window
# helper to load data from PNG image files
import imageio
import json
# neural network class definition
class neuralNetwork:
    # initialise the neural network
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # set number of nodes in each input, hidden, output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        # link weight matrices, wih and who
        # weights inside the arrays are w_i_j, where link is from node i to node j in the next layer
        # w11 w21
        # w12 w22 etc 
        self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))#随机取即可,这个是一个经验函数
        self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))
        # learning rate
        self.lr = learningrate
        self.error=0
        # activation function is the sigmoid function
        e=2.71828
        self.activation_function = lambda x: 1/(1+e**x)
        pass
    # train the neural network
    def train(self, inputs_list, targets_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T
        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)
        # output layer error is the (target - actual)
        output_errors = targets - final_outputs
        self.error=output_errors
        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = numpy.dot(self.who.T, output_errors) 
        # update the weights for the links between the hidden and output layers
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
        # update the weights for the links between the input and hidden layers
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), numpy.transpose(inputs))
        pass
    # query the neural network
    def query(self, inputs_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)
        return final_outputs
# number of input, hidden and output nodes
input_nodes = 9
hidden_nodes = 200
output_nodes = 1
# learning rate
learning_rate = 0.1
# create instance of neural network
flower = neuralNetwork(input_nodes,hidden_nodes,output_nodes, learning_rate)
with open('data1.json', encoding='utf-8') as f:
    line = f.readline()
    d = json.loads(line)
loops=400
for j in range (loops):
    for i in d:
        list1=d[i]
        listAf=[]
        listAh=list1[0:9]
        listAf.append(list1[9])
        listAh=numpy.asarray(listAh) 
        listAf=numpy.asarray(listAf)
        listAf=listAf/32+0.5
        listAh=listAh/32+0.5
        flower.train(listAh,listAf)
    if j%10==0:
        print("processing:",j)
total_error=0
Num=0
for i in d:
    Num+=1
    list1=d[i]
    listAf=[]
    listAh=list1[0:9]
    listAf.append(list1[9])
    listAh=numpy.asarray(listAh) 
    listAf=numpy.asarray(listAf)
    listAf=listAf/32+0.5
    listAh=listAh/32+0.5
    this=flower.query(listAh)
    print((this[0][0]-0.5)*32)
    print(list1[9])
    total_error+=abs(this[0][0]-listAf[0])
print(total_error/Num)
print(flower.error)
f=open("get.txt","w")
get=str(flower.who)+str(flower.wih)
f.write(get)
f.close()



        





# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 03:51:02 2020

@author: Dariswan Janweri
"""
import numpy as np
import random
import csv

#INPUT#
data_path = 'data/example.csv'  #load path's csv dataset
idx_label = 35                  #index column label or class
is_header = False               #True if dataset has header, False without header
n_sample  = 20                  # n sample each cluster or class

#PROCESS SAMPLING#
def take_data():
    collect_data = []
    with open(data_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            collect_data.append(row)
    if(is_header):
        return np.array(collect_data[1:])
    else:
        return np.array(collect_data)

def split_cluster(data):
    classes = np.unique(data[:,idx_label])
    clustered_data=[]
    for i in range(classes.shape[0]):
        clustered_data.append([])
    for i in range(data.shape[0]):
        for j in range(classes.shape[0]):
            if(data[i,idx_label]==classes[j]):
                clustered_data[j].append(data[i])
    return clustered_data

def sampling(data,n):
    sampled_data=[]
    for i in range(len(data)):
        data[i] = random.sample(data[i], n)
        sampled_data.extend(data[i])
    random.shuffle(sampled_data)        #shuffled final sample data
    with open('output/result.csv', "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in sampled_data:
            writer.writerow(line)

data = take_data()
clustered = split_cluster(data)
sampling(clustered,n_sample)
    
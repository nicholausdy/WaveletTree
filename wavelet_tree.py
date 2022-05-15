# Written by: Yosodipuro Nicholaus Danispadmanaba
# For Special Topics in Mechano-Informatics II assignment

import math

class WaveletTree:
    def __init__(self, input_set, max_elem, min_elem):
        self.input_set = input_set
        self.max_elem = max_elem
        self.min_elem = min_elem
        self.sub_arrays_bit_vectors= []
        self.sub_arrays_cum_sum = []

    def create_sub_arrays(self):
        count = self.max_elem - self.min_elem + 1
        num_levels = round(math.log(count, 2))

        for i in range(num_levels):
            num_sub_arrays = 2 ** i
            self.sub_arrays_bit_vectors.append([])
            self.sub_arrays_cum_sum.append([])

            for j in range(num_sub_arrays):
                self.sub_arrays_bit_vectors[i].append([]) 
                self.sub_arrays_cum_sum[i].append([])

    def divide_vectorize(self):
        for i in range(len(self.input_set)):
            self.insert_elem(self.input_set[i])

    def insert_elem(self, elem):
        max_elem = self.max_elem
        min_elem = self.min_elem
        index = 0
        for i in range(len(self.sub_arrays_bit_vectors)):
            cutoff = (max_elem + min_elem) // 2
            if elem <= cutoff:
                elem_vector = 0
                self.sub_arrays_bit_vectors[i][index].append(elem_vector)
                if index == 0:
                    index = 2 ** (index) - 1
                else:
                    index = 2 ** (index)
                max_elem = cutoff
            else:
                elem_vector = 1
                self.sub_arrays_bit_vectors[i][index].append(elem_vector)
                if index == 0:
                    index = 2 ** (index)
                else:
                    index = 2 ** (index) + 1
                min_elem = cutoff + 1

    def create_cum_sum(self):
        for i in range(len(self.sub_arrays_bit_vectors)):
            for j in range(len(self.sub_arrays_bit_vectors[i])):
                count = 0
                for k in range(len(self.sub_arrays_bit_vectors[i][j])):
                    if self.sub_arrays_bit_vectors[i][j][k] == 1:
                        count = count + 1
                    self.sub_arrays_cum_sum[i][j].append(count)
                

    @staticmethod
    def build(input_set, max_elem, min_elem):
        wavelet = WaveletTree(input_set, max_elem, min_elem)
        wavelet.create_sub_arrays()
        wavelet.divide_vectorize()
        wavelet.create_cum_sum()
        return wavelet   

# Test
# input_set = [1,3,6,8,2,5,7,1,7,2,4,5]
# max_elem = 8
# min_elem = 1
# wavelet = WaveletTree.build(input_set, max_elem, min_elem)
# print("Bit vectors:")
# print(wavelet.sub_arrays_bit_vectors)
# print("Cum sum:")
# print(wavelet.sub_arrays_cum_sum)


# Written by: Yosodipuro Nicholaus Danispadmanaba
# For Special Topics in Mechano-Informatics II assignment

# Algorithm for computing MinElem(S,sp,ep) on wavelet trees 
import math
from wavelet_tree import WaveletTree

def min_elem(input_set, input_max_elem, input_min_elem, start_index, end_index):
    wavelet = WaveletTree.build(input_set, input_max_elem, input_min_elem)
    bit_vectors = wavelet.sub_arrays_bit_vectors
    cum_sum = wavelet.sub_arrays_cum_sum
    #
    # print("Bit vectors")
    # print(bit_vectors)
    # print("Cum sum")
    # print(cum_sum)
    sub_array_index = 0
    start_index = start_index
    end_index = end_index
    chosen_index = -99
   
   
    for tree_level in range(len(bit_vectors)):
        count = input_max_elem - input_min_elem + 1 
        num_levels = round(math.log(count, 2))
        # print("Tree levels")
        # print(tree_level)
        # print("Sub array index")
        # print(sub_array_index)
        # print("Start index")
        # print(start_index)
        # print("End index")
        # print(end_index)

        if tree_level != (num_levels - 1): #Check has arrived in leaf or not
        # find whether zeros exist or not
            
            arr_rank_of_zeros = []
            arr_rank_of_ones = []
            is_zero_found = False
            for elem_index in range(start_index, end_index + 1):
                elem = bit_vectors[tree_level][sub_array_index][elem_index]
    
                rank = cum_sum[tree_level][sub_array_index][elem_index]
                if elem == 0:
                    is_zero_found = True
                    rank = elem_index - rank
                    arr_rank_of_zeros.append(rank)
                else:
                    rank = rank - 1
                    arr_rank_of_ones.append(rank)
            # Go to the left child if zero is found
            if is_zero_found:
                if sub_array_index == 0:
                    sub_array_index = 2 ** (sub_array_index) - 1
                else:
                    sub_array_index = 2 ** (sub_array_index) 
                start_index = arr_rank_of_zeros[0]
                end_index = arr_rank_of_zeros[-1]
            # Go to the right child if zero is not found
            else:
                if sub_array_index == 0:
                    sub_array_index = 2 ** (sub_array_index)
                else:
                    sub_array_index = 2 ** (sub_array_index) + 1
                start_index = arr_rank_of_ones[0]
                end_index = arr_rank_of_ones[-1]
            # print("Arr rank of zeros")
            # print(arr_rank_of_zeros)
            # print("Arr rank of ones")
            # print(arr_rank_of_ones)
        else:
            # compare value at leaf
            # standard minimum algorithm
            start_value = bit_vectors[tree_level][sub_array_index][start_index]
            min = start_value
            chosen_index = start_index
            for index in range(start_index + 1, end_index + 1):
                value = bit_vectors[tree_level][sub_array_index][index]
                if value < min:
                    min = value
                    chosen_index = index
            # print("Chosen index")
            # print(chosen_index)

    bit_value = bit_vectors[tree_level][sub_array_index][chosen_index]
    return 2 * sub_array_index + 1 + bit_value


# Test
input_set = [1,3,6,8,2,5,7,1,7,2,4,5]
input_min_elem = 1
input_max_elem = 8

start_index = 4
end_index = 7
value = min_elem(input_set, input_max_elem, input_min_elem, start_index, end_index)
print(value)

            


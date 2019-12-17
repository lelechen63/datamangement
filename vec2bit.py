
import pickle
import numpy as np 
import matplotlib.pyplot as plt

def _vec2bit(vector):
    int_vec = np.where(  vector < -0.3, 0, vector)
    int_vec = np.where( int_vec > 0.3 , 3, int_vec)
    int_vec = np.where((int_vec < 0.3) & (int_vec > 0) , 2,  int_vec)
    int_vec = np.where((int_vec < 0) & (int_vec > -0.3) ,1, int_vec)
    vshape = int_vec.shape
    binary_vec = np.unpackbits(int_vec.astype(np.uint8), axis=1)
    binary_vec = binary_vec.reshape(vshape[0], vshape[1],8)[:,:,-2:]
    binary_vec = binary_vec.reshape(vshape[0], vshape[1] * 2)

def vec2bit(pkl_file):
    _file = open(pkl_file, "rb")
    data = pickle.load(_file)
    max = -1000
    min = 1000
    for d in data:
        print (d)
        vector = np.load( d.replace('json','npy')) 
        # _ = plt.hist(vector, bins='auto') 
        # plt.title("Histogram with 'auto' bins")
        # # plt.show()
        # plt.savefig('./original.png')
        # break

        int_vec = np.where(  vector < -0.3, 0, vector)
        int_vec = np.where( int_vec > 0.3 , 3, int_vec)
        int_vec = np.where((int_vec < 0.3) & (int_vec > 0) , 2,  int_vec)
        int_vec = np.where((int_vec < 0) & (int_vec > -0.3) ,1, int_vec)
        
        
        vshape = int_vec.shape
        # print (vshape)
        # _ = plt.hist(int_vec, bins='auto') 
        # plt.title("Histogram with 'auto' bins")
        # plt.show()

        binary_vec = np.unpackbits(int_vec.astype(np.uint8), axis=1)
        binary_vec = binary_vec.reshape(vshape[0], vshape[1],8)[:,:,-2:]
        binary_vec = binary_vec.reshape(vshape[0], vshape[1] * 2)
        # print (binary_vec[:10,:20])
        
        np.save(d.replace('.json','_binary.npy'), binary_vec)
        # break
    #     print (vector.max(), vector.min())
    #     if vector.max() > max:
    #         max = vector.max()
    #     if vector.min() < min:
    #         min = vector.min()
    #     # break
    # print (max, min)

# vector = np.array([[5,1],[1.5,0],[-2,-4]])
# int_vec = np.where(  vector < -2, 0, vector)
# int_vec = np.where( int_vec > 2 , 3, int_vec)
# int_vec = np.where((int_vec < 2) & (int_vec > 0) , 2,  int_vec)
# int_vec = np.where((int_vec < 0) & (int_vec > -2) ,1, int_vec)
# print (vector)
# print (int_vec)
vec2bit('./pickle/all_file.pkl')

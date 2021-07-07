import sys
import numpy as np
import matplotlib
import purecma_edited as pcmae
import purecma as pcma
from cec17_functions import cec17_test_func

def calculate_function_value(x, function_no):
        f = [0]
        mx = 1
        cec17_test_func(x, f, len(x), mx, function_no)
        return f[0]

def main():
    dimension = int(sys.argv[1])
    function_no = int(sys.argv[2])
    bufflength = int(sys.argv[3])
    maxfevals = 10000 * dimension
    min_x = -100.0
    max_x = 100.0
    iterations = 51
    records = [0.01, 0.02, 0.03, 0.05, 0.1, 0.2,
               0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]      
    error_values = np.zeros([iterations, len(records)])
    for i in range(iterations):
        if bufflength == -1:
            es = pcma.CMAES(list(np.random.uniform(min_x, max_x, dimension)), sigma=0.3 * (max_x - min_x), ftarget=function_no*100 + 1e-8, maxfevals=maxfevals)
        else:
            es = pcmae.CMAES(list(np.random.uniform(min_x, max_x, dimension)), sigma=0.3 * (max_x - min_x), ftarget=function_no*100 + 1e-8, maxfevals=maxfevals, bufflength=bufflength)
        j = 0
        result = 0
        while not es.stop():
            X = es.ask() # get candidate solutions
            f = [calculate_function_value(x, function_no) for x in X] # evaluate solutions
            es.tell(X, f) # do all the real work
            result = es.result[1] # best f-value
            for record in records[j:]:
                if es.counteval >= record * maxfevals:
                    error_values[i][j] = result - function_no * 100
                    j += 1
        if result - function_no * 100 > 1e-8:
            while j < len(records):
                error_values[i][j] = result - function_no * 100
                j += 1
    errors_file = f"{dimension},{function_no},{bufflength}.txt"
    np.savetxt(errors_file, error_values)
    worse = []
    best = []
    mean = []
    median = []
    st_deviation = []
    for i in range(len(records)):
        results = np.sort(error_values[:,i])
        worse.append(results[-1])
        best.append(results[0])
        mean.append(np.mean(results))
        median.append(np.median(results))
        st_deviation.append(np.std(results))
    print(dimension, function_no, bufflength)
    print(worse)
    print(best)
    print(mean)
    print(median)
    print(st_deviation)
    

if __name__ == '__main__':
    main()

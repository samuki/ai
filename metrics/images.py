import numpy as np

def COR(A, B): 
    """Pixel wise correlation between two images 

    Args:
        A (numpy array): input image A
        B (numpy array): input image B 

    Returns:
        float: correlation between images A and B
    """
    mean_A = np.mean(A)
    mean_B = np.mean(B)
    numerator = np.sum(np.multiply(A-mean_A, B-mean_B))
    denominator = np.sqrt(np.sum((A-mean_A)**2))*np.sqrt(np.sum((B-mean_B)**2))
    return numerator/denominator
from sklearn.metrics import confusion_matrix
import numpy as np 

def cohens_kappa(annotation1, annotation2):    
    """Calculate cohens kappa to estimate the agreement between two sets of annotations

    Args:
        annotation1 (list, numpy array): first set of annotations
        annotation2 (list, numpy array): second set of annotations

    Returns:
        float: agreement between both annotations
    """
    cm = confusion_matrix(annotation1, annotation2)
    p_o = (cm[0][0]+cm[1][1])/np.sum(cm)
    p_yes = (cm[0][0]+cm[0][1])/np.sum(cm)* (cm[0][0]+cm[1][0])/np.sum(cm)
    p_no = (cm[1][0]+cm[1][1])/np.sum(cm)* (cm[0][1]+cm[1][1])/np.sum(cm)
    p_e = p_yes+p_no
    kappa = (p_o-p_e)/(1-p_e)
    return kappa
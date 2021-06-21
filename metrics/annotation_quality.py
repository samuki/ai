from sklearn.metrics import confusion_matrix

def cohens_kappa(cm):    
    cm = confusion_matrix(annotations['gold'], annotations['predicted'])
    p_o = (cm[0][0]+cm[1][1])/np.sum(cm)
    p_yes = (cm[0][0]+cm[0][1])/np.sum(cm)* (cm[0][0]+cm[1][0])/np.sum(cm)
    p_no = (cm[1][0]+cm[1][1])/np.sum(cm)* (cm[0][1]+cm[1][1])/np.sum(cm)
    p_e = p_yes+p_no
    kappa = (p_o-p_e)/(1-p_e)
    return kappa
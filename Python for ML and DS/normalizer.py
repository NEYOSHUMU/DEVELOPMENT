def normalize(data=None, mean=None, std=None):
    '''
    Normalization function
    arguments:
             data: the data value you want to normalize
             mean: mean value of your data
             std: standard deviation of your data
    return:
          z-score: normalized value   
    '''
    
    return (data - mean)/ std
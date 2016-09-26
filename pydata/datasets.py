import pandas as pd
import numpy as np
from os.path import join
from os.path import dirname

def load_mnist(split='train'):
    import cPickle
    module_path = dirname(__file__)
    f = open(join(module_path, 'data', 'mnist.pkl'))
    train, val, test = cPickle.load(f)
    f.close()
    meta = {
        'target_labels': range(10),
        'date_acquired': '22-Sep-2016',
        'url': 'http://deeplearning.net/tutorial/gettingstarted.html'
    }
    if (split == 'test'):
        return np.float32(test[0]), np.int8(test[1]), meta
    elif (split == 'val'):
        return np.float32(val[0]), np.int8(val[1]), meta
    else: # return training set by default
        return np.float32(train[0]), np.int8(train[1]), meta

def load_usps(split='train'):
    module_path = dirname(__file__)
    meta = {
            'target_labels': range(10),
            'date_acquired': '22-Sep-2016',
            'url': 'http://www-i6.informatik.rwth-aachen.de/~keysers/usps.html'
    }
    if (split == 'test'):
        digits = pd.read_csv(join(module_path, 'data', 'usps', 'usps_test.csv'), header=None)
        X = digits[range(1,257)].as_matrix()
        y = digits[[0]].as_matrix()
    elif (split == 'train'):
        digits = pd.read_csv(join(module_path, 'data', 'usps', 'usps_train.csv'), header=None)
        X = digits[range(1,257)].as_matrix()
        y = digits[[0]].as_matrix()
    else:
        digits1 = pd.read_csv(join(module_path, 'data', 'usps', 'usps_train.csv'), header=None)
        digits2 = pd.read_csv(join(module_path, 'data', 'usps', 'usps_test.csv'), header=None)
        X = np.vstack((digits1[range(1,257)].as_matrix(), digits2[range(1,257)].as_matrix()))
        y = np.vstack((digits1[[0]].as_matrix(), digits2[[0]].as_matrix()))
    return np.float32(X), np.int8(y), meta

def load_forest_cover():
    module_path = dirname(__file__)
    data = pd.read_csv(join(module_path, 'data', 'forest_cover_data.csv'), header=None)
    meta = {
            'feature_names':['Elevation', 'Aspect', 'Slope', 'Horizontal_Distance_To_Hydrology',
                             'Vertical_Distance_To_Hydrology', 'Horizontal_Distance_To_Roadways',
                             'Hillshade_9am', 'Hillshade_Noon', 'Hillshade_3pm',
                             'Horizontal_Distance_To_Fire_Points']
                            +['Wilderness_Area_{}'.format(i) for i in range(4)]  # 4 binary cols
                            +['Soil_Type_{}'.format(i) for i in range(40)],      # 40 binary cols
            'target_labels':['Spruce/Fir', 'Lodgepole Pine',
                             'Ponderosa Pine', 'Cottonwood/Willow',
                             'Aspen', 'Douglas-Fir', 'Krummholz'],
            'date_acquired': '22-Sep-2016',
            'url': 'https://archive.ics.uci.edu/ml/datasets/Covertype'
    }
    X = data[range(54)].as_matrix()
    y = data[[54]].as_matrix()-1 # output lies in {0,1,2,3,4,5,6}
    return np.float32(X), np.int8(y), meta

def load_letters():
    module_path = dirname(__file__)
    letters = pd.read_csv(join(module_path, 'data', 'letter_data.csv'), header=None)
    meta = {
            'feature_names': ['x-box', 'y-box', 'width', 'high',
                              'onpix', 'x-bar', 'y-bar', 'x2bar',
                              'y2bar', 'xybar', 'x2ybr', 'xy2br',
                              'x-ege', 'xegvy', 'y-ege', 'yegvx'],
            'target_labels': [chr(ord('A')+i) for i in range(26)],
            'date_acquired': '22-Sep-2016',
            'url': 'https://archive.ics.uci.edu/ml/datasets/Letter+Recognition'
    }
    X = letters[range(1,17)].as_matrix()
    y = letters[[0]].applymap(lambda x: ord(x)-ord('A')).as_matrix()
    return np.float32(X), np.int8(y), meta

def load_magic04():
    module_path = dirname(__file__)
    magic = pd.read_csv(join(module_path, 'data', 'magic04_data.csv'), header=None)
    meta = {
            'feature_names': ['Length', 'Width', 'Size', 'Conc',
                              'Conc1', 'Asym', 'M3Long', 'M3Trans',
                              'Alpha', 'Dist'],
            'target_labels': ['gamma', 'hadron'],
            'date_acquired': '22-Sep-2016',
            'url': 'https://archive.ics.uci.edu/ml/datasets/MAGIC+Gamma+Telescope'
    }
    X = magic[range(10)].as_matrix()
    def tf(x):
        if x == 'g': return 0
        else: return 1
    y = magic[[10]].applymap(tf).as_matrix()
    return np.float32(X), np.int8(y), meta

def load_banana():
    module_path = dirname(__file__)
    banana = pd.read_csv(join(module_path, 'data', 'banana_data.csv'), header=None)
    X = banana[[1,2]].as_matrix()
    y = banana[[0]].as_matrix()
    meta = {
            'feature_names': ['x1', 'x2'],
            'date_acquired': '22-Sep-2016',
            'url': 'http://mldata.org/repository/data/viewslug/banana-ida/'
    }
    return np.float32(X), np.int8(y), meta

def load_cifar10(split='train'):
    """Loads the cifar10 dataset. Test/train splits can be chosen
       using the parameter split.
       'all'   => load complete dataset
       'test'  => load test split
       'train' => load train split
    """

    def unpickle(file):
        import cPickle
        fo = open(file, 'rb')
        dict = cPickle.load(fo)
        fo.close()
        return dict

    module_path = dirname(__file__)
    meta = {
        'target_labels': ['airplane', 'automobile', 'bird',
                          'cat', 'deer', 'dog', 'frog',
                          'horse', 'ship', 'truck'],
        'date_acquired': '22-Sep-2016',
        'url': 'http://www.cs.toronto.edu/~kriz/cifar.html'
    }

    if (split == 'test'): # test
        f = unpickle(join(module_path, 'data', 'cifar10', 'test_batch'))
        meta['filenames'] = f['filenames']
        return np.float32(f['data']), np.int8(f['labels']), meta
    else:  # train / all
        for i in range(1,6): # train
            f = unpickle(join(module_path, 'data', 'cifar10', 'data_batch_{}'.format(i)))
            if i == 1:
                data = f['data']
                labels = f['labels']
                filenames = f['filenames']
            else:
                data = np.vstack((data,f['data']))
                labels = np.hstack((labels,f['labels']))
                filenames += f['filenames']
        if (split != 'train'): # all
            f = unpickle(join(module_path, 'data', 'cifar10', 'test_batch'))
            data = np.vstack((data,f['data']))
            labels = np.hstack((labels,f['labels']))
            filenames += f['filenames']
        meta['filenames'] = filenames
        return np.float32(data), np.int8(labels), meta


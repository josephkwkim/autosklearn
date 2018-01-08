from .base import classifier as cl
from .base import regressor as reg

def classifier(x_train, x_test, y_train, y_test):
    return cl(x_train, x_test, y_train, y_test)

def regressor(x_train, x_test, y_train, y_test):
    return reg(x_train, x_test, y_train, y_test)

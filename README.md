# **autosklearn**
#### Automated selection of the best scikit-learn model for your data.

To install, download this repo and move it to `site-packages` folder within your python 3 distribution.  (Anaconda3 etc.)

This library only has support for supervised learning (regression, classification) at the moment. To run regression models, use the following commands:
```
from autosklearn.supervised import regressor
# your code here
results = regressor(x_train, x_test, y_train, y_test)
# results will be initialized as pandas Series object.
```
For classification:
```
from autosklearn.supervised import classifier
# your code here
results = classifier(x_train, x_test, y_train, y_test)
# results will be initialized as a pandas Series object.
```

Dependencies:
- scikit-learn
- numpy
- pandas

This should be compatable for mac, windows, and unix but has only been tested on windows.


*Disclaimer:*
*This library is not very actively maintained and is more a proof-of-concept than a legitimate library meant for public distribution.  It is meant as a useful tool for myself but the code is not very well maintained or documented.*

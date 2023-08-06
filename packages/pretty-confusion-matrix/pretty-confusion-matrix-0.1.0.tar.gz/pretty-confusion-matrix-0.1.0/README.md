# Confusion Matrix in Python
Plot a pretty confusion matrix (like Matlab) in python using seaborn and matplotlib


Created on Mon Jun 25 14:17:37 2018
@author: Wagner Cipriano - wagnerbhbr


This module get a pretty print confusion matrix from a NumPy matrix or from 2 NumPy arrays (`y_test` and `predictions`).

Examples:
```python
array = np.array( [[13,  0,  1,  0,  2,  0],
                  [ 0, 50,  2,  0, 10,  0],
                  [ 0, 13, 16,  0,  0,  3],
                  [ 0,  0,  0, 13,  1,  0],
                  [ 0, 40,  0,  1, 15,  0],
                  [ 0,  0,  0,  0,  0, 20]])
#get pandas dataframe
df_cm = DataFrame(array, index=range(1,7), columns=range(1,7))
#colormap: see this and choose your more dear
cmap = 'PuRd'
pretty_plot_confusion_matrix(df_cm, cmap=cmap)
```
![alt text](https://raw.githubusercontent.com/khuyentran1401/pretty-print-confusion-matrix/master/Screenshots/Conf_matrix_default.png)

```python
y_test = np.array([1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5])

predic = np.array([1,2,4,3,5, 1,2,4,3,5, 1,2,3,4,4, 1,4,3,4,5, 1,2,4,4,5, 1,2,4,4,5, 1,2,4,4,5, 1,2,4,4,5, 1,2,3,3,5, 1,2,3,3,5, 1,2,3,4,4, 1,2,3,4,1, 1,2,3,4,1, 1,2,3,4,1, 1,2,4,4,5, 1,2,4,4,5, 1,2,4,4,5, 1,2,4,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5, 1,2,3,4,5])
"""
Examples to validate output (confusion matrix plot)
   actual: 5 and prediction 1   >>  3
   actual: 2 and prediction 4   >>  1
   actual: 3 and prediction 4   >>  10
"""
columns = []
annot = True;
cmap = 'Oranges';
fmt = '.2f'
lw = 0.5
cbar = False
show_null_values = 2
pred_val_axis = 'y'
#size::
fz = 12;
figsize = [9,9];
if(len(y_test) > 10):
   fz=9; figsize=[14,14];
plot_confusion_matrix_from_data(y_test, predic, columns,
annot, cmap, fmt, fz, lw, cbar, figsize, show_null_values, pred_val_axis)
```

![alt text](https://raw.githubusercontent.com/khuyentran1401/pretty-print-confusion-matrix/master/Screenshots/Conf_matrix_default_2.png)




REFerences:
1. Mat lab confusion matrix

   https://www.mathworks.com/help/nnet/ref/plotconfusion.html
   
   https://www.mathworks.com/help/examples/nnet/win64/PlotConfusionMatrixUsingCategoricalLabelsExample_02.png

   https://stackoverflow.com/questions/5821125/how-to-plot-confusion-matrix-with-string-axis-rather-than-integer-in-python/51176855#51176855


2. Other Examples in python
  
  a) https://stackoverflow.com/a/51176855/1809554
  
  b) https://www.programcreek.com/python/example/96197/seaborn.heatmap

  c) http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-auto-examples-model-selection-plot-confusion-matrix-py

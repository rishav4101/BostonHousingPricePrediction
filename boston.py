import numpy
from numpy import arange
from numpy import set_printoptions
from matplotlib import pyplot
from pandas import read_csv
from pandas import set_option
#from pandas.tools.plotting import scatter_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler


filename = '/home/rishav/Desktop/MLbasicMODELS/BostonHousing/housing.csv'
names = [' CRIM ', ' ZN ', ' INDUS ', ' CHAS ', ' NOX ', ' RM ', ' AGE ', ' DIS ', ' RAD ', ' TAX ', ' PTRATIO ',
         ' B ', ' LSTAT ', ' MEDV ']
dataset = read_csv('housing.csv', delim_whitespace=True, names=names)

array = dataset.values
X = array[:, 0:13]
Y = array[:, 13]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y,
                                                                test_size=validation_size, random_state=seed)
# Rescaling Data
# scaler = MinMaxScaler(feature_range=(0, 1))
# rX = scaler.fit_transform(X)
# set_printoptions(precision=3)
# print(rX[0:5, :])

# Standardising Data
# scalar = StandardScaler().fit(X)
# rX = scalar.transform(X)
# set_printoptions(precision=3)
# print(rX[0:5, :])

# Test options and evaluation metric
num_folds = 10
seed = 7
scoring = 'neg_mean_squared_error'


# # Spot-Check Algorithms
# models = []
# models.append((' LR ', LinearRegression()))
# models.append((' LASSO ', Lasso()))
# models.append((' EN ', ElasticNet()))
# models.append((' KNN ', KNeighborsRegressor()))
# models.append((' CART ', DecisionTreeRegressor()))
# models.append((' SVR ', SVR()))
# # evaluate each model in turn
# results = []
# names = []
# for name, model in models:
#     kfold = KFold(n_splits=num_folds, random_state=None)
#     cv_results = cross_val_score(
#         model, X_train, Y_train, cv=kfold, scoring=scoring)
#     results.append(cv_results)
#     names.append(name)
#     msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
#     print(msg)

# # Standardize the dataset
# pipelines = []
# pipelines.append((' ScaledLR ', Pipeline([(' Scaler ', StandardScaler()), (' LR ',
#                                                                            LinearRegression())])))
# pipelines.append((' ScaledLASSO ', Pipeline([(' Scaler ', StandardScaler()), (' LASSO ',
#                                                                               Lasso())])))
# pipelines.append((' ScaledEN ', Pipeline([(' Scaler ', StandardScaler()), (' EN ',
#                                                                            ElasticNet())])))
# pipelines.append((' ScaledKNN ', Pipeline([(' Scaler ', StandardScaler()), (' KNN ',
#                                                                             KNeighborsRegressor())])))
# pipelines.append((' ScaledCART ', Pipeline([(' Scaler ', StandardScaler()), (' CART ',
#                                                                              DecisionTreeRegressor())])))
# pipelines.append((' ScaledSVR ', Pipeline(
#     [(' Scaler ', StandardScaler()), (' SVR ', SVR())])))
# results = []
# names = []
# for name, model in pipelines:
#     kfold = KFold(n_splits=num_folds, random_state=seed, shuffle=True)
#     cv_results = cross_val_score(
#         model, X_train, Y_train, cv=kfold, scoring=scoring)
#     results.append(cv_results)
#     names.append(name)
#     msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
#     print(msg)

# # Compare Algorithms
# fig = pyplot.figure()
# fig.suptitle(' Scaled Algorithm Comparison ')
# ax = fig.add_subplot(111)
# pyplot.boxplot(results)
# ax.set_xticklabels(names)
# pyplot.show()


# # KNN Algorithm tuning
# scaler = StandardScaler().fit(X_train)
# rescaledX = scaler.transform(X_train)
# k_values = numpy.array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])
# param_grid = dict(n_neighbors=k_values)
# model = KNeighborsRegressor()
# kfold = KFold(n_splits=num_folds, random_state=None)
# grid = GridSearchCV(estimator=model, param_grid=param_grid,
#                     scoring=scoring, cv=kfold)
# grid_result = grid.fit(rescaledX, Y_train)
# print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
# means = grid_result.cv_results_['mean_test_score']
# stds = grid_result.cv_results_['std_test_score']
# params = grid_result.cv_results_['params']
# for mean, stdev, param in zip(means, stds, params):
#     print("%f (%f) with: %r" % (mean, stdev, param))


# # Another way that we can improve the performance of algorithms on this problem is by using
# # ensemble methods.
# # ensembles
# ensembles = []
# ensembles.append((' ScaledAB ', Pipeline([(' Scaler ', StandardScaler()), (' AB ',
#                                                                            AdaBoostRegressor())])))
# ensembles.append((' ScaledGBM ', Pipeline([(' Scaler ', StandardScaler()), (' GBM ',
#                                                                             GradientBoostingRegressor())])))
# ensembles.append((' ScaledRF ', Pipeline([(' Scaler ', StandardScaler()), (' RF ',
#                                                                            RandomForestRegressor())])))
# ensembles.append((' ScaledET ', Pipeline([(' Scaler ', StandardScaler()), (' ET ',
#                                                                            ExtraTreesRegressor())])))
# results = []
# names = []
# for name, model in ensembles:
#     kfold = KFold(n_splits=num_folds, random_state=None)
#     cv_results = cross_val_score(
#         model, X_train, Y_train, cv=kfold, scoring=scoring)
#     results.append(cv_results)
#     names.append(name)
#     msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
#     print(msg)

# # Compare Algorithms
# fig = pyplot.figure()
# fig.suptitle(' Scaled Ensemble Algorithm Comparison ')
# ax = fig.add_subplot(111)
# pyplot.boxplot(results)
# ax.set_xticklabels(names)
# pyplot.show()

# # Tune scaled GBM
# scaler = StandardScaler().fit(X_train)
# rescaledX = scaler.transform(X_train)
# param_grid = dict(n_estimators=numpy.array(
#     [50, 100, 150, 200, 250, 300, 350, 400]))
# model = ExtraTreesRegressor(random_state=None)
# kfold = KFold(n_splits=num_folds, random_state=None)
# grid = GridSearchCV(estimator=model, param_grid=param_grid,
#                     scoring=scoring, cv=kfold)
# grid_result = grid.fit(rescaledX, Y_train)

# print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
# means = grid_result.cv_results_['mean_test_score']
# stds = grid_result.cv_results_['std_test_score']
# params = grid_result.cv_results_['params']
# for mean, stdev, param in zip(means, stds, params):
#     print("%f (%f) with: %r" % (mean, stdev, param))

# prepare the model
scaler = StandardScaler().fit(X_train)
rescaledX = scaler.transform(X_train)
model = GradientBoostingRegressor(random_state=seed, n_estimators=400)
model.fit(rescaledX, Y_train)
# transform the validation dataset
rescaledValidationX = scaler.transform(X_validation)
predictions = model.predict(rescaledValidationX)
print(mean_squared_error(Y_validation, predictions))
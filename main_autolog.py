from src import io_data, viz, modelling, preprocessing, dataprep
from src.preprocessing import Preprocessor
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from mlflow.tracking import MlflowClient
import mlflow
import warnings
warnings.filterwarnings("ignore")
 
def main_autolog():
    # Load data
    df = io_data.load_data("datasetchurn.csv")
 
    # Data prep
    df = dataprep.data_preparation(df.copy())
 
    # Preprocessing
    ## Train test split
    X_train, X_test, y_train, y_test = preprocessing.split_data(df)
 
    ## encoding and imputing
    preprocessor = Preprocessor()
    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.fit_transform(X_test)
 
    # init MLflow
    mlflow_tracking_uri = "file:///C:/Users/vjesequel/Documents/vj_training_albus/mlruns"
    experiment_name = 'autolog_experiment'
    mlflow.set_tracking_uri(mlflow_tracking_uri)
    experiment = MlflowClient().get_experiment_by_name(experiment_name)
    exp_id = experiment.experiment_id if experiment else MlflowClient().create_experiment(experiment_name)
 
    # mlflow autolog: autolog autorisation
    mlflow.sklearn.autolog()
 
    with mlflow.start_run(experiment_id=exp_id, run_name='auto_log') as run:
        # defining parameter range
        param_grid = {'C': [0.1, 1, 10, 100], 
                    'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
                    'gamma':['scale', 'auto'],
                    'kernel': ['linear']} 
         
        grid = GridSearchCV(SVC(), param_grid, refit = True, verbose = 3, n_jobs=-1)
         
        # fitting the model for grid search
        grid.fit(X_train, y_train) 
         
        # print best parameter after tuning
        print(grid.best_params_)
        grid_predictions = grid.predict(X_test)
         
        # print classification report
        print(classification_report(y_test, grid_predictions))  
 
if __name__ == '__main__':
    main_autolog()
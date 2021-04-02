from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def get_model_metrics(model, X, y):
    """
        Separate data in train and test sets,
        fit the model,
        make predictions on train and test datas,
        print metrics

        params:
            model(function): model used with params (ie: Lasso(alpha=x)) 
            X(DataFrame): DataFrame subset with selected features,
            y(Series): variable to predict

        returns: 
                print β1, β0, R2 and RMSE
    """
    # Split des datas
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=0.8, random_state=1
    )
    model.fit(X_train, y_train)
    # Affichage des β1 pour chaque variable
    for idx, name in enumerate(X_train.columns):
        print(f"β1 de {name} : {round(model.coef_[idx], 3)}")

    print(f"β0 (intercept_) : {round(model.intercept_, 3)}\n")

    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    y_list = [y_train, y_train_pred, y_test, y_test_pred]
    get_r2_rmse(y_list)


def get_r2_rmse(y_list):
    """
        calculate R2 and RMSE for each sets (train and test)
        and format output

        param:
            y_list = [
                y_train, 
                y_train_pred, 
                y_test, 
                y_test_pred
            ]
    """

    sets = ["Training", "Testing "]
    i = 0
    for set in sets:
        r2 = round(r2_score(y_list[i], y_list[i+1]), 3)
        rmse = round(mean_squared_error(
            y_list[i], y_list[i+1], squared=False), 3)
        print(
            "{} set : R2 = {}, RMSE = {}".format(set, r2, rmse)
        )
        i += 2

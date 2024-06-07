import pandas as pd
import numpy as np
import random
import torch
from sklearn.preprocessing import StandardScaler, MultiLabelBinarizer
import sklearn.metrics as metrics
import matplotlib.pyplot as plt


def prepare_final(final_df: pd.DataFrame) -> pd.DataFrame:
    final_df.drop(columns=['user_id'], inplace=True)

    mlb = MultiLabelBinarizer()
    encoded_genres = pd.DataFrame(mlb.fit_transform(final_df['favourite_genres']), columns=mlb.classes_, index=final_df.index)
    final_df = pd.concat([final_df.drop('favourite_genres', axis=1), encoded_genres], axis=1)

    numeric_columns = final_df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    scaler = StandardScaler()
    final_df[numeric_columns] = scaler.fit_transform(final_df[numeric_columns])

    return final_df


def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def show_metrics(y_test, y_pred, y_pred_proba):
    accuracy = metrics.accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy:.4f}')

    roc_auc = metrics.roc_auc_score(y_test, y_pred_proba)
    print(f'ROC AUC: {roc_auc:.4f}')

    precision = metrics.precision_score(y_test, y_pred)
    print(f'Precision: {precision:.4f}')

    recall = metrics.recall_score(y_test, y_pred)
    print(f'Recall: {recall:.4f}')

    f1 = metrics.f1_score(y_test, y_pred)
    print(f'F1 Score: {f1:.4f}')

    cm = metrics.confusion_matrix(y_test, y_pred)
    disp = metrics.ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.show()

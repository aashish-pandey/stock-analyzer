from sklearn.ensemble import RandomForestClassifier
from app.models.base import generate_target, get_feature_target

def train(df):
    df = generate_target(df)
    X_train, X_test, y_train, y_test = get_feature_target(df)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    return model, accuracy
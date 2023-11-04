import joblib
modelo = joblib.load('randomforest.pkl')
DatosUsuario = 'data to use as input'
predicciones = modelo.predict([DatosUsuario])
for prediccion in predicciones:
    print("Predicción:", prediccion)
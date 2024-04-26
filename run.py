import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Datos del titanic")
st.header("Luis Edgar Ramirez Perez")

file_path = 'Titanic.csv'
df = pd.read_csv(file_path)
st.dataframe(df)

# Primera gráfica
fig, ax = plt.subplots()
ax.hist(df["Fare"])
st.header("Histograma del Titanic")
st.pyplot(fig)

# Segunda gráfica
fig2, ax2 = plt.subplots()

y_pos = df['Pclass']
x_pos = df['Fare']

ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Class")
ax2.set_xlabel("Fare")
ax2.set_title('¿Cuanto pagaron las clases del Titanic')

st.header("Gráfica de Barras del Titanic")
st.pyplot(fig2)

# Tercera gráfica
fig3, ax3 = plt.subplots()

ax3.scatter(df["Age"], df["Fare"])
ax3.set_xlabel("Edad")
ax3.set_ylabel("Tarifa")

st.header("Gráfica de Dispersión del Titanic")
st.pyplot(fig3)

# Cuarta gráfica
fig4, ax4 = plt.subplots()
ax4 = df.boxplot(["Age"])
ax4.set_ylabel("Tarifa")
st.header("Gráfica de cajas por Edad")
st.pyplot(fig4)


#quinta
fig5, ax5 = plt.subplots()
hist_class = np.histogram(df["Pclass"], bins=3, range=(1,3))[0]


labels = ['1', '2', '3']
colors = ['tab:red', 'tab:green', 'tab:blue']
explode = [0, 0, 0.2]

ax5.pie(hist_class,
        labels = labels,
        colors = colors,
        autopct='%.0f%%',
        explode = explode,
        shadow = True)
st.header("Gráfica de pastel - Clase social")
st.pyplot(fig5)
st.dataframe(hist_class)
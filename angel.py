import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st

from PIL import Image
image = Image.open('logo.jpg')
st.image(image, caption='SPACEX EMPLOYEES')

employee = pd.read_csv("kpis.csv")
#employee.info()
employee2 = employee[["name_employee","birth_date","age","gender","marital_status","hiring_date","position","salary","performance_score","last_performance_date","average_work_hours","satisfaction_level","absences"]]

#Código que permita desplegar un control para seleccionar el género del empleado.
gender = st.selectbox("Selecciona tu género",employee2["gender"].unique())
st.write("El género seleccionado es: ",gender)

#Código que permita desplegar un control para seleccionar un rango del puntaje de desempeño del empleado.
performance_score = st.expander("Selecciona una calificación", True)
rango = performance_score.slider(

    "Selecciona del rango",

    min_value=float(employee2['performance_score'].min()),

    max_value=float(employee2['performance_score'].max())

)
sub_rango = employee2[(employee2['performance_score'] >= employee2)]

st.write(f"La calificación seleccionada es: {rango}: {sub_rango.shape[0]}")

#Código que permita desplegar un control para seleccionar el estado civil del empleado.
marital_status = st.selectbox("Selecciona un estado civil",employee2["marital_status"].unique())
st.write("El estado civil seleccionado es: ",marital_status)

#Código que permita mostrar un gráfico en donde se visualice la distribución de los puntajes de desempeño.
fig = px.pie(employee2, values="performance_score", names="performance_score",title="Puntajes de Desempeño")
#fig.show()
st.plotly_chart(fig, use_container_width=True)

#Código que permita mostrar un gráfico en donde se visualice el promedio de horas trabajadas por el género del empleado.
fig2 = px.pie(employee2, values="average_work_hours", names="gender", title="Promedio de horas trabajadas por el género del empleado.")
#fig2.show()
st.plotly_chart(fig2, use_container_width=True)

#Código que permita mostrar un gráfico en donde se visualice la relación del promedio de horas trabajadas versus el puntaje de desempeño.
fig4 = px.bar(employee2, x="performance_score", y="average_work_hours", title="Promedio de horas vs puntaje de desempeño")
#fig4.show()
st.plotly_chart(fig, use_container_width=True)

#Código que permita desplegar una conclusión sobre el análisis mostrado en la aplicación web.
st.latex(r'''
        Los gráficos muestran que es un grupo diverso de trabajo, en cuanto a género y edad.
        El promedio de horas trabajadas por puntaje de desempeño muestra que el trabajo en más horas no significa una buena calificación en desempeño
        ''')
import pandas as pd
import streamlit as st
from PIL import Image
import altair as alt
import plotly.express as px


st.set_page_config(layout='wide')
col1, col2 = st.columns([1, 4], gap='small')
##########################################################################################
#•  Código que permita desplegar el logotipo de la empresa en la aplicación web.
logo = Image.open('logo.jpg')
col1.image(logo, width=250)
work = pd.read_csv('kpis.csv')
##########################################################################################
#•  Código que contenga las instrucciones para el despliegue de un título y una breve 
# descripción de la aplicación web.
col2.title('Análisis de desempeño de colaboradores Socialize Your Knowledge')
st.markdown("El presente cuadro de mando proporciona las herramientas gráficas necesarias para"
        "visualizar e interpretar \nlos resultados de los analisis de desempeño de los" 
        "colaboradores de Socialize your Knowledge.")
# st.divider()
##########################################################################################
#•  Código que permita desplegar un control para seleccionar el género del empleado.
gender = st.sidebar.radio('Género', work['gender'].unique())
##########################################################################################
#•  Código que permita desplegar un control para seleccionar un rango del puntaje de desempeño del empleado.
satisfaction_lvl = st.sidebar.slider(
    'Puntaje:',
    min_value=float(work['satisfaction_level'].min()),
    max_value=float(work['satisfaction_level'].max())
    )
##########################################################################################
#•  Código que permita desplegar un control para seleccionar el estado civil del empleado.
marital_status = st.sidebar.radio('Estado civil', work['marital_status'].unique())
##########################################################################################
col3, col4 = st.columns([0.5,0.5], gap='large')


#•  Código que permita mostrar un gráfico en donde se visualice la distribución 
# de los puntajes de desempeño.
col3.header('Puntajes de desempeño')
fig_performance = px.histogram(work, x='performance_score', color='gender')
col3.plotly_chart(fig_performance)
##########################################################################################
#•  Código que permita mostrar un gráfico en donde se visualice el promedio de 
# horas trabajadas por el género del empleado.
col4.header('Prom. Horas trabajadas por género')
fig_avgwork_gender = px.histogram(work, x='gender', y='average_work_hours', 
                                  text_auto=True, histfunc='avg', color='gender')
col4.plotly_chart(fig_avgwork_gender)
##########################################################################################
#•  Código que permita mostrar un gráfico en donde se visualice la edad de los 
# empleados con respecto al salario de los mismo.
col3.header('Edad empleados VS sueldo')
fig_age_salary = px.scatter(
    work,
    x='salary',
    y='age',
    color='gender'
    )
col3.plotly_chart(fig_age_salary)
##########################################################################################
#•  Código que permita mostrar un gráfico en donde se visualice la relación del 
# promedio de horas trabajadas versus el puntaje de desempeño.
col4.header('Horas laboradas VS puntaje desempeño')
fig_avgwork_performance = px.scatter(
    work,
    x='average_work_hours',
    y='performance_score',
    color='gender'
)
col4.plotly_chart(fig_avgwork_performance)
##########################################################################################
#•  Código que permita desplegar una conclusión sobre el análisis mostrado en la aplicación web.
#st.divider()
st.subheader('Conclusión')
st.markdown('De acuerdo al análisis presentado se deduce que alrededor del 70% de los colaboradores'
            ' tiene un puntaje satisfactorio con una relacíon promedio entre genero masculino y'
            ' femenino de 40/60 respectivamente.\n\nLa normativa de equidad de genero se mantiene'
            ' estable manteniendo una relación casi de 50/50.\n\nNo existe relación marcada entre'
            ' la edad de los colaboradores y su sueldo percibido, rondando en su mayoría entre los'
            ' 50k y 100k independientemente de la edad, con un poequeño grupo de empleados entre los'
            ' 40 y 60 años de edad que alcanzó una percepción más alta.\n\nAparentemente el puntaje'
            ' de desempeño tiene relación con la cantidad de horas trabajadas, mejorando su puntaje'
            ' conforme aumenta sus horas laborales.')
# st.divider()
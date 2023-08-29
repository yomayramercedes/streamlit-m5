import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Función que lee el archivo
@st.cache
def data(filas):
    df=pd.read_csv("Employees.csv").head(filas)
    return df

#Funcion que busca empleados
@st.cache
def buscarEmployee(empleados):
    dfEmployee = df[df['Employee_ID'].str.upper().str.contains(empleados)]
    return dfEmployee

#Funcion que busca por ciudad
@st.cache
def buscarCiudad(empleados):
    dfCiudad = df[df['Hometown'].str.upper().str.contains(empleados)]
    return dfCiudad

#Funcion que busca por unidad
@st.cache
def buscarUnit(empleados):
    dfUnint = df[df['Unit'].str.upper().str.contains(empleados)]
    return dfUnint

#Recupera 500 lineas del archivo
df = data(500)

#Titulos de la aplicación
st.title("Reto DSAI-M5 - Yomayra Mercedes")
st.header("Analisis deserción empleados")

#Crea el sidebar
sidebar = st.sidebar
sidebar.title("Filtrar empleados")
if sidebar.checkbox("Mostrar todos los empleados"):
    cantidad_registros = "cantidad de registros :" + str((len(df.index)))    
    st.write(cantidad_registros)
    st.write(df)

input_employeeid = st.sidebar.text_input('Ingrese ID: ')
btn_employeeid = st.sidebar.button('Buscar')

if btn_employeeid:
    dfBusqueda = buscarEmployee(input_employeeid.upper())
    cantidad_empleados = "cantidad de registros :" + str((len(dfBusqueda.index)))
    st.write(cantidad_empleados)
    st.write(dfBusqueda)

input_hometown = st.sidebar.text_input('Ingrese ciudad: ')
btn_ciudad = st.sidebar.button('Buscar por ciudad')

if btn_ciudad:
    dfBusqueda = buscarCiudad(input_hometown.upper())
    cantidad_hometown = "cantidad de empleados por ciudad :" + str((len(dfBusqueda.index)))
    st.write(cantidad_hometown)
    st.write(dfBusqueda)

input_unit = st.sidebar.text_input('Ingrese unindad: ')
btn_unit = st.sidebar.button('Buscar por unidad')

if btn_unit:
    dfBusqueda = buscarUnit(input_unit.upper())
    cantidad_unit = "cantidad de empleados por unidad :" + str((len(dfBusqueda.index)))
    st.write(cantidad_unit)
    st.write(dfBusqueda)

selected_box = st.sidebar.selectbox('Ciudades', df['Hometown'].unique())
btn_ciudad_selected = st.sidebar.button('Seleccionar ciudad')

if btn_ciudad_selected:
    dfBusqueda = buscarCiudad(selected_box.upper())
    cantidad_hometown = "cantidad de empleados por ciudad :" + str((len(dfBusqueda.index)))
    st.write(cantidad_hometown)
    st.write(dfBusqueda)

selected_box_unit = st.sidebar.selectbox('Unidad', df['Unit'].unique())
btn_unit_selected = st.sidebar.button('Seleccionar Unidad')

if btn_unit_selected:
    dfBusqueda = buscarUnit(selected_box_unit.upper())
    cantidad_unit = "cantidad de empleados por unidad :" + str((len(dfBusqueda.index)))
    st.write(cantidad_unit)
    st.write(dfBusqueda)

st.markdown("___")
# Empleados por edad
df_edad = df.groupby(["Age"]).sum().reset_index()
fig, ax = plt.subplots()
ax.hist(df.Age)
st.header("Histograma de empleados por edad")
st.pyplot(fig)

#Empleados por unidad
st.markdown("___")
fig3, ax3 = plt.subplots()
ax3.scatter(df.Age, df.Unit)
ax3.set_xlabel("Edad")
ax3.set_ylabel("Unidad")
st.header("Grafica de frecuencia")
st.pyplot(fig3)

st.markdown("___")

#Ciudades con mayor indice de deserción
fig2, ax2 = plt.subplots()
y_pos = df['Hometown']
x_pos = df['Attrition_rate']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Ciudad")
ax2.set_xlabel("Indice deserción")
ax2.set_title('Indice de deserción')
st.header("Grafica de Barras - La ciudad con mayor indice de deserción es Clinton")
st.pyplot(fig2)

#Relación indice de desercion según la edad
st.markdown("___")
fig3, ax3 = plt.subplots()
y_pos = df['Age']
x_pos = df['Attrition_rate']
ax3.bar(y_pos, x_pos )
ax3.set_xlabel("Edad")
ax3.set_ylabel("Indice")
ax3.set_title('Indice deserción segun edad')
st.header("La edad con mayor cantidad de desercion es entre 20 y 40")
st.pyplot(fig3)

#Relación tiempo de servicio y deserción
st.markdown("___")
fig4, ax4 = plt.subplots()
x_pos = df['Time_of_service']
y_pos = df['Attrition_rate']
ax4.bar(x_pos, y_pos )
ax4.set_xlabel("Años de servicio")
ax4.set_ylabel("Indice deserción")
ax4.set_title('Relación tiempo servicio - deserción')
st.header("El nivel de deserción es mas bajo despues de 30 años de servicio")
st.pyplot(fig4)



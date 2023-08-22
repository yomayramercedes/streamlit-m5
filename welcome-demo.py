import streamlit as st 

# return a welcome message
def bienvenida(nombre):
  mymensaje = 'bienvenido/a :' + nombre
  return mymensaje

# read name
myname = st.text_input('nombre :')

if (myname):
  # call function with myname parameter  
  mensaje = bienvenida(myname)
  st.write(f" {mensaje}")
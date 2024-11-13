import streamlit as st
import numpy as np
import pandas as pd
import random as rd
from Class_Preguntas import Questionary, preguntas
from Class_Teoria import Theory, conceptuales
from Imagenes import *

# Importaciones actualizadas
from supabase import create_client, Client
import os
from datetime import datetime
import json
import plotly.express as px

#=========================Configuración de la página============================
st.set_page_config(layout="wide")

#Versión final para esconder el menú y stToolbar 
hide_streamlit_style = """
<style>
    #MainMenu {display: none;}
    [data-testid="stToolbar"] {display: none;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#División de página
col_1, col_2, col_3 = st.columns(3)

#Leer credenciales de usuarios y crear un diccionario
datos_usuarios = pd.read_excel("./Usuarios.xlsx")
datos_usuarios["username"] = datos_usuarios["username"].astype(str)
datos_usuarios["password"] = datos_usuarios["password"].astype(str)
users_credentials = pd.Series(datos_usuarios.password.values, index=datos_usuarios.username).to_dict()

# Configuración de Supabase
SUPABASE_URL="https://iogbgaiiwwfmrontssoi.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlvZ2JnYWlpd3dmbXJvbnRzc29pIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjUzMjU4MTcsImV4cCI6MjA0MDkwMTgxN30.8H8qeLO_qHFuBU7Il5zw9UFCO0Ixr1jHWY7RO3Kweso"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Función para inicializar la base de datos (no es necesaria para Supabase)
def init_db():
    pass

init_db()

# Función para registrar eventos
def log_event(username, event_type, event_data):
    timestamp = datetime.now().isoformat()
    event_data_json = json.dumps(event_data)
    
    data = {
        "username": username,
        "timestamp": timestamp,
        "event_type": event_type,
        "event_data": event_data_json
    }
    
    response = supabase.table("user_events").insert(data).execute()
    
    if hasattr(response, 'error') and response.error:
        print(f"Error logging event: {response.error}")

# Función para obtener el consentimiento del usuario
def get_user_consent():
    consent = st.checkbox("Acepto el seguimiento anónimo de actividad para mejorar la aplicación", value=True)
    
    if "consent" not in st.session_state:
        st.session_state["consent"] = consent

    if "authenticated" in st.session_state and st.session_state["authenticated"]:
        username = st.session_state.get("username", "unknown_user")
        if consent:
            log_event(username, "consent_given", {"type": "activity_tracking"})
    
    return consent

if "user" not in st.session_state:
    st.session_state["user"] = "" 
if "passwd" not in st.session_state:
    st.session_state["passwd"] = "" 
    
username = st.session_state["user"].strip()
password = st.session_state["passwd"].strip()


#Función para verificar credenciales
def creds_entered():   
    
    if username in users_credentials and users_credentials[username] == password:
        st.session_state["authenticated"] = True
        st.session_state["username"] = username
        st.success("Inicio de sesión exitoso")
        log_event(username, "login_successful", {})
        st.rerun()
    else:
        st.error("Usuario o contraseña incorrectos")
        log_event(username, "login_failed", {})

#Función para generar un formulario para verificar usuario    
def authenticate_user():
    with col_2:
        if "authenticated" not in st.session_state:
            st.markdown(
            """
            <style>
            .title {
                display: flex;
                justify-content: center;
                font-size: 2.5em;
                margin: 0;
            }
            </style>
            <div class="title">
                <h1>StaticGenius</h1>
            </div>
            """,unsafe_allow_html=True)
            st.markdown(
            """
            <style>
            .header {
                display: flex;
                justify-content: center;
                font-size: 2.0em;
                margin: 0;
            }
            </style>
            <div class="header">
                <h2>Iniciar sesión</h2>
            </div>
            """,unsafe_allow_html=True)
            st.text_input(label="Usuario:", value="", key="user")
            st.text_input(label="Contraseña:", value="", key="passwd", type="password")
            consent = get_user_consent()
            if st.button("Iniciar sesión"):
                if consent:
                   creds_entered()  
                else:
                    st.write("Debe aceptar el seguimiento anónimo de actividad para mejorar la aplicación")     
           
        else:
            if st.session_state["authenticated"]:
                return True
            else:
                st.markdown(
                """
                <style>
                .title {
                    display: flex;
                    justify-content: center;
                    font-size: 2.5em;
                    margin: 0;
                }
                </style>
                <div class="title">
                    <h1>StaticGenius</h1>
                </div>
                """, unsafe_allow_html=True)
                st.markdown(
                """
                <style>
                .header {
                    display: flex;
                    justify-content: center;
                    font-size: 2.0em;
                    margin: 0;
                }
                </style>
                <div class="header">
                    <h2>Iniciar sesión</h2>
                </div>
                """, unsafe_allow_html=True)
                st.text_input(label="Usuario:", value="", key="user")
                st.text_input(label="Contraseña:", value="", key="passwd", type="password")
                consent = get_user_consent()
                if st.button("Iniciar sesión"):
                    if consent:
                       creds_entered()
                    else:
                        st.write("Debe aceptar el seguimiento anónimo de actividad para mejorar la aplicación")
            return False    

def get_user_statistics(username):
    # Study time
    study_time_query = supabase.table("user_events").select("timestamp, event_data").eq("username", username).eq("event_type", "study_time").execute()
    
    # Exercises solved
    exercises_query = supabase.table("user_events").select("timestamp, event_data").eq("username", username).eq("event_type", "answer_submitted").execute()
    
    # Points
    points_query = supabase.table("user_events").select("timestamp, event_data").eq("username", username).eq("event_type", "points_earned").execute()
    
    # Practice options
    options_query = supabase.table("user_events").select("timestamp, event_data").eq("username", username).eq("event_type", "practice_options_selected").execute()
    
    # Process the results and create DataFrames
    study_time_df = pd.DataFrame(study_time_query.data)
    exercises_df = pd.DataFrame(exercises_query.data)
    points_df = pd.DataFrame(points_query.data)
    options_df = pd.DataFrame(options_query.data)
    
    # Convert timestamps to datetime and create date column
    for df in [study_time_df, exercises_df, points_df, options_df]:
        if not df.empty and 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['date'] = df['timestamp'].dt.date
        else:
            # If DataFrame is empty or doesn't have 'timestamp' column, create empty columns
            df['timestamp'] = pd.Series(dtype='datetime64[ns]')
            df['date'] = pd.Series(dtype='object')
    
    # Process study time
    if not study_time_df.empty and 'event_data' in study_time_df.columns:
        study_time_df['total_time'] = study_time_df['event_data'].apply(lambda x: int(json.loads(x)) if x else 0)
        study_time_df = study_time_df.groupby('date')['total_time'].sum().reset_index()
    else:
        study_time_df = pd.DataFrame(columns=['date', 'total_time'])
    
    # Process exercises
    if not exercises_df.empty and 'event_data' in exercises_df.columns:
        exercises_df['event_data'] = exercises_df['event_data'].apply(json.loads)
        exercises_df['is_correct'] = exercises_df['event_data'].apply(lambda x: x.get('is_correct', False))
        exercises_df['question_id'] = exercises_df['event_data'].apply(lambda x: x.get('question_id', None))
        exercises_df = exercises_df.groupby('date').agg({
            'is_correct': ['count', 'sum'],
            'question_id': 'count'
        }).reset_index()
        exercises_df.columns = ['date', 'total', 'correct', 'question_count']
    else:
        exercises_df = pd.DataFrame(columns=['date', 'total', 'correct', 'question_count'])
    
    # Process points
    if not points_df.empty and 'event_data' in points_df.columns:
        points_df['points'] = points_df['event_data'].apply(lambda x: int(json.loads(x)['points']) if x else 0)
        points_df = points_df.groupby('date')['points'].sum().reset_index()
        points_df.columns = ['date', 'total_points']
    else:
        points_df = pd.DataFrame(columns=['date', 'total_points'])
    
    # Process practice options
    if not options_df.empty and 'event_data' in options_df.columns:
        options_df['event_data'] = options_df['event_data'].apply(json.loads)
        options_df['topic'] = options_df['event_data'].apply(lambda x: x.get('topic', None))
        options_df['subtopic'] = options_df['event_data'].apply(lambda x: x.get('subtopic', None))
        options_df['complexity'] = options_df['event_data'].apply(lambda x: x.get('complexity', None))
    else:
        options_df = pd.DataFrame(columns=['date', 'topic', 'subtopic', 'complexity'])
    
    # Combine data for detailed statistics
    detailed_stats = options_df.merge(exercises_df, on='date', how='left')
    detailed_stats = detailed_stats.merge(points_df, on='date', how='left')
    
    # Aggregate detailed statistics
    detailed_stats = detailed_stats.groupby(['topic', 'subtopic', 'complexity']).agg({
        'question_count': 'sum',
        'correct': 'sum',
        'total_points': 'sum'
    }).reset_index()
    
    detailed_stats.columns = ['topic', 'subtopic', 'complexity', 'total_exercises', 'correct_exercises', 'total_points']
    detailed_stats['total_points'] = detailed_stats['total_points'].fillna(0)
    
    return study_time_df, exercises_df, points_df, detailed_stats

def create_topic_subtopic_exercises_chart(detailed_stats):
    # Ensure 'total_exercises' and 'correct_exercises' are numeric
    detailed_stats['total_exercises'] = pd.to_numeric(detailed_stats['total_exercises'], errors='coerce')
    detailed_stats['correct_exercises'] = pd.to_numeric(detailed_stats['correct_exercises'], errors='coerce')
    
    # Fill NaN values with 0
    detailed_stats['total_exercises'] = detailed_stats['total_exercises'].fillna(0)
    detailed_stats['correct_exercises'] = detailed_stats['correct_exercises'].fillna(0)
    
    # Melt the DataFrame to create a "long" format suitable for Plotly Express
    melted_df = pd.melt(detailed_stats, 
                        id_vars=['topic', 'subtopic', 'complexity'],
                        value_vars=['total_exercises', 'correct_exercises'],
                        var_name='exercise_type', 
                        value_name='count')

    fig = px.bar(melted_df, 
                 x='topic', 
                 y='count',
                 color='subtopic', 
                 pattern_shape='exercise_type',
                 facet_row='complexity',
                 title='Ejercicios por Tema, Subtema y Complejidad',
                 labels={'count': 'Número de Ejercicios', 'exercise_type': 'Tipo'})
    
    fig.update_layout(
        xaxis_title='Tema',
        yaxis_title='Número de Ejercicios',
        legend_title='Subtema',
        height=800  # Increase height to accommodate facets
    )
    
    return fig


def create_topic_subtopic_points_chart(detailed_stats):
    # Ensure 'total_points' is numeric
    detailed_stats['total_points'] = pd.to_numeric(detailed_stats['total_points'], errors='coerce')
    
    # Fill NaN values with 0
    detailed_stats['total_points'] = detailed_stats['total_points'].fillna(0)

    fig = px.bar(detailed_stats, 
                 x='topic', 
                 y='total_points',
                 color='subtopic', 
                 facet_row='complexity',
                 title='Puntos Ganados por Tema, Subtema y Complejidad',
                 labels={'total_points': 'Puntos', 'topic': 'Tema'})
    
    fig.update_layout(
        xaxis_title='Tema',
        yaxis_title='Puntos',
        legend_title='Subtema',
        height=800  # Increase height to accommodate facets
    )
    
    return fig

def create_study_time_chart(study_time_df):
    # Convertir la columna 'date' a datetime si no lo está ya
    study_time_df['date'] = pd.to_datetime(study_time_df['date'])
    
    # Formatear la fecha para mostrar solo día, mes y año
    study_time_df['formatted_date'] = study_time_df['date'].dt.strftime('%d-%m-%Y')
    
    fig = px.line(study_time_df, x='formatted_date', y='total_time', title='Tiempo de Estudio Diario')
    fig.update_layout(
        xaxis_title='Fecha',
        yaxis_title='Tiempo de Estudio (minutos)',
        xaxis_tickangle=-45
    )
    return fig

def create_exercises_chart(exercises_df):
    if exercises_df.empty:
        fig = px.bar(title='Ejercicios Resueltos Diariamente')
        fig.update_layout(
            xaxis_title='Fecha',
            yaxis_title='Número de Ejercicios',
            showlegend=False
        )
    else:
        # Convertir la columna 'date' a datetime si no lo está ya
        exercises_df['date'] = pd.to_datetime(exercises_df['date'])
        
        # Formatear la fecha para mostrar solo día, mes y año
        exercises_df['formatted_date'] = exercises_df['date'].dt.strftime('%d-%m-%Y')
        
        # Asegúrate de que las columnas 'correct' y 'total' sean de tipo numérico
        exercises_df['correct'] = pd.to_numeric(exercises_df['correct'], errors='coerce').fillna(0).astype(int)
        exercises_df['total'] = pd.to_numeric(exercises_df['total'], errors='coerce').fillna(0).astype(int)
        
        # Crea el gráfico de barras
        fig = px.bar(
            exercises_df,
            x='formatted_date',
            y=['correct', 'total'],
            title='Ejercicios Resueltos Diariamente',
            labels={'value': 'Número de Ejercicios', 'variable': 'Tipo'},
            barmode='group'
        )
        
        fig.update_layout(
            xaxis_title='Fecha',
            yaxis_title='Número de Ejercicios',
            legend_title='Tipo de Ejercicio',
            xaxis_tickangle=-45,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            )
        )
    
    return fig


def create_topic_statistics_chart(topic_stats):
    fig = px.bar(topic_stats, x='topic', y=['total_exercises', 'correct_exercises', 'total_attempts', 'points'],
                 title='Estadísticas por Tema',
                 labels={'value': 'Cantidad', 'variable': 'Métrica'},
                 barmode='group')
    
    fig.update_layout(
        xaxis_title='Tema',
        yaxis_title='Cantidad',
        legend_title='Métrica',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    return fig

def create_points_chart(points_df):
    # Convertir la columna 'date' a datetime si no lo está ya
    points_df['date'] = pd.to_datetime(points_df['date'])
    
    # Formatear la fecha para mostrar solo día, mes y año
    points_df['formatted_date'] = points_df['date'].dt.strftime('%d-%m-%Y')
    
    fig = px.line(points_df, x='formatted_date', y='total_points', title='Puntos Ganados Diariamente')
    fig.update_layout(
        xaxis_title='Fecha',
        yaxis_title='Puntos',
        xaxis_tickangle=-45
    )
    return fig

def calculate_total_statistics(study_time_df, exercises_df, points_df):
    total_study_time = study_time_df['total_time'].sum() if 'total_time' in study_time_df.columns else 0
    total_exercises = exercises_df['total'].sum() if 'total' in exercises_df.columns else 0
    total_correct = exercises_df['correct'].sum() if 'correct' in exercises_df.columns else 0
    total_points = points_df['total_points'].sum() if 'total_points' in points_df.columns else 0
    
    return {
        'total_study_time': total_study_time,
        'total_exercises': total_exercises,
        'total_correct': total_correct,
        'total_points': total_points
    }

def calculate_points(difficulty, attempts, used_help):
    base_points = {"Fácil": 10, "Medio": 20, "Díficil": 30}
    points = base_points.get(difficulty, 10)
    
    if attempts == 1 and not used_help:
        return points
    elif attempts <= 3:
        return points // 2
    else:
        return points // 3

if authenticate_user():
    consent = st.session_state.consent

    # -------------------------------Inicialización de variables con sesión de estado-----------------------------------------

    # Initialize the "Intento" Variable to Count the Number of User's Attempts to Verify Their Answer
    if 'Intento' not in st.session_state:
        st.session_state.Intento = 0
    # Initialize the State for the "mostrar_respuesta" Function When the User Verifies Their Answer
    if 'mostrar_respuesta' not in st.session_state:
        st.session_state.mostrar_respuesta = False
    # Initialize the questions to show
    if f'pregunta_actual_{username}' not in st.session_state:
        st.session_state[f'pregunta_actual_{username}'] = 0 
    # Initialize the version of the question to show    
    if 'version_actual' not in st.session_state:    
        st.session_state.version_actual = 1
    # Inicializa el método
    if 'way' not in st.session_state:
        st.session_state.way = ""
    # Inicializa el nivel de dificultad
    if 'complexity' not in st.session_state:
        st.session_state.complexity = ""
    # Inicializa el tema
    if 'topic' not in st.session_state:
        st.session_state.topic = ""
    # Inicializa el subtema
    if 'subtopic' not in st.session_state:
        st.session_state.subtopic = ""

    # -------------------------------------------Creación de la barra lateral-------------------------------------
    st.sidebar.markdown("<h1 style='font-size:36px;'>StaticGenius</h1>", unsafe_allow_html=True)
    action = st.sidebar.radio("Seleccione la acción que desa realizar", options = ["Estudiar","Consultar estadísticas"])
    
    respuesta_usuario = {}
    
    if action == "Estudiar":
        way = st.sidebar.radio("Seleccione su método de estudio", options=["Práctica", "Teoría"])
        respuesta_usuario['way'] = way

        if way == "Teoría":
            st.sidebar.header("Teoría")
            topic=st.sidebar.selectbox("Seleccione el tema", options=["Equilibrio de partículas", "Apoyos y reacciones", "Centroides", "Fuerzas distribuidas"])
            respuesta_usuario['topic'] = topic

            if topic == "Equilibrio de partículas":
                subtopic=st.sidebar.selectbox("Seleccione el subtema", options=["Vectores","Equilibrio"])
            #if topic == "Momento":
            #    subtopic=st.sidebar.selectbox("Seleccione el subtema", options=["Momento"])
            if topic == "Apoyos y reacciones":
                subtopic=st.sidebar.selectbox("Seleccione el subtema", options=["Apoyos y reacciones"])
            if topic == "Centroides":
                subtopic=st.sidebar.selectbox("Seleccione el subtema", options=["Centroides"])
            if topic == "Fuerzas distribuidas":
                subtopic=st.sidebar.selectbox("Seleccione el subtema", options=["Vigas", "Presiones hidrostáticas"])

            if consent:
                log_event(st.session_state["username"], "theory_section_accessed", {})
            respuesta_usuario['subtopic'] = subtopic

        else:
            st.sidebar.header("Práctica")
            complexity = st.sidebar.radio("Nivel de dificultad", options=["Fácil", "Medio", "Díficil"])
            topic = st.sidebar.selectbox("Seleccione el tema", options=["Equilibrio de partículas", "Momento", "Sistemas equivalentes", "Armaduras", "Centroides", "Fuerzas distribuidas"])
            
            if topic == "Equilibrio de partículas":
                subtopic = st.sidebar.selectbox("Seleccione el subtema", options=["Vectores 2D", "Vectores 3D", "Vector unitario", "Equilibrio 2D"])
            elif topic=="Momento":
                subtopic = st.sidebar.selectbox("Seleccione el subtema", options=["Momento en un punto 2D"])
            elif topic=="Sistemas equivalentes":
                subtopic = st.sidebar.selectbox("Seleccione el subtema", options=["Sistemas equivalentes"])
            elif topic=="Armaduras":
                subtopic = st.sidebar.selectbox("Seleccione el subtema", options=["Cerchas", "Marcos"])
            elif topic=="Centroides":
                subtopic = st.sidebar.selectbox("Seleccione el subtema", options=["Centroides"])
            elif topic=="Fuerzas distribuidas":
                subtopic = st.sidebar.selectbox("Seleccione el subtema", options=["Fuerzas distribuidas"])

            if consent:
                log_event(st.session_state["username"], "practice_options_selected", {
                    "complexity": complexity,
                    "topic": topic,
                    "subtopic": subtopic
                })

            #Almacenar la selección del usuario
            respuesta_usuario = {'complexity': complexity, 'topic': topic, 'subtopic': subtopic}
    
    elif action == "Consultar estadísticas":
        st.header("Estadísticas de Usuario")
        username = st.session_state.get("username", "unknown_user")
        study_time_df, exercises_df, points_df, detailed_stats = get_user_statistics(username)
        
        # Display total statistics
        total_stats = calculate_total_statistics(study_time_df, exercises_df, points_df)
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Tiempo Total de Estudio", f"{total_stats['total_study_time']} min")
        col2.metric("Ejercicios Totales", total_stats['total_exercises'])
        col3.metric("Ejercicios Correctos", total_stats['total_correct'])
        col4.metric("Puntos Totales", total_stats['total_points'])
        
        # Display overall charts
        st.plotly_chart(create_study_time_chart(study_time_df))
        st.plotly_chart(create_exercises_chart(exercises_df))
        st.plotly_chart(create_points_chart(points_df))
        
        # Display detailed charts
        st.subheader("Estadísticas Detalladas por Tema, Subtema y Complejidad")
        st.plotly_chart(create_topic_subtopic_exercises_chart(detailed_stats))
        st.plotly_chart(create_topic_subtopic_points_chart(detailed_stats))
        
        if consent:
            log_event(username, "statistics_viewed", {})

    
    topic_user = respuesta_usuario.get('topic', None)
    subtopic_user = respuesta_usuario.get('subtopic', None)
    complexity_user = respuesta_usuario.get('complexity', None)  

    # Lista filtrada de preguntas según la selección del usuario
    preguntas_filtradas = Questionary.filtrar_preguntas(preguntas, topic_user, subtopic_user, complexity_user)
    conceptuales_filtradas = Theory.filtrar_preguntas_teoria(conceptuales, topic_user, subtopic_user)        
    #Reinicia el número de la pregunta cuando se cambia de tema, subtema o nivel de dificulta
   # Verificar si se ha cambiado alguna de las opciones
    if action == "Estudiar":
        if way == "Práctica":
            if (st.session_state.way != way or st.session_state.topic != topic or st.session_state.subtopic != subtopic or st.session_state.complexity != complexity):
            # Actualizar el estado de sesión con las nuevas selecciones
                st.session_state.way = way
                st.session_state.topic = topic
                st.session_state.subtopic = subtopic
                st.session_state.complexity = complexity 
                # Reiniciar el número de la pregunta
                st.session_state[f'pregunta_actual_{username}'] = 0
        elif way == "Teoría":
            if (st.session_state.way != way or st.session_state.topic != topic or st.session_state.subtopic != subtopic):
            # Actualizar el estado de sesión con las nuevas selecciones
                st.session_state.way = way
                st.session_state.topic = topic
                st.session_state.subtopic = subtopic
                # Reiniciar el número de la pregunta
                st.session_state[f'pregunta_actual_{username}'] = 0

        #=========================Funciones para generar las preguntas============================

    #Función para crear las cajas para las respuestas del usuario
    def render_input_widgets(preguntas_filtradas, pregunta_actual):
        col1, col2, col3 = st.columns(3)
        if preguntas_filtradas[pregunta_actual].no_answers == 0:
            response1 = 0.0
            response2 = 0.0
            response3 = 0.0
        if preguntas_filtradas[pregunta_actual].no_answers == 1:
            response1 = col1.number_input(f"{preguntas_filtradas[pregunta_actual].a1_name}", key=f"response1_{preguntas_filtradas[pregunta_actual]}", value=0.00)
            response2 = 0.0
            response3 = 0.0
        elif preguntas_filtradas[pregunta_actual].no_answers == 2:
            response1 = col1.number_input(f"{preguntas_filtradas[pregunta_actual].a1_name}", key=f"response1_{preguntas_filtradas[pregunta_actual]}", value=0.00)
            response2 = col2.number_input(f"{preguntas_filtradas[pregunta_actual].a2_name}", key=f"response2_{preguntas_filtradas[pregunta_actual]}", value=0.00)
            response3 = 0.0
        elif preguntas_filtradas[pregunta_actual].no_answers == 3:
            response1 = col1.number_input(f"{preguntas_filtradas[pregunta_actual].a1_name}", key=f"response1_{preguntas_filtradas[pregunta_actual]}", value=0.00)
            response2 = col2.number_input(f"{preguntas_filtradas[pregunta_actual].a2_name}", key=f"response2_{preguntas_filtradas[pregunta_actual]}", value=0.00)
            response3 = col3.number_input(f"{preguntas_filtradas[pregunta_actual].a3_name}", key=f"response3_{preguntas_filtradas[pregunta_actual]}", value=0.00)
        
        return response1, response2, response3

    #Función para evaluar las respuestas del usuario
    def resultado(preguntas_filtradas, response1, response2, response3, pregunta_actual):
        respx1 = preguntas_filtradas[pregunta_actual].answer1
        respx2 = preguntas_filtradas[pregunta_actual].answer2
        respx3 = preguntas_filtradas[pregunta_actual].answer3

        outxt = 'Error'
        cont = 0
        l_error = 0.2
        if preguntas_filtradas[pregunta_actual].no_answers == 1:
            if abs(respx1 - response1) < l_error:
                outxt = 'Felicitaciones!!!! La respuesta es correcta.'
                cont = 1
            else:
                outxt = 'La respuesta no es correcta, presione el boton de "Ayuda", o trate de nuevo.'
        elif preguntas_filtradas[pregunta_actual].no_answers == 2:
            if abs(respx1 - response1) > l_error and abs(respx2 - response2) > l_error:
                outxt = 'Las respuestas no son correctas, presione el boton de "Ayuda", o trate de nuevo.'
            else:
                if abs(respx1 - response1) < l_error and abs(respx2 - response2) < l_error:
                    outxt = 'Felicitaciones!!!! La respuesta es correcta.'
                    cont = 1
                elif abs(respx1 - response1) < l_error and abs(respx2 - response2) > l_error:
                    outxt = 'Solamente la primera respuesta es correcta, presione el boton de "Ayuda", o trate de nuevo.'
                elif abs(respx1 - response1) > l_error and abs(respx2 - response2) < l_error:
                    outxt = 'Solamente la segunda respuesta es correcta, presione el boton de "Ayuda", o trate de nuevo.'
        elif preguntas_filtradas[pregunta_actual].no_answers == 3:
            if abs(respx1 - response1) > l_error and abs(respx2 - response2) > l_error and abs(respx3 - response3) > l_error:
                outxt = 'Las respuestas no son correctas, presione el boton de "Ayuda", o trate de nuevo.'
            else:
                if abs(respx1 - response1) < l_error and abs(respx2 - response2) < l_error and abs(respx3 - response3) < l_error:
                    outxt = 'Felicitaciones!!!! La respuesta es correcta.'
                    cont = 1
                else:
                    correct_answers = []
                    if abs(respx1 - response1) < l_error:
                        correct_answers.append("primera")
                    if abs(respx2 - response2) < l_error:
                        correct_answers.append("segunda")
                    if abs(respx3 - response3) < l_error:
                        correct_answers.append("tercera")
                        
                    if len(correct_answers) == 1:
                        outxt = f'Solamente la {correct_answers[0]} respuesta es correcta, presione el boton de "Ayuda", o trate de nuevo.'
                    elif len(correct_answers) == 2:
                        outxt = f'Solamente la {correct_answers[0]} y la {correct_answers[1]} respuestas son correctas, presione el boton de "Ayuda", o trate de nuevo.'
            
        if st.session_state.get("consent", False):
            log_event(st.session_state["username"], "answer_submitted", {
            "question_id": preguntas_filtradas[pregunta_actual].no_pregunta,
            "version": preguntas_filtradas[pregunta_actual].version,
            "is_correct": cont == 1
            })
            
        return outxt, cont

    #Función para mostrar la imagen de la pregunta
    def filtrar_imagenes_preguntas(pregunta_no, version_no, subtopic, difficulty):
        left_col, center_col, right_col = st.columns(3)
        with center_col:
            if difficulty == "Fácil":
                if subtopic == "Vectores 2D" or subtopic == "Vector unitario":
                    if pregunta_no <= 2: #Vectores 2D y Vector unitario
                        if version_no == 1:
                            st.image(EQ_image_paths[0], width=325) 
                        elif version_no == 2:
                            st.image(EQ_image_paths[1], width=350)
                        elif version_no == 3:
                            st.image(EQ_image_paths[2], width=350)
                        elif version_no == 4:
                            st.image(EQ_image_paths[3], width=350)   
                            
                    elif pregunta_no > 2 and pregunta_no <= 4: #Vectores 2D y Vector unitario
                        if version_no == 1:
                            st.image(EQ_image_paths[4], width=200)
                        elif version_no == 2:
                            st.image(EQ_image_paths[5], width=200)
                        elif version_no == 3:
                            st.image(EQ_image_paths[6], width=200)
                        elif version_no == 4:
                            st.image(EQ_image_paths[7], width=200)
                if subtopic == "Vectores 3D":
                    if pregunta_no == 1 or pregunta_no == 2:
                        if version_no == 1:
                            st.image(EQ_image_paths[29], width=325) 
                        elif version_no == 2:
                            st.image(EQ_image_paths[30], width=350)
                        elif version_no == 3:
                            st.image(EQ_image_paths[31], width=350)
                        elif version_no == 4:
                            st.image(EQ_image_paths[32], width=350)
                    if pregunta_no == 3 or pregunta_no == 4:
                        if version_no == 1:
                            st.image(EQ_image_paths[33], width=325) 
                        elif version_no == 2:
                            st.image(EQ_image_paths[34], width=350)
                        elif version_no == 3:
                            st.image(EQ_image_paths[35], width=350)
                        elif version_no == 4:   
                            st.image(EQ_image_paths[36], width=350) 
                if subtopic == "Equilibrio 2D":
                    if pregunta_no == 1 or pregunta_no == 2:
                        if version_no == 1:
                            st.image(EQ_image_paths[50], width=400) 
                        elif version_no == 2:
                            st.image(EQ_image_paths[51], width=350)
                        elif version_no == 3:
                            st.image(EQ_image_paths[45], width=350)
                        elif version_no == 4:
                            st.image(EQ_image_paths[46], width=350) 
                    if pregunta_no == 3:
                        if version_no == 1:
                            st.image(EQ_image_paths[52], width=250) 
                        elif version_no == 2:
                            st.image(EQ_image_paths[53], width=350)
                        elif version_no == 3:
                            st.image(EQ_image_paths[54], width=350)
                        elif version_no == 4:
                            st.image(EQ_image_paths[55], width=350)  
                    if pregunta_no == 4:
                        if version_no == 1:
                            st.image(EQ_image_paths[56], width=375) 
                        elif version_no == 2:
                            st.image(EQ_image_paths[57], width=350)     
                if subtopic == "Momento en un punto 2D":
                    if pregunta_no == 1 or pregunta_no == 2:
                        if version_no == 1:
                            st.image(MO_image_paths[0], width=600) 
                        elif version_no == 2:
                            st.image(MO_image_paths[1], width=600)
                        elif version_no == 3:
                            st.image(MO_image_paths[2], width=350)
                        elif version_no == 4:
                            st.image(MO_image_paths[3], width=350)
                    if pregunta_no == 3 or pregunta_no == 4:
                        if version_no == 1:
                            st.image(MO_image_paths[4], width=600) 
                        elif version_no == 2:
                            st.image(MO_image_paths[1], width=350)
                        elif version_no == 3:
                            st.image(MO_image_paths[2], width=350)
                        elif version_no == 4:
                            st.image(MO_image_paths[3], width=350)
                if subtopic == "Sistemas equivalentes":
                    if pregunta_no == 1:
                        if version_no == 1:
                            st.image(SE_image_paths[0], width=450) 
                        if version_no == 2:
                            st.image(SE_image_paths[1], width=450) 
                    if pregunta_no == 2:
                        st.image(SE_image_paths[2], width=500)
                    if pregunta_no == 3:
                        st.image(SE_image_paths[3], width=350)
                if subtopic == "Cerchas":
                    if pregunta_no == 1:
                        if version_no == 1:
                            st.image(AR_image_paths[0], width=500) 
                        if version_no == 2:
                            st.image(AR_image_paths[1], width=500)   
                    if pregunta_no == 2:
                        st.image(AR_image_paths[2], width=500)  
                    if pregunta_no == 3:
                        st.image(AR_image_paths[3], width=600) 
                if subtopic == "Marcos":
                    if pregunta_no == 1:
                        st.image(AR_image_paths[10], width=450) 
                    if pregunta_no == 2:
                        st.image(AR_image_paths[11], width=350)
                if subtopic == "Centroides":
                    if pregunta_no == 1:
                        st.image(CT_image_paths[0], width=300) 
                    if pregunta_no == 2:
                        st.image(CT_image_paths[1], width=300)
                    if pregunta_no == 3:
                        st.image(CT_image_paths[2], width=420)
                if subtopic == "Fuerzas distribuidas":
                    if pregunta_no == 1:
                        st.image(FD_image_paths[0], width=450) 
                    if pregunta_no == 2:
                        st.image(FD_image_paths[1], width=400)
                    if pregunta_no == 3:
                        st.image(FD_image_paths[2], width=450)
                    
                
            if difficulty == "Medio":
                if subtopic == "Vectores 2D":
                    if pregunta_no == 1:
                        if version_no == 1:
                            st.image(EQ_image_paths[8], width=250)
                        elif version_no == 2:
                            st.image(EQ_image_paths[9], width=250)
                        elif version_no == 3:
                            st.image(EQ_image_paths[10], width=250)
                        elif version_no == 4:
                            st.image(EQ_image_paths[11], width=250)    
                    if pregunta_no == 2:
                        if version_no == 1:
                            st.image(EQ_image_paths[12], width=300)
                        elif version_no == 2:
                            st.image(EQ_image_paths[13])
                        elif version_no == 3:
                            st.image(EQ_image_paths[14])
                        elif version_no == 4:
                            st.image(EQ_image_paths[15])   
                    if pregunta_no == 3:
                        st.image(EQ_image_paths[16], width=330)
                    if pregunta_no == 4:
                        st.image(EQ_image_paths[17], width=180)
                if subtopic == "Vectores 3D":
                    if pregunta_no == 1 or pregunta_no==2 or pregunta_no == 3:
                        if version_no == 1:
                            st.image(EQ_image_paths[37], width=350)
                        elif version_no == 2:
                            st.image(EQ_image_paths[38], width=350)
                        elif version_no == 3:
                            st.image(EQ_image_paths[39], width=350)
                        elif version_no == 4:
                            st.image(EQ_image_paths[40], width=350) 
                if subtopic == "Vector unitario":
                    if pregunta_no == 1 or pregunta_no == 2:
                        if version_no == 1:
                            st.image(EQ_image_paths[45], width=350)
                        elif version_no == 2:
                            st.image(EQ_image_paths[46], width=350)
                        elif version_no == 3:
                            st.image(EQ_image_paths[47], width=350)
                        elif version_no == 4:
                            st.image(EQ_image_paths[48], width=350) 
                    if pregunta_no == 3 or pregunta_no == 4:
                        st.image(EQ_image_paths[49], width=400)
                if subtopic == "Equilibrio 2D":
                    if pregunta_no == 1:
                        if version_no == 1:
                            st.image(EQ_image_paths[58], width=250) 
                if subtopic == "Momento en un punto 2D":
                    if pregunta_no == 1 or pregunta_no == 2 or pregunta_no == 3 or pregunta_no == 4:
                        if version_no == 1:
                            st.image(MO_image_paths[5], width=500) 
                        elif version_no == 2:
                            st.image(MO_image_paths[6], width=500)
                        elif version_no == 3:
                            st.image(MO_image_paths[7], width=500)
                        elif version_no == 4:
                            st.image(MO_image_paths[8], width=500)
                if subtopic == "Sistemas equivalentes":
                    if pregunta_no == 1:
                        st.image(SE_image_paths[4], width=450)  
                    if pregunta_no == 2:
                        st.image(SE_image_paths[5], width=350)
                if subtopic == "Cerchas":
                    if pregunta_no == 1:
                        st.image(AR_image_paths[4], width=400) 
                    if pregunta_no == 2:
                        st.image(AR_image_paths[5], width=500) 
                    if pregunta_no == 3:
                        st.image(AR_image_paths[6], width=500) 
                    if pregunta_no == 4:
                        st.image(AR_image_paths[7], width=600)   
                if subtopic == "Marcos":
                    if pregunta_no == 1:
                        st.image(AR_image_paths[12], width=550) 
                    if pregunta_no == 2:
                        st.image(AR_image_paths[13], width=400)  
                if subtopic == "Centroides":
                    if pregunta_no == 1:
                        st.image(CT_image_paths[3], width=420)    
                if subtopic == "Fuerzas distribuidas":
                    if pregunta_no == 1:
                        st.image(FD_image_paths[3], width=350)
                    if pregunta_no == 2:
                        st.image(FD_image_paths[4], width=450) 
                    if pregunta_no == 3:
                        st.image(FD_image_paths[5], width=400)    
                
            if difficulty == "Díficil":
                if subtopic == "Vectores 2D":
                    if pregunta_no == 1 or pregunta_no == 2:
                        if version_no == 1:
                            st.image(EQ_image_paths[18], width=350)
                        elif version_no == 2:
                            st.image(EQ_image_paths[19], width=350)
                        elif version_no == 3:
                            st.image(EQ_image_paths[20], width=350)
                        elif version_no == 4:
                            st.image(EQ_image_paths[21], width=350)
                    if pregunta_no == 3:
                        if version_no == 1:
                            st.image(EQ_image_paths[23], width=250)
                        elif version_no == 2:
                            st.image(EQ_image_paths[24], width=250)
                    if pregunta_no == 4:
                        st.image(EQ_image_paths[22], width=350)
                    if pregunta_no == 5:
                        if version_no == 1:
                            st.image(EQ_image_paths[25], width=250)
                        elif version_no == 2:
                            st.image(EQ_image_paths[26], width=250)
                        elif version_no == 3:
                            st.image(EQ_image_paths[27], width=250)
                        elif version_no == 4:
                            st.image(EQ_image_paths[28], width=250)
                if subtopic == "Vectores 3D":
                    if pregunta_no == 1 or pregunta_no == 2 or pregunta_no == 3:
                        if version_no == 1:
                            st.image(EQ_image_paths[41], width=400)
                        elif version_no == 2:
                            st.image(EQ_image_paths[41], width=400)
                        elif version_no == 3:
                            st.image(EQ_image_paths[43], width=400)
                        elif version_no == 4:
                            st.image(EQ_image_paths[44], width=400)
                if subtopic == "Vector unitario":
                    if pregunta_no == 1 or pregunta_no == 2 or pregunta_no == 3:
                        st.image(EQ_image_paths[49], width=400)
                if subtopic == "Momento en un punto 2D":
                    if pregunta_no == 1 or pregunta_no == 2: 
                        if version_no == 1:
                            st.image(MO_image_paths[9], width=550) 
                        elif version_no == 2:
                            st.image(MO_image_paths[10], width=550)
                        elif version_no == 3:
                            st.image(MO_image_paths[11], width=550)
                if subtopic == "Sistemas equivalentes":
                    if pregunta_no == 1:
                        st.image(SE_image_paths[6], width=450) 
                if subtopic == "Cerchas":
                    if pregunta_no == 1:
                        st.image(AR_image_paths[8], width=500)
                    if pregunta_no == 2:
                        st.image(AR_image_paths[9], width=350) 
                if subtopic == "Marcos":
                    if pregunta_no == 1:
                        st.image(AR_image_paths[14], width=500) 
                    if pregunta_no == 2:
                        st.image(AR_image_paths[15], width=400)
                if subtopic == "Centroides":
                    if pregunta_no == 1:
                        st.image(CT_image_paths[5], width=500) 
                    if pregunta_no == 2:
                        st.image(CT_image_paths[6], width=500) 
                            
        return

    #Función para mostrar la imagen de la respuesta
    def filtrar_imagenes_respuestas_P1(pregunta_no, version_no, subtopic, difficulty):
        left_col, center_col, right_col = st.columns(3)

        with left_col:
            if difficulty == "Fácil":
                if subtopic == "Equilibrio 2D":
                    if pregunta_no == 3:
                        st.image(EQ_rtas_paths[9], width=250)
                    if pregunta_no == 4:
                        st.image(EQ_rtas_paths[10], width=350)
                if subtopic == "Centroides":
                    if pregunta_no ==1:
                        st.image(CT_rtas_paths[0], width=200)
                if subtopic == "Fuerzas distribuidas":
                    if pregunta_no ==1:
                        st.image(FD_rtas_paths[0], width=350)
                    if pregunta_no ==2:
                        st.image(FD_rtas_paths[1], width=350)
                    if pregunta_no ==3:
                        st.image(FD_rtas_paths[3], width=350)
                    
            if difficulty == "Medio":
                if subtopic == "Equilibrio 2D":
                    if pregunta_no == 1:
                        st.image(EQ_rtas_paths[8], width=250)
                if subtopic == "Centroides":
                    if pregunta_no ==1:
                        st.image(CT_rtas_paths[1], width=200)
                if subtopic == "Fuerzas distribuidas":
                    if pregunta_no ==1:
                        st.image(FD_rtas_paths[5], width=350)
                    if pregunta_no ==2:
                        st.image(FD_rtas_paths[6], width=350)
                    if pregunta_no ==3:
                        st.image(FD_rtas_paths[7], width=350)

            if difficulty == "Díficil":
                if subtopic == "Vectores 2D":
                    if pregunta_no == 1 or pregunta_no == 2: 
                        if version_no == 1:
                            st.image(EQ_rtas_paths[0], width=550) 
                        elif version_no == 2:
                            st.image(EQ_rtas_paths[1], width=550)
                        elif version_no == 3:
                            st.image(EQ_rtas_paths[2], width=550)
                        elif version_no == 4:
                            st.image(EQ_rtas_paths[3], width=550)
                    if pregunta_no == 3: 
                        if version_no == 1:
                            st.image(EQ_rtas_paths[4], width=550) 
                        elif version_no == 2:
                            st.image(EQ_rtas_paths[5], width=550)
                    if pregunta_no == 5: 
                        if version_no == 1 or version_no == 2:
                            st.image(EQ_rtas_paths[6], width=250) 
                        elif version_no == 3 or version_no == 4:
                            st.image(EQ_rtas_paths[7], width=250)  
                if subtopic == "Centroides":
                    if pregunta_no ==1:
                        st.image(CT_rtas_paths[2], width=600)                                         
        return

    def filtrar_imagenes_respuestas_P2(pregunta_no, version_no, subtopic, difficulty):
        left_col, center_col, right_col = st.columns(3)

        with left_col:
            if difficulty == "Fácil":
                if subtopic == "Fuerzas distribuidas":
                    if pregunta_no ==1:
                        st.image(FD_rtas_paths[1], width=350)
                    if pregunta_no ==3:
                        st.image(FD_rtas_paths[4], width=350)
        return

    #Función para que el botón "Ayuda" muestre secuencialmente las ayudas
    def butt_ayuda(preguntas_filtradas, pregunta_actual, ayuda_clicked):
        ayudas = [preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].ayuda1, preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].ayuda2, preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].ayuda3]
                
        ayudas_no_vacias = [ayuda for ayuda in ayudas if ayuda.strip() != ""]
        if 'ayuda_index' not in st.session_state:
            st.session_state.ayuda_index = 0 
        if ayuda_clicked:
            if ayudas_no_vacias:
                help_text_placeholder = st.empty() 
                help_text_placeholder.write(ayudas[st.session_state.ayuda_index])
                st.session_state.ayuda_index = (st.session_state.ayuda_index + 1) % len(ayudas_no_vacias)
                if st.session_state.get("consent", False):
                    log_event(st.session_state["username"], "help_requested", {
                    "question_id": preguntas_filtradas[pregunta_actual].no_pregunta,
                    "help_index": st.session_state.ayuda_index
                    })

    #Función para generar una nueva versión de la pregunta
    def nueva_version_callback(username):
        no_pregunta_actual = preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].no_pregunta
        preguntas_actuales = [pregunta for pregunta in preguntas_filtradas if pregunta.no_pregunta == no_pregunta_actual]
        versiones = sorted(set([pregunta.version for pregunta in preguntas_actuales]))
            
        if len(versiones) == 1:
            misma_pregunta = preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']]
            misma_pregunta.regenerate_values()
            st.session_state.Intento = 0
        else:
            indice_version_actual = versiones.index(st.session_state.version_actual)
            siguiente_version = (indice_version_actual + 1) % len(versiones)
            st.session_state.version_actual = versiones[siguiente_version]

            for i, pregunta in enumerate(preguntas_filtradas):
                if pregunta.no_pregunta == no_pregunta_actual and pregunta.version == st.session_state.version_actual:
                    st.session_state[f'pregunta_actual_{username}'] = i
                    st.session_state.Intento = 0
                #break
            
        if st.session_state.get("consent", False):
            log_event(st.session_state["username"], "new_version_generated", {
            "question_id": no_pregunta_actual,
            "new_version": st.session_state.version_actual
                })
                        
    #Función para generar un nuevo problema
    def nuevo_problema_callback(username):
        nuevo_problema = st.session_state[f'pregunta_actual_{username}'] + 1
        while nuevo_problema < len(preguntas_filtradas) and preguntas_filtradas[nuevo_problema].no_pregunta == preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].no_pregunta:
            nuevo_problema += 1
        if nuevo_problema >= len(preguntas_filtradas):
            nuevo_problema = 0

        st.session_state[f'pregunta_actual_{username}'] = nuevo_problema
        st.session_state.version_actual = 1 
        st.session_state.Intento = 0
            
        if st.session_state.get("consent", False):
            log_event(st.session_state["username"], "new_problem_generated", {
            "new_question_id": preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].no_pregunta
            })

    #Function to Display the Answer Explanation
    def mostrar_respuesta(username):
        st.write(preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].respuesta_P1)
        filtrar_imagenes_respuestas_P1(preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].no_pregunta, preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].version, preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].subtopic, preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].complexity)
        st.write(preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].respuesta_P2) 
        filtrar_imagenes_respuestas_P2(preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].no_pregunta, preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].version, preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].subtopic, preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].complexity)
        st.write(preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].respuesta_P3) 
        
        if st.session_state.get("consent", False):
            log_event(st.session_state["username"], "answer_revealed", {
            "question_id": preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].no_pregunta
            })

    #Function to display the Answer Explanation for the "Quiero ver la respuesta" button
    def on_button_click(username):
        st.session_state.mostrar_respuesta = True

    #Function to generate the questions
    def generate_questions(username):
        current_question = preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']]

        st.markdown(f"<h2 style='text-align: left;'>{current_question.topic} - {current_question.subtopic}</h2>", unsafe_allow_html=True)
        st.write("""
                 """) 
        st.markdown('<h3 style="font-size:18px;">Pregunta</h3>', unsafe_allow_html=True)
        st.write(current_question.pregunta)
        filtrar_imagenes_preguntas(current_question.no_pregunta, current_question.version, current_question.subtopic, current_question.complexity)
    
        st.markdown('<h3 style="font-size:18px;">Respuestas</h3>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 14px;">Ingrese sus respuestas con dos decimales</p>', unsafe_allow_html=True)
        response1, response2, response3 = render_input_widgets(preguntas_filtradas, st.session_state[f'pregunta_actual_{username}'])
    
        st.markdown('<h3 style="font-size:18px;">Acciones</h3>', unsafe_allow_html=True)
    
        respuesta_pressed, ayuda_pressed, repetir_pressed, nuevo_pressed = st.columns(4)
        respuesta_clicked = respuesta_pressed.button(":green[Verificar respuesta]", key=f"respuesta_button_{st.session_state[f'pregunta_actual_{username}']}", help="Verificación de la respuesta", use_container_width=True)
        ayuda_clicked = ayuda_pressed.button(":blue[Ayuda]", key=f"ayuda_button_{st.session_state[f'pregunta_actual_{username}']}", help="Ayuda para la solución", use_container_width=True)
        repetir_pressed.button("Nueva versión", key="nueva_version_button", help="Genera una nueva versión del problema", use_container_width=True, on_click=nueva_version_callback, args=(username,))
        nuevo_pressed.button("Siguiente problema", key=f"nuevo_problema_button{st.session_state[f'pregunta_actual_{username}']}", help="Genera un nuevo problema", use_container_width=True, on_click=nuevo_problema_callback, args=(username,))
    
        if st.session_state.get("consent", False):
            log_event(st.session_state["username"], "question_viewed", {
                "question_id": current_question.no_pregunta,
                "version": current_question.version
            })
    
        return response1, response2, response3, respuesta_clicked, ayuda_clicked

    
    def generate_calculation_questions(username):
            
        response1, response2, response3, respuesta_clicked, ayuda_clicked = generate_questions(username)

        # "Verificar respuesta" button - Evaluation of the validity of the result input by user
        if respuesta_clicked:
            st.session_state.Intento += 1
            outputx, is_correct = resultado(preguntas_filtradas, response1, response2, response3, st.session_state[f'pregunta_actual_{username}'])
            st.write(outputx)
                    
            difficulty = preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].complexity
            used_help = st.session_state.get('ayuda_used', False)
            points_earned = calculate_points(difficulty, st.session_state.Intento, used_help)
                    
            if is_correct == 1:
                st.session_state.mostrar_respuesta = True
                log_event(st.session_state["username"], "points_earned", {"points": points_earned})
            elif is_correct == 0:
                if st.session_state.Intento > 3:
                    st.button(":pensive: Quiero ver la respuesta", key=f"ver_respuesta_button{st.session_state[f'pregunta_actual_{username}']}", help="Permite ver la respuesta", on_click=on_button_click, args=(username,))
                    
            if st.session_state.get("consent", False):
                log_event(st.session_state["username"], "answer_submitted", {
                "question_id": preguntas_filtradas[st.session_state[f'pregunta_actual_{username}']].no_pregunta,
                "attempt": st.session_state.Intento,
                "is_correct": is_correct,
                "points_earned": points_earned
                })
                
        if st.session_state.mostrar_respuesta:
            mostrar_respuesta(username)
            st.session_state.mostrar_respuesta = False
                            
        # "Ayuda" button - It shows helps 
        if ayuda_clicked:    
            butt_ayuda(preguntas_filtradas, st.session_state[f'pregunta_actual_{username}'], ayuda_clicked)
            st.session_state.ayuda_used = True
    
    #=========================Functions to generate the theory questions============================
    def opciones_respuesta():
        opcion_seleccionada = st.radio("",options=[conceptuales_filtradas[st.session_state[f'pregunta_actual_{username}']].opcion_1, conceptuales_filtradas[st.session_state[f'pregunta_actual_{username}']].opcion_2, conceptuales_filtradas[st.session_state[f'pregunta_actual_{username}']].opcion_3, conceptuales_filtradas[st.session_state[f'pregunta_actual_{username}']].opcion_4]) 
        return opcion_seleccionada

    #Function to evaluate the user's answers
    def evaluacion_respuesta_teoria(conceptuales_filtradas, opcion_seleccionada, pregunta_actual):
        respuesta_correcta = conceptuales_filtradas[pregunta_actual].opcion_correcta

        text_respuesta = ""
        contador = 0
        if respuesta_correcta == opcion_seleccionada:
            text_respuesta = "Felicitaciones!!!! La respuesta es correcta."
            contador = 1
        else:
            text_respuesta = "La respuesta no es correcta, intente de nuevo."
        return text_respuesta, contador


    # Function to Generate a New Problem
    def nuevo_problema_teoria_callback():
        nuevo_problema_teoria = st.session_state[f'pregunta_actual_{username}'] + 1
        while nuevo_problema_teoria < len(conceptuales_filtradas) and conceptuales_filtradas[nuevo_problema_teoria].no_pregunta == conceptuales_filtradas[st.session_state[f'pregunta_actual_{username}']].no_pregunta:
            nuevo_problema_teoria += 1
        if nuevo_problema_teoria >= len(conceptuales_filtradas):
            nuevo_problema_teoria = 0
        st.session_state[f'pregunta_actual_{username}'] = nuevo_problema_teoria

   #Función para mostrar la imagen de la pregunta de teoría
    def filtrar_imagenes_teoria(pregunta_no, subtopic):
        left_col, center_col, right_col = st.columns(3)
        with center_col:
            if subtopic == "Vectores":
                if pregunta_no == 1: 
                    st.image(EQ_teoria_preguntas[0], width=180)  
                if pregunta_no == 2 or pregunta_no == 3: 
                    st.image(EQ_teoria_preguntas[1], width=200)
                if pregunta_no == 4: 
                    st.image(EQ_teoria_preguntas[2], width=300)  
                if pregunta_no == 5: 
                    st.image(EQ_teoria_preguntas[3], width=250)  
                if pregunta_no == 6: 
                    st.image(EQ_teoria_preguntas[4], width=350)  
                if pregunta_no == 7: 
                    st.image(EQ_teoria_preguntas[5], width=225)
                if pregunta_no == 8: 
                    st.image(EQ_teoria_preguntas[6], width=250)  
                if pregunta_no == 9 or pregunta_no == 12: 
                    st.image(EQ_teoria_preguntas[7], width=250)  
                if pregunta_no == 11: 
                    st.image(EQ_teoria_preguntas[8], width=550)
            if subtopic == "Equilibrio":
                if pregunta_no == 4:
                    st.image(EQ_image_paths[37], width=350) 
                if pregunta_no == 5: 
                    st.image(EQ_teoria_preguntas[9], width=550)      
                if pregunta_no == 7: 
                    st.image(EQ_teoria_preguntas[10], width=500)    
                if pregunta_no == 8: 
                    st.image(EQ_teoria_preguntas[11], width=250)
                if pregunta_no == 9: 
                    st.image(EQ_teoria_preguntas[12], width=450)    
            if subtopic == "Centroides":
                if pregunta_no == 1:
                    st.image(CT_teoria_preguntas[0], width=350)
                if pregunta_no == 2:
                    st.image(CT_teoria_preguntas[1], width=350)
                if pregunta_no == 6:
                    st.image(CT_teoria_preguntas[2], width=300)
            if subtopic == "Vigas":
                if pregunta_no == 1:
                    st.image(FD_teoria_preguntas[0], width=520)
                if pregunta_no == 2:
                    st.image(FD_teoria_preguntas[1], width=400)
                if pregunta_no == 3:
                    st.image(FD_teoria_preguntas[2], width=520)

        with left_col:
            if subtopic == "Presiones hidrostáticas":
                if pregunta_no == 1:
                    st.image(FD_teoria_preguntas[3], width=900)
                if pregunta_no == 3:
                    st.image(FD_teoria_preguntas[4], width=750)
        return

    #Función para mostrar la imagen de la respuesta
    def filtrar_imagenes_respuestas_teoria_P1(pregunta_no, subtopic):
        left_col, center_col, right_col = st.columns(3)

        with left_col:
                if subtopic == "Vectores":
                    if pregunta_no == 12: 
                        st.image(EQ_teoria_respuestas[0],width=200)
                    if pregunta_no == 13: 
                        st.image(EQ_teoria_respuestas[1],width=250)
                if subtopic == "Centroides":
                    if pregunta_no == 6:
                        st.image(CT_teoria_respuestas[0],width=300)
        return

    def generate_theory_questions():
        st.markdown(f"<h2 style='text-align: left;'>{conceptuales_filtradas[st.session_state[f'pregunta_actual_{username}']].topic} - {conceptuales_filtradas[st.session_state[f'pregunta_actual_{username}']].subtopic}</h2>", unsafe_allow_html=True)
        st.write("""
                 """)
        st.markdown('<h3 style="font-size:18px;">Pregunta</h3>', unsafe_allow_html=True) #Title Pregunta
        st.write(conceptuales_filtradas[st.session_state[f'pregunta_actual_{username}']].enunciado) #Write the statement question
        filtrar_imagenes_teoria(conceptuales_filtradas[st.session_state[f'pregunta_actual_{username}']].no_pregunta, conceptuales_filtradas[st.session_state[f'pregunta_actual_{username}']].subtopic)
        #Answer options
        opcion_seleccionada = opciones_respuesta()

        #Buttons
        verificar_pressed, siguiente_pressed, col_3, col_4 = st.columns(4)
        verificar_clicked = verificar_pressed.button(":green[Verificar respuesta]", key=f"verificar_respuesta_teoria_button{st.session_state[f'pregunta_actual_{username}']}", use_container_width=True, help="Verificación la respuesta")
        sproblema_clicked = siguiente_pressed.button("Siguiente problema", key=f"nuevo_problema_button{st.session_state[f'pregunta_actual_{username}']}", help="Genera un nuevo problema", use_container_width=True, on_click=nuevo_problema_teoria_callback)

        # "Verificar respuesta" button - Evaluation of the validity of the result input by user
        if verificar_clicked:
            text_respuesta, is_correct = evaluacion_respuesta_teoria(conceptuales_filtradas, opcion_seleccionada, st.session_state[f'pregunta_actual_{username}'])
            st.write(text_respuesta)
            if is_correct == 1:
                st.write(conceptuales_filtradas[st.session_state[f'pregunta_actual_{username}']].respuesta_P1)
                filtrar_imagenes_respuestas_teoria_P1(conceptuales_filtradas[st.session_state[f'pregunta_actual_{username}']].no_pregunta, conceptuales_filtradas[st.session_state[f'pregunta_actual_{username}']].subtopic)
                st.write(conceptuales_filtradas[st.session_state[f'pregunta_actual_{username}']].respuesta_P2)

    def main():
        if way == "Práctica":
            generate_calculation_questions(username)
        elif way == "Teoría":
            generate_theory_questions()
    

    if __name__ == '__main__':  
        if action == "Estudiar":
            main() 
                
        if st.session_state.get("consent", False):
            study_duration = int((datetime.now() - st.session_state.get("session_start_time", datetime.now())).total_seconds() / 60)
            log_event(st.session_state["username"], "study_time", study_duration)
            log_event(st.session_state["username"], "session_end", {})

        # Don't forget to set the session start time when the user logs in:
        if "authenticated" in st.session_state and st.session_state["authenticated"]:
            if "session_start_time" not in st.session_state:
                st.session_state.session_start_time = datetime.now()

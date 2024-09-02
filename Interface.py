import streamlit as st
import streamlit_authenticator as stauth
import uuid
import numpy as np
import pandas as pd
import random as rd
import math
from Class_Preguntas import Questionary, preguntas
from Class_Teoria import Theory, conceptuales
from Imagenes import *

# Nuevas importaciones
import sqlite3
from datetime import datetime, timedelta
import cv2
import pyautogui
import base64
import threading
import time
import os
import json
import plotly.express as px

#=========================Configuración de la página============================
st.set_page_config(layout="wide")

col_1, col_2, col_3 = st.columns(3)

#Leer credenciales de usuarios y crear un diccionario
datos_usuarios = pd.read_excel("./Usuarios.xlsx")
datos_usuarios["username"] = datos_usuarios["username"].astype(str)
datos_usuarios["password"] = datos_usuarios["password"].astype(str)
users_credentials = pd.Series(datos_usuarios.password.values, index=datos_usuarios.username).to_dict()

# Configuración de la base de datos
def init_db():
    conn = sqlite3.connect('user_activity.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_events
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT,
                  timestamp TEXT,
                  event_type TEXT,
                  event_data TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS screen_recordings
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT,
                  timestamp TEXT,
                  recording_path TEXT)''')
    conn.commit()
    conn.close()

init_db()

# Función para registrar eventos
# Update the log_event function to ensure proper JSON formatting
def log_event(username, event_type, event_data):
    conn = sqlite3.connect('user_activity.db')
    c = conn.cursor()
    timestamp = datetime.now().isoformat()
    event_data_json = json.dumps(event_data)  # Ensure proper JSON formatting
    c.execute("INSERT INTO user_events (username, timestamp, event_type, event_data) VALUES (?, ?, ?, ?)",
              (username, timestamp, event_type, event_data_json))
    conn.commit()
    conn.close()

# Funciones actualizadas de grabación de pantalla

def start_screen_recording(username):
    if "screen_recorder" not in st.session_state:
        # Crear el nombre del archivo
        filename = f"screen_recording_{username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
        
        # Obtener el directorio actual del script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Crear la ruta completa para el directorio de grabaciones
        recordings_dir = os.path.join(current_dir, 'grabaciones')
        
        # Asegurar que el directorio existe
        os.makedirs(recordings_dir, exist_ok=True)
        
        # Crear la ruta completa del archivo
        filepath = os.path.join(recordings_dir, filename)
        
        # Obtener el tamaño de la pantalla
        screen_size = pyautogui.size()
        
        # Inicializar el escritor de video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(filepath, fourcc, 10.0, screen_size)
        
        st.session_state["screen_recorder"] = out
        st.session_state["recording_filename"] = filepath
        
        # Iniciar el hilo de grabación
        st.session_state["recording_thread"] = threading.Thread(target=record_screen, args=(username,))
        st.session_state["recording_thread"].start()
        
        # Registrar el inicio de la grabación
        log_event(username, "screen_recording_started", {"filename": filepath})
        print(f"Iniciando grabación: {filepath}")  # Añadir log para depuración

def record_screen(username):
    try:
        while st.session_state.get("screen_record_consent", False):
            # Capture the screen
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
            # Write the frame
            st.session_state["screen_recorder"].write(frame)
            
            # Sleep to control frame rate
            time.sleep(0.1)  # Adjust this for desired frame rate
    except Exception as e:
        print(f"Error in screen recording: {str(e)}")
    finally:
        stop_screen_recording(username)

def stop_screen_recording(username):
    if "screen_recorder" in st.session_state:
        st.session_state["screen_recorder"].release()
        log_event(username, "screen_recording_stopped", {"filename": st.session_state.get("recording_filename", "Unknown")})
        del st.session_state["screen_recorder"]
        if "recording_thread" in st.session_state:
            st.session_state["recording_thread"].join()
            del st.session_state["recording_thread"]

# Función para obtener el consentimiento del usuario
def get_user_consent():
    st.sidebar.markdown("## Consentimiento de Recolección de Datos")
    consent = st.sidebar.checkbox("Acepto el seguimiento anónimo de actividad para mejorar la aplicación")
    screen_record_consent = st.sidebar.checkbox("Acepto la grabación opcional de pantalla con fines de investigación")
    
    if "authenticated" in st.session_state and st.session_state["authenticated"]:
        username = st.session_state.get("username", "unknown_user")
        if consent:
            log_event(username, "consent_given", {"type": "activity_tracking"})
        if screen_record_consent:
            log_event(username, "consent_given", {"type": "screen_recording"})
            start_screen_recording(username)
    
    return consent, screen_record_consent

#Función para verificar credenciales
def creds_entered():
    username = st.session_state["user"].strip()
    password = st.session_state["passwd"].strip()
    
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
            st.text_input(label="Username:", value="", key="user")
            st.text_input(label="Password:", value="", key="passwd", type="password")
            if st.button("Iniciar sesión"):
                creds_entered()
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
                st.text_input(label="Username:", value="", key="user")
                st.text_input(label="Password:", value="", key="passwd", type="password")
                if st.button("Login"):
                    creds_entered()
                return False

def get_user_statistics(username):
    conn = sqlite3.connect('user_activity.db')
    
    # Study time
    study_time_query = """
    SELECT DATE(timestamp) as date, SUM(CAST(event_data AS INTEGER)) as total_time
    FROM user_events
    WHERE username = ? AND event_type = 'study_time'
    GROUP BY DATE(timestamp)
    ORDER BY date
    """
    study_time_df = pd.read_sql_query(study_time_query, conn, params=(username,))
    study_time_df['date'] = pd.to_datetime(study_time_df['date'])
    
    # Exercises solved
    exercises_query = """
    SELECT DATE(timestamp) as date, 
           COUNT(*) as total,
           SUM(CASE WHEN event_data LIKE '%"is_correct": true%' OR event_data LIKE '%"is_correct": 1%' THEN 1 ELSE 0 END) as correct
    FROM user_events
    WHERE username = ? AND event_type = 'answer_submitted'
    GROUP BY DATE(timestamp)
    ORDER BY date
    """
    exercises_df = pd.read_sql_query(exercises_query, conn, params=(username,))
    exercises_df['date'] = pd.to_datetime(exercises_df['date'])
    
    # Points
    points_query = """
    SELECT DATE(timestamp) as date, SUM(CAST(JSON_EXTRACT(event_data, '$.points') AS INTEGER)) as total_points
    FROM user_events
    WHERE username = ? AND event_type = 'points_earned'
    GROUP BY DATE(timestamp)
    ORDER BY date
    """
    try:
        points_df = pd.read_sql_query(points_query, conn, params=(username,))
        points_df['date'] = pd.to_datetime(points_df['date'])
    except sqlite3.OperationalError:
        # If JSON_EXTRACT fails, fall back to a simpler query
        points_query = """
        SELECT DATE(timestamp) as date, COUNT(*) as total_points
        FROM user_events
        WHERE username = ? AND event_type = 'points_earned'
        GROUP BY DATE(timestamp)
        ORDER BY date
        """
        points_df = pd.read_sql_query(points_query, conn, params=(username,))
        points_df['date'] = pd.to_datetime(points_df['date'])
    
    conn.close()
    
    return study_time_df, exercises_df, points_df

def create_study_time_chart(study_time_df):
    fig = px.line(study_time_df, x='date', y='total_time', title='Tiempo de Estudio Diario')
    fig.update_layout(yaxis_title='Tiempo de Estudio (minutos)')
    return fig

def create_exercises_chart(exercises_df):
    fig = px.bar(exercises_df, x='date', y=['correct', 'total'], title='Ejercicios Resueltos Diariamente',
                 labels={'value': 'Número de Ejercicios', 'variable': 'Tipo'})
    return fig

def create_points_chart(points_df):
    fig = px.line(points_df, x='date', y='total_points', title='Puntos Ganados Diariamente')
    fig.update_layout(yaxis_title='Puntos')
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

#Mostrar página web cuando el usuario está autenticado           
if authenticate_user():
    consent, screen_record_consent = get_user_consent()
    st.session_state["consent"] = consent
    st.session_state["screen_record_consent"] = screen_record_consent

#-------------------------------Inicialización de variables con sesión de estado-----------------------------------------

    #Initialize the "Intento" Variable to Count the Number of User's Attempts to Verify Their Answer
    if 'Intento' not in st.session_state:
        st.session_state.Intento = 0
    #Initialize the State for the "mostrar_respuesta" Function When the User Verifies Their Answer
    if 'mostrar_respuesta' not in st.session_state:
        st.session_state.mostrar_respuesta = False
    #Initialize the questions to show
    if 'pregunta_actual' not in st.session_state:
        st.session_state.pregunta_actual = 0 
    #Initialize the version of the question to show    
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

    #-------------------------------------------Creación de la barra lateral-------------------------------------
    st.sidebar.markdown("<h1 style='font-size:36px;'>StaticGenius</h1>", unsafe_allow_html=True)
    way = st.sidebar.radio("Seleccione su método de estudio", options=["Práctica", "Teoría", "Estadísticas"])
    respuesta_usuario = {}
    respuesta_usuario['way'] = way


    if way == "Estadísticas":
        st.header("Estadísticas de Usuario")
        
        username = st.session_state.get("username", "unknown_user")
        study_time_df, exercises_df, points_df = get_user_statistics(username)
        
        # Display total statistics
        total_stats = calculate_total_statistics(study_time_df, exercises_df, points_df)
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Tiempo Total de Estudio", f"{total_stats['total_study_time']} min")
        col2.metric("Ejercicios Totales", total_stats['total_exercises'])
        col3.metric("Ejercicios Correctos", total_stats['total_correct'])
        col4.metric("Puntos Totales", total_stats['total_points'])
        
        # Display charts
        st.plotly_chart(create_study_time_chart(study_time_df))
        st.plotly_chart(create_exercises_chart(exercises_df))
        st.plotly_chart(create_points_chart(points_df))
        
        if consent:
            log_event(username, "statistics_viewed", {})
    
    elif way == "Teoría":
        st.sidebar.header("Teoría")
        topic=st.sidebar.selectbox("Seleccione el tema", options=["Equilibrio de partículas", "Momento"])
        respuesta_usuario['topic'] = topic

        if topic=="Equilibrio de partículas":
            subtopic=st.sidebar.selectbox("Seleccione el subtema", options=["Vectores","Equilibrio"])
            respuesta_usuario['subtopic'] = subtopic

        if consent:
            log_event(st.session_state["username"], "theory_section_accessed", {})
        # Aquí puedes añadir el contenido de la sección de teoría
        #st.write("Contenido de la sección de teoría aún no implementado.")
    else:
        st.sidebar.header("Práctica")
        complexity = st.sidebar.radio("Nivel de dificultad", options=["Fácil", "Medio", "Díficil"])
        topic = st.sidebar.selectbox("Seleccione el tema", options=["Equilibrio de partículas"])
        
        if topic == "Equilibrio de partículas":
            subtopic = st.sidebar.selectbox("Seleccione el subtema", options=["Vectores 2D", "Vectores 3D", "Vector unitario", "Equilibrio 2D", "Equilibrio 3D"])
        
        if consent:
            log_event(st.session_state["username"], "practice_options_selected", {
                "complexity": complexity,
                "topic": topic,
                "subtopic": subtopic
            })

        #Almacenar la selección del usuario
        respuesta_usuario = {'complexity': complexity, 'topic': topic, 'subtopic': subtopic}
    
    topic_user = respuesta_usuario.get('topic', None)
    subtopic_user = respuesta_usuario.get('subtopic', None)
    complexity_user = respuesta_usuario.get('complexity', None)  

    #Lista filtrada de preguntas según la selección del usuario
    preguntas_filtradas = Questionary.filtrar_preguntas(preguntas, topic_user, subtopic_user, complexity_user)
    conceptuales_filtradas = Theory.filtrar_preguntas_teoria(conceptuales, topic_user, subtopic_user)
        
    #Reinicia el número de la pregunta cuando se cambia de tema, subtema o nivel de dificulta
   # Verificar si se ha cambiado alguna de las opciones
    if way == "Práctica":
        if (st.session_state.way != way or st.session_state.topic != topic or st.session_state.subtopic != subtopic or st.session_state.complexity != complexity):
        # Actualizar el estado de sesión con las nuevas selecciones
            st.session_state.way = way
            st.session_state.topic = topic
            st.session_state.subtopic = subtopic
            st.session_state.complexity = complexity 
            # Reiniciar el número de la pregunta
            st.session_state.pregunta_actual = 0
    elif way == "Teoría":
        if (st.session_state.way != way or st.session_state.topic != topic or st.session_state.subtopic != subtopic):
        # Actualizar el estado de sesión con las nuevas selecciones
            st.session_state.way = way
            st.session_state.topic = topic
            st.session_state.subtopic = subtopic
            # Reiniciar el número de la pregunta
            st.session_state.pregunta_actual = 0




    #=========================Funciones para generar las preguntas============================

    #Función para crear las cajas para las respuestas del usuario
    def render_input_widgets(preguntas_filtradas, pregunta_actual):
        col1, col2, col3 = st.columns(3)
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
        if preguntas_filtradas[pregunta_actual].no_answers == 1:
            if abs(respx1 - response1) < 0.1:
                outxt = 'Felicitaciones!!!! La respuesta es correcta.'
                cont = 1
            else:
                outxt = 'La respuesta no es correcta, presione el boton de "Ayuda", o trate de nuevo.'
        elif preguntas_filtradas[pregunta_actual].no_answers == 2:
            if abs(respx1 - response1) > 0.1 and abs(respx2 - response2) > 0.1:
                outxt = 'Las respuestas no son correctas, presione el boton de "Ayuda", o trate de nuevo.'
            else:
                if abs(respx1 - response1) < 0.1 and abs(respx2 - response2) < 0.1:
                    outxt = 'Felicitaciones!!!! La respuesta es correcta.'
                    cont = 1
                elif abs(respx1 - response1) < 0.1 and abs(respx2 - response2) > 0.1:
                    outxt = 'Solamente la primera respuesta es correcta, presione el boton de "Ayuda", o trate de nuevo.'
                elif abs(respx1 - response1) > 0.1 and abs(respx2 - response2) < 0.1:
                    outxt = 'Solamente la segunda respuesta es correcta, presione el boton de "Ayuda", o trate de nuevo.'
        elif preguntas_filtradas[pregunta_actual].no_answers == 3:
            if abs(respx1 - response1) > 0.1 and abs(respx2 - response2) > 0.1 and abs(respx3 - response3) > 0.1:
                outxt = 'Las respuestas no son correctas, presione el boton de "Ayuda", o trate de nuevo.'
            else:
                if abs(respx1 - response1) < 0.1 and abs(respx2 - response2) < 0.1 and abs(respx3 - response3) < 0.1:
                    outxt = 'Felicitaciones!!!! La respuesta es correcta.'
                    cont = 1
                else:
                    correct_answers = []
                    if abs(respx1 - response1) < 0.1:
                        correct_answers.append("primera")
                    if abs(respx2 - response2) < 0.1:
                        correct_answers.append("segunda")
                    if abs(respx3 - response3) < 0.1:
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
                            st.image(image_paths[0], width=325) 
                        elif version_no == 2:
                            st.image(image_paths[1], width=350)
                        elif version_no == 3:
                            st.image(image_paths[2], width=350)
                        elif version_no == 4:
                            st.image(image_paths[3], width=350)   
                            
                    elif pregunta_no > 2 and pregunta_no <= 4: #Vectores 2D y Vector unitario
                        if version_no == 1:
                            st.image(image_paths[4], width=200)
                        elif version_no == 2:
                            st.image(image_paths[5], width=200)
                        elif version_no == 3:
                            st.image(image_paths[6], width=200)
                        elif version_no == 4:
                            st.image(image_paths[7], width=200)
                if subtopic == "Vectores 3D":
                    if pregunta_no == 1 or pregunta_no == 2:
                        if version_no == 1:
                            st.image(image_paths[29], width=325) 
                        elif version_no == 2:
                            st.image(image_paths[30], width=350)
                        elif version_no == 3:
                            st.image(image_paths[31], width=350)
                        elif version_no == 4:
                            st.image(image_paths[32], width=350)
                    if pregunta_no == 3 or pregunta_no == 4:
                        if version_no == 1:
                            st.image(image_paths[33], width=325) 
                        elif version_no == 2:
                            st.image(image_paths[34], width=350)
                        elif version_no == 3:
                            st.image(image_paths[35], width=350)
                        elif version_no == 4:
                            st.image(image_paths[36], width=350) 
                        

                
            if difficulty == "Medio":
                if subtopic == "Vectores 2D":
                    if pregunta_no == 1:
                        if version_no == 1:
                            st.image(image_paths[8], width=250)
                        elif version_no == 2:
                            st.image(image_paths[9], width=250)
                        elif version_no == 3:
                            st.image(image_paths[10], width=250)
                        elif version_no == 4:
                            st.image(image_paths[11], width=250)    
                    if pregunta_no == 2:
                        if version_no == 1:
                            st.image(image_paths[12], width=300)
                        elif version_no == 2:
                            st.image(image_paths[13])
                        elif version_no == 3:
                            st.image(image_paths[14])
                        elif version_no == 4:
                            st.image(image_paths[15])   
                    if pregunta_no == 3:
                        st.image(image_paths[16], width=330)
                    if pregunta_no == 4:
                        st.image(image_paths[17], width=180)
                if subtopic == "Vectores 3D":
                    if pregunta_no == 1 or pregunta_no==2 or pregunta_no == 3:
                        if version_no == 1:
                            st.image(image_paths[37], width=350)
                        elif version_no == 2:
                            st.image(image_paths[38], width=350)
                        elif version_no == 3:
                            st.image(image_paths[39], width=350)
                        elif version_no == 4:
                            st.image(image_paths[40], width=350) 
                
            if difficulty == "Díficil":
                if subtopic == "Vectores 2D":
                    if pregunta_no == 1 or pregunta_no == 2:
                        if version_no == 1:
                            st.image(image_paths[18], width=350)
                        elif version_no == 2:
                            st.image(image_paths[19], width=350)
                        elif version_no == 3:
                            st.image(image_paths[20], width=350)
                        elif version_no == 4:
                            st.image(image_paths[21], width=350)
                    if pregunta_no == 3:
                        if version_no == 1:
                            st.image(image_paths[23], width=250)
                        elif version_no == 2:
                            st.image(image_paths[24], width=250)
                    if pregunta_no == 4:
                        st.image(image_paths[22], width=350)
                    if pregunta_no == 5:
                        if version_no == 1:
                            st.image(image_paths[25], width=250)
                        elif version_no == 2:
                            st.image(image_paths[26], width=250)
                        elif version_no == 3:
                            st.image(image_paths[27], width=250)
                        elif version_no == 4:
                            st.image(image_paths[28], width=250)
                            
        return

    #Función para mostrar la imagen de la respuesta
    def filtrar_imagenes_respuestas_P1(pregunta_no, version_no, subtopic, difficulty):
        left_col, center_col, right_col = st.columns(3)

        with left_col:
            if difficulty == "Díficil":
                if subtopic == "Vectores 2D":
                    if pregunta_no == 1 or pregunta_no == 2: 
                        if version_no == 1:
                            st.image(rtas_paths[0], width=550) 
                        elif version_no == 2:
                            st.image(rtas_paths[1], width=550)
                        elif version_no == 3:
                            st.image(rtas_paths[2], width=550)
                        elif version_no == 4:
                            st.image(rtas_paths[3], width=550)
                    if pregunta_no == 3: 
                        if version_no == 1:
                            st.image(rtas_paths[4], width=550) 
                        elif version_no == 2:
                            st.image(rtas_paths[5], width=550)
                    if pregunta_no == 5: 
                        if version_no == 1 or version_no == 2:
                            st.image(rtas_paths[6], width=250) 
                        elif version_no == 3 or version_no == 4:
                            st.image(rtas_paths[7], width=250)                    
        return

    #Función para que el botón "Ayuda" muestre secuencialmente las ayudas
    def butt_ayuda(preguntas_filtradas, pregunta_actual, ayuda_clicked):
        ayudas = [preguntas_filtradas[st.session_state.pregunta_actual].ayuda1, preguntas_filtradas[st.session_state.pregunta_actual].ayuda2, preguntas_filtradas[st.session_state.pregunta_actual].ayuda3]
                
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
    def nueva_version_callback():
        no_pregunta_actual = preguntas_filtradas[st.session_state.pregunta_actual].no_pregunta
        preguntas_actuales = [pregunta for pregunta in preguntas_filtradas if pregunta.no_pregunta == no_pregunta_actual]
        versiones = sorted(set([pregunta.version for pregunta in preguntas_actuales]))
            
        if len(versiones) == 1:
            misma_pregunta = preguntas_filtradas[st.session_state.pregunta_actual]
            misma_pregunta.regenerate_values()
            st.session_state.Intento = 0
        else:
            indice_version_actual = versiones.index(st.session_state.version_actual)
            siguiente_version = (indice_version_actual + 1) % len(versiones)
            st.session_state.version_actual = versiones[siguiente_version]

            for i, pregunta in enumerate(preguntas_filtradas):
                if pregunta.no_pregunta == no_pregunta_actual and pregunta.version == st.session_state.version_actual:
                    st.session_state.pregunta_actual = i
                    st.session_state.Intento = 0
                #break
            
        if st.session_state.get("consent", False):
            log_event(st.session_state["username"], "new_version_generated", {
            "question_id": no_pregunta_actual,
            "new_version": st.session_state.version_actual
                })
                        
    #Función para generar un nuevo problema
    def nuevo_problema_callback():
        nuevo_problema = st.session_state.pregunta_actual + 1
        while nuevo_problema < len(preguntas_filtradas) and preguntas_filtradas[nuevo_problema].no_pregunta == preguntas_filtradas[st.session_state.pregunta_actual].no_pregunta:
            nuevo_problema += 1
        if nuevo_problema >= len(preguntas_filtradas):
            nuevo_problema = 0

        st.session_state.pregunta_actual = nuevo_problema
        st.session_state.version_actual = 1 
        st.session_state.Intento = 0
            
        if st.session_state.get("consent", False):
            log_event(st.session_state["username"], "new_problem_generated", {
            "new_question_id": preguntas_filtradas[st.session_state.pregunta_actual].no_pregunta
            })

    #Function to Display the Answer Explanation
    def mostrar_respuesta():
        st.write(preguntas_filtradas[st.session_state.pregunta_actual].respuesta_P1)
        filtrar_imagenes_respuestas_P1(preguntas_filtradas[st.session_state.pregunta_actual].no_pregunta, preguntas_filtradas[st.session_state.pregunta_actual].version, preguntas_filtradas[st.session_state.pregunta_actual].subtopic, preguntas_filtradas[st.session_state.pregunta_actual].complexity)
        st.write(preguntas_filtradas[st.session_state.pregunta_actual].respuesta_P2) 
            
        if st.session_state.get("consent", False):
            log_event(st.session_state["username"], "answer_revealed", {
            "question_id": preguntas_filtradas[st.session_state.pregunta_actual].no_pregunta
            })

    #Function to display the Answer Explanation for the "Quiero ver la respuesta" button
    def on_button_click():
        st.session_state.mostrar_respuesta = True

    #Function to generate the questions
    def generate_questions():
        st.markdown('<h3 style="font-size:18px;">Pregunta</h3>', unsafe_allow_html=True) #Title Pregunta
        st.write(preguntas_filtradas[st.session_state.pregunta_actual].pregunta) #Write the statement question
        filtrar_imagenes_preguntas(preguntas_filtradas[st.session_state.pregunta_actual].no_pregunta, preguntas_filtradas[st.session_state.pregunta_actual].version, preguntas_filtradas[st.session_state.pregunta_actual].subtopic, preguntas_filtradas[st.session_state.pregunta_actual].complexity) #Select the image
         

        st.markdown('<h3 style="font-size:18px;">Respuestas</h3>', unsafe_allow_html=True) #Title Respuestas
        st.markdown('<p style="font-size: 14px;">Ingrese sus respuestas con dos decimales</p>', unsafe_allow_html=True) #Title of instructions
        response1, response2, response3 = render_input_widgets(preguntas_filtradas,st.session_state.pregunta_actual) #Create boxes to the user's answers

        st.markdown('<h3 style="font-size:18px;">Acciones</h3>', unsafe_allow_html=True) #Title Acciones
            
        #Create butttons
        respuesta_pressed, ayuda_pressed, repetir_pressed, nuevo_pressed = st.columns(4)
        respuesta_clicked = respuesta_pressed.button("Verificar respuesta", key=f"respuesta_button_{st.session_state.pregunta_actual}", help="Verificación de la respuesta", use_container_width=True)
        ayuda_clicked = ayuda_pressed.button("Ayuda", key=f"ayuda_button_{st.session_state.pregunta_actual}", help="Ayuda para la solución", use_container_width=True)
        repetir_pressed.button("Nueva versión", key="nueva_version_button", help="Genera una nueva versión del problema", use_container_width=True, on_click=nueva_version_callback)
        nuevo_pressed.button("Siguiente problema", key=f"nuevo_problema_button{st.session_state.pregunta_actual}", help="Genera un nuevo problema", use_container_width=True, on_click=nuevo_problema_callback)

        if st.session_state.get("consent", False):
            log_event(st.session_state["username"], "question_viewed", {
            "question_id": preguntas_filtradas[st.session_state.pregunta_actual].no_pregunta,
            "version": preguntas_filtradas[st.session_state.pregunta_actual].version
            })

            return response1, response2, response3, respuesta_clicked, ayuda_clicked

    
    def generate_calculation_questions():
            
        response1, response2, response3, respuesta_clicked, ayuda_clicked = generate_questions()

        # "Verificar respuesta" button - Evaluation of the validity of the result input by user
        if respuesta_clicked:
            st.session_state.Intento += 1
            outputx, is_correct = resultado(preguntas_filtradas, response1, response2, response3, st.session_state.pregunta_actual)
            st.write(outputx)
                    
            difficulty = preguntas_filtradas[st.session_state.pregunta_actual].complexity
            used_help = st.session_state.get('ayuda_used', False)
            points_earned = calculate_points(difficulty, st.session_state.Intento, used_help)
                    
            if is_correct == 1:
                st.session_state.mostrar_respuesta = True
                log_event(st.session_state["username"], "points_earned", {"points": points_earned})
            elif is_correct == 0:
                if st.session_state.Intento > 3:
                    st.button(":pensive: Quiero ver la respuesta", key=f"ver_respuesta_button{st.session_state.pregunta_actual}", help="Permite ver la respuesta", on_click=on_button_click)
                    
            if st.session_state.get("consent", False):
                log_event(st.session_state["username"], "answer_submitted", {
                "question_id": preguntas_filtradas[st.session_state.pregunta_actual].no_pregunta,
                "attempt": st.session_state.Intento,
                "is_correct": is_correct,
                "points_earned": points_earned
                })
                
        if st.session_state.mostrar_respuesta:
            mostrar_respuesta()
            st.session_state.mostrar_respuesta = False
                            
        # "Ayuda" button - It shows helps 
        if ayuda_clicked:    
            butt_ayuda(preguntas_filtradas, st.session_state.pregunta_actual, ayuda_clicked)
            st.session_state.ayuda_used = True
    
    #=========================Functions to generate the theory questions============================
    def opciones_respuesta():
        opcion_seleccionada = st.radio("",options=[conceptuales_filtradas[st.session_state.pregunta_actual].opcion_1, conceptuales_filtradas[st.session_state.pregunta_actual].opcion_2, conceptuales_filtradas[st.session_state.pregunta_actual].opcion_3, conceptuales_filtradas[st.session_state.pregunta_actual].opcion_4]) 
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
        nuevo_problema_teoria = st.session_state.pregunta_actual + 1
        while nuevo_problema_teoria < len(conceptuales_filtradas) and conceptuales_filtradas[nuevo_problema_teoria].no_pregunta == conceptuales_filtradas[st.session_state.pregunta_actual].no_pregunta:
            nuevo_problema_teoria += 1
        if nuevo_problema_teoria >= len(conceptuales_filtradas):
            nuevo_problema_teoria = 0
        st.session_state.pregunta_actual = nuevo_problema_teoria

    #Función para mostrar la imagen de la pregunta de teoría
    def filtrar_imagenes_teoria(pregunta_no, subtopic):
        left_col, center_col, right_col = st.columns(3)
        with center_col:
            if subtopic == "Vectores":
                    if pregunta_no == 2 or pregunta_no == 3: 
                        st.image(teoria_preguntas[0], width=200)
                    if pregunta_no == 4: 
                        st.image(teoria_preguntas[1], width=300)  
                    if pregunta_no == 7: 
                        st.image(teoria_preguntas[2], width=250)
                    if pregunta_no == 8: 
                        st.image(teoria_preguntas[3], width=250)  
        return


    def generate_theory_questions():
        st.markdown('<h3 style="font-size:18px;">Pregunta</h3>', unsafe_allow_html=True) #Title Pregunta
        st.write(conceptuales_filtradas[st.session_state.pregunta_actual].enunciado) #Write the statement question
        filtrar_imagenes_teoria(conceptuales_filtradas[st.session_state.pregunta_actual].no_pregunta, conceptuales_filtradas[st.session_state.pregunta_actual].subtopic)
        #Answer options
        opcion_seleccionada = opciones_respuesta()

        #Buttons
        verificar_pressed, siguiente_pressed, col_3, col_4 = st.columns(4)
        verificar_clicked = verificar_pressed.button("Verificar respuesta",key=f"verificar_respuesta_teoria_button{st.session_state.pregunta_actual}", use_container_width=True, help="Verificación la respuesta")
        sproblema_clicked = siguiente_pressed.button("Siguiente problema", key=f"nuevo_problema_button{st.session_state.pregunta_actual}", help="Genera un nuevo problema", use_container_width=True, on_click=nuevo_problema_teoria_callback)

        # "Verificar respuesta" button - Evaluation of the validity of the result input by user
        if verificar_clicked:
            text_respuesta, is_correct = evaluacion_respuesta_teoria(conceptuales_filtradas, opcion_seleccionada, st.session_state.pregunta_actual)
            st.write(text_respuesta)
            if is_correct == 1:
                st.write(conceptuales_filtradas[st.session_state.pregunta_actual].respuesta_P1)

    def main():
        if way == "Práctica":
            generate_calculation_questions()
        elif way == "Teoría":
            generate_theory_questions()
    

    if __name__ == '__main__':  
        main() 
        # Cleanup
        if st.session_state.get("screen_record_consent", False):
            username = st.session_state.get("username", "unknown_user")
            stop_screen_recording(username)
                
        if st.session_state.get("consent", False):
            study_duration = int((datetime.now() - st.session_state.get("session_start_time", datetime.now())).total_seconds() / 60)
            log_event(st.session_state["username"], "study_time", study_duration)
            log_event(st.session_state["username"], "session_end", {})

        # Don't forget to set the session start time when the user logs in:
        if "authenticated" in st.session_state and st.session_state["authenticated"]:
            if "session_start_time" not in st.session_state:
                st.session_state.session_start_time = datetime.now()
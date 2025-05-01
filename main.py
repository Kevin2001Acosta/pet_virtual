import streamlit as st
from langchain_openai import ChatOpenAI
import config

api = config.OPENAI_API_KEY

llm = ChatOpenAI(
    model="gpt-3.5-turbo", temperature=0, openai_api_key=api)

st.title("Chatbot de prueba")

messages = [("system", "Eres un amigo y eres una mascota gato hablante que habla como amigo")]

if "messages" not in st.session_state:
    st.session_state.messages = []


# mostrar los mensajes del chat al recargar la app
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
# reaccionar a la entrada del usuario
if prompt := st.chat_input("¿Cómo puedo ayudarte?"):
    # mostrar mensaje del usuario en el contenedor
    st.chat_message("user").markdown(prompt)
    
    # agregar el mensaje al historial de chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    messages.append(['human', prompt])
    
    response = llm.invoke(messages).content
    
    # mostrar respuesta del asistente en el contenedor de mensaje del chat
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # agregar respuesta del asistente al historial del chat
    st.session_state.messages.append({"role": "assistant", "content": response})
    

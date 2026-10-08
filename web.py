import streamlit as st
from streamlit import session_state

import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title('My Todo App!!!')
st.header("some text for testing")
st.subheader('This is my first web app in python')
st.write('This is a simple test app in python')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del session_state[todo]
        st.rerun()

st.text_input(label='', placeholder='Enter a todo....',
              on_change=add_todo, key="new_todo")



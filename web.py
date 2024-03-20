import streamlit as st
import functions

todos = functions.get_todos()

def add_todo(filepath="todos.txt"):
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()


st.title("My todo app")
st.subheader("My subtitle")
st.write("This app is to increase productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", placeholder="Add new to do ...",
              on_change=add_todo, key='new_todo')

st.session_state
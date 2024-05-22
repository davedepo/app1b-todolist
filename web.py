import streamlit as st
import functions

todos = functions.get_todos()


# Callback function to add a new todo
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("Web App")
st.subheader("It is a Todos list maintained on webpage")
st.write("You can use to organize your deliverables")

# Assuming 'todos' is a list of tasks
for index, todo in enumerate(todos):
    # Convert 'todo' to string and create a checkbox with a unique key
    checkbox_items = st.checkbox(str(todo), key=todo)
    if checkbox_items:
        # Process the checked item
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# Input for new todo
st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo"
              )

# to check the dic type value for each key in for-loop list
# st.session_state

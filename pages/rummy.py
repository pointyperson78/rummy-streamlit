import streamlit as st
if "actions" not in st.session_state:
    st.session_state.actions = []

player = st.selectbox(
    'Player:'
    ,('Player 1', 'Player 2', 'Player 3', 'Player 4'),
    index = None
)
type = st.selectbox(
    'Type of Action'
    ,('Pick up','Put down'),
    index = None
)
num = st.selectbox(
    'Number:'
    ,('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King'),
    index = None
)
suit = st.selectbox(
    'Suit:'
    ,('Spades','Clubs','Hearts','Diamonds'),
    index = None
)

button = st.button('Add')
if button:
   action = {"player": player, "type"=type "number":num, "suit":suit,} 
   st.session_state.actions.append(action)
   player = None
st.write(st.session_state.actions)


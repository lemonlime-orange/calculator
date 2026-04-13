import streamlit as st
import math

st.set_page_config(page_title="Engineering Calculator", page_icon="🧮", layout="centered")

# -------- 스타일 --------
st.markdown("""
<style>
.block-container {padding: 1.5rem;}
.display {
    background-color: #1c1f26;
    color: #00ffcc;
    padding: 20px;
    border-radius: 10px;
    text-align: right;
    font-size: 32px;
    font-weight: bold;
    margin-bottom: 10px;
}
.small-display {
    color: #888;
    font-size: 14px;
    text-align: right;
}
button {
    height: 60px;
    font-size: 18px !important;
    border-radius: 8px !important;
}
</style>
""", unsafe_allow_html=True)

# -------- 상태 --------
if "expression" not in st.session_state:
    st.session_state.expression = ""
if "mode" not in st.session_state:
    st.session_state.mode = "DEG"

# -------- 디스플레이 --------
st.markdown(f'<div class="small-display">Mode: {st.session_state.mode}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="display">{st.session_state.expression if st.session_state.expression else "0"}</div>', unsafe_allow_html=True)

# -------- 함수 --------
def add(val):
    st.session_state.expression += str(val)

def clear():
    st.session_state.expression = ""

def backspace():
    st.session_state.expression = st.session_state.expression[:-1]

def toggle_mode():
    st.session_state.mode = "RAD" if st.session_state.mode == "DEG" else "DEG"

def calculate():
    try:
        expr = st.session_state.expression.replace("^", "**")
        if st.session_state.mode == "DEG":
            expr = expr.replace("sin(", "math.sin(math.radians(")
            expr = expr.replace("cos(", "math.cos(math.radians(")
            expr = expr.replace("tan(", "math.tan(math.radians(")
        else:
            expr = expr.replace("sin(", "math.sin(")
            expr = expr.replace("cos(", "math.cos(")
            expr = expr.replace("tan(", "math.tan(")
        result = eval(expr)
        st.session_state.expression = str(result)
    except:
        st.session_state.expression = "Error"

# -------- 버튼 레이아웃 --------
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "%", "+"],
    ["(", ")", "^", "="],
]

for row in buttons:
    cols = st.columns(4)
    for i, val in enumerate(row):
        if val == "=":
            cols[i].button(val, on_click=calculate, use_container_width=True)
        else:
            cols[i].button(val, on_click=add, args=(val,), use_container_width=True)

# -------- 추가 기능 --------
col1, col2, col3, col4 = st.columns(4)
col1.button("C", on_click=clear, use_container_width=True)
col2.button("⌫", on_click=backspace, use_container_width=True)
col3.button("DEG/RAD", on_click=toggle_mode, use_container_width=True)

# 공학 함수
if col4.button("√", use_container_width=True):
    st.session_state.expression += "math.sqrt("

col5, col6, col7 = st.columns(3)
if col5.button("sin", use_container_width=True):
    st.session_state.expression += "sin("
if col6.button("cos", use_container_width=True):
    st.session_state.expression += "cos("
if col7.button("tan", use_container_width=True):
    st.session_state.expression += "tan("

col8, col9 = st.columns(2)
if col8.button("log", use_container_width=True):
    st.session_state.expression += "math.log10("
if col9.button("ln", use_container_width=True):
    st.session_state.expression += "math.log("

st.markdown("---")
st.caption("Advanced Engineering Calculator (Casio-style)")

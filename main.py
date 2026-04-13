import streamlit as st
import math

st.set_page_config(page_title="Casio fx-570 Style", page_icon="🧮", layout="centered")

# -------- 스타일 (카시오 느낌) --------
st.markdown("""
<style>
.block-container {padding: 1rem; max-width: 420px; margin: auto;}
.preview {
    color: #aaa;
    font-size: 12px;
    text-align: right;
}
.display {
    background-color: #d9e6d2;
    color: #000;
    padding: 15px;
    border-radius: 5px;
    text-align: right;
    font-size: 28px;
    font-family: 'Courier New', monospace;
    margin-bottom: 8px;
    border: 2px solid #333;
}
button {
    height: 55px;
    font-size: 16px !important;
    border-radius: 6px !important;
}

/* 버튼 색상 구분 */
div.stButton:nth-child(n) > button {
    background-color: #2f2f2f;
    color: white;
}

/* 숫자 버튼 */
button:contains("0"),
button:contains("1"),
button:contains("2"),
button:contains("3"),
button:contains("4"),
button:contains("5"),
button:contains("6"),
button:contains("7"),
button:contains("8"),
button:contains("9") {
    background-color: #444 !important;
}

</style>
""", unsafe_allow_html=True)

# -------- 상태 --------
if "expr" not in st.session_state:
    st.session_state.expr = ""
if "preview" not in st.session_state:
    st.session_state.preview = ""
if "mode" not in st.session_state:
    st.session_state.mode = "DEG"

# -------- 디스플레이 --------
st.markdown(f'<div class="preview">{st.session_state.preview}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="display">{st.session_state.expr if st.session_state.expr else "0"}</div>', unsafe_allow_html=True)

# -------- 함수 --------
def add(x):
    st.session_state.expr += str(x)

def clear():
    st.session_state.expr = ""
    st.session_state.preview = ""

def back():
    st.session_state.expr = st.session_state.expr[:-1]

def toggle():
    st.session_state.mode = "RAD" if st.session_state.mode == "DEG" else "DEG"

def calc():
    try:
        exp = st.session_state.expr.replace("^", "**")
        raw = st.session_state.expr

        if st.session_state.mode == "DEG":
            exp = exp.replace("sin(", "math.sin(math.radians(")
            exp = exp.replace("cos(", "math.cos(math.radians(")
            exp = exp.replace("tan(", "math.tan(math.radians(")

        result = eval(exp)
        st.session_state.preview = raw + " ="
        st.session_state.expr = str(result)
    except:
        st.session_state.expr = "Error"

# -------- 상단 (SHIFT 느낌 간단 구현) --------
t1, t2, t3, t4 = st.columns(4)
t1.button("SHIFT", use_container_width=True)
t2.button("MODE", on_click=toggle, use_container_width=True)
t3.button("C", on_click=clear, use_container_width=True)
t4.button("⌫", on_click=back, use_container_width=True)

# -------- 함수 줄 --------
f1, f2, f3, f4 = st.columns(4)
f1.button("sin", on_click=add, args=("sin(",), use_container_width=True)
f2.button("cos", on_click=add, args=("cos(",), use_container_width=True)
f3.button("tan", on_click=add, args=("tan(",), use_container_width=True)
f4.button("^", on_click=add, args=("^",), use_container_width=True)

f5, f6, f7, f8 = st.columns(4)
f5.button("log", on_click=add, args=("math.log10(",), use_container_width=True)
f6.button("ln", on_click=add, args=("math.log(",), use_container_width=True)
f7.button("(", on_click=add, args=("(",), use_container_width=True)
f8.button(")", on_click=add, args=(")",), use_container_width=True)

# -------- 숫자 --------
nums = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["0",".","%","+"],
]

for row in nums:
    cols = st.columns(4)
    for i,v in enumerate(row):
        cols[i].button(v, on_click=add, args=(v,), use_container_width=True)

# -------- 계산 --------
st.button("=", on_click=calc, use_container_width=True)

st.caption("Casio fx-570 Style Calculator UI")

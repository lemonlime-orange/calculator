import streamlit as st
import math

st.set_page_config(page_title="Neon Engineering Calculator", page_icon="🧮", layout="centered")

# -------- 스타일 (간지 네온 UI) --------
st.markdown("""
<style>
body {
    background-color: #0a0a0f;
}
.block-container {
    padding: 1.5rem;
    max-width: 420px;
    margin: auto;
}

.display {
    background: linear-gradient(145deg, #0f172a, #020617);
    color: #22c55e;
    padding: 20px;
    border-radius: 12px;
    text-align: right;
    font-size: 34px;
    font-weight: bold;
    margin-bottom: 10px;
    box-shadow: 0 0 15px rgba(34,197,94,0.5);
}

.sub {
    color: #94a3b8;
    font-size: 12px;
    text-align: right;
    margin-bottom: 5px;
}

button {
    height: 60px;
    font-size: 18px !important;
    border-radius: 10px !important;
    background: #111827 !important;
    color: white !important;
    border: 1px solid #1f2937 !important;
    transition: 0.2s;
}

button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 10px #22c55e;
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
st.markdown(f'<div class="sub">{st.session_state.preview}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="display">{st.session_state.expr if st.session_state.expr else "0"}</div>', unsafe_allow_html=True)

# -------- 함수 --------
def add(v):
    st.session_state.expr += str(v)

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

# -------- 상단 --------
t1, t2, t3, t4 = st.columns(4)
t1.button("C", on_click=clear, use_container_width=True)
t2.button("⌫", on_click=back, use_container_width=True)
t3.button("MODE", on_click=toggle, use_container_width=True)
t4.button("√", on_click=lambda: add("math.sqrt("), use_container_width=True)

# -------- 함수 --------
f1, f2, f3, f4 = st.columns(4)
f1.button("sin", on_click=lambda: add("sin("), use_container_width=True)
f2.button("cos", on_click=lambda: add("cos("), use_container_width=True)
f3.button("tan", on_click=lambda: add("tan("), use_container_width=True)
f4.button("^", on_click=lambda: add("^"), use_container_width=True)

f5, f6, f7, f8 = st.columns(4)
f5.button("log", on_click=lambda: add("math.log10("), use_container_width=True)
f6.button("ln", on_click=lambda: add("math.log("), use_container_width=True)
f7.button("(", on_click=lambda: add("("), use_container_width=True)
f8.button(")", on_click=lambda: add(")"), use_container_width=True)

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

st.caption("🔥 Neon Style Engineering Calculator")

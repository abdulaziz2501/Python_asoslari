import streamlit as st
import math

# Sahifa konfiguratsiyasi
st.set_page_config(
    page_title="Calculator",
    page_icon="🧮",
    layout="centered"
)

# CSS stillar
st.markdown("""
<style>
.calculator-title {
    text-align: center;
    color: #1f77b4;
    font-size: 3em;
    margin-bottom: 30px;
}

.result-display {
    background-color: #f0f2f6;
    padding: 30px;
    border-radius: 15px;
    font-size: 2.5em;
    text-align: center;
    margin-bottom: 30px;
    border: 3px solid #1f77b4;
    font-weight: bold;
}

/* Button stillarini kattalashtirish */
.stButton button {
    width: 100% !important;
    height: 80px !important;
    font-size: 24px !important;
    font-weight: bold !important;
    border-radius: 15px !important;
    border: 2px solid #ddd !important;
    margin: 3px !important;
    transition: all 0.2s !important;
}

.stButton button:hover {
    background-color: #1f77b4 !important;
    color: white !important;
    transform: scale(1.05) !important;
}

/* Raqam tugmalari */
.stButton button:nth-child(1) {
    background-color: #e8f4fd !important;
}

/* Operator tugmalari */
.stButton button[title*="÷"], 
.stButton button[title*="×"], 
.stButton button[title*="-"], 
.stButton button[title*="+"], 
.stButton button[title*="="] {
    background-color: #ff6b6b !important;
    color: white !important;
}

/* C tugmasi */
.stButton button[title*="C"] {
    background-color: #ff4757 !important;
    color: white !important;
}

/* Qo'shimcha funksiya tugmalari */
.stButton button[title*="√"], 
.stButton button[title*="%"], 
.stButton button[title*="^"] {
    background-color: #ffa502 !important;
    color: white !important;
}

/* Container o'lchamini kattalashtirish */
.main .block-container {
    max-width: 600px !important;
    padding-top: 2rem !important;
}

/* Column bo'shliqlarini kamaytirish */
.stColumns {
    gap: 0.2rem !important;
}
</style>
""", unsafe_allow_html=True)


# Sarlavha
st.markdown('<h1 class="calculator-title">🧮 Calculator</h1>', unsafe_allow_html=True)

# Session state inizializatsiya
if 'result' not in st.session_state:
    st.session_state.result = 0
if 'current_input' not in st.session_state:
    st.session_state.current_input = ""
if 'operator' not in st.session_state:
    st.session_state.operator = ""
if 'previous_number' not in st.session_state:
    st.session_state.previous_number = 0
if 'display' not in st.session_state:
    st.session_state.display = "0"

# Natijani ko'rsatish
st.markdown(f'<div class="result-display">{st.session_state.display}</div>', unsafe_allow_html=True)


# Calculator funksiyalari
def clear():
    st.session_state.result = 0
    st.session_state.current_input = ""
    st.session_state.operator = ""
    st.session_state.previous_number = 0
    st.session_state.display = "0"


def add_digit(digit):
    if st.session_state.display == "0" or st.session_state.display == "Error":
        st.session_state.display = str(digit)
    else:
        st.session_state.display += str(digit)


def add_operator(op):
    try:
        if st.session_state.operator and st.session_state.display:
            calculate()
        st.session_state.previous_number = float(st.session_state.display)
        st.session_state.operator = op
        st.session_state.display = "0"
    except:
        st.session_state.display = "Error"


def calculate():
    try:
        current = float(st.session_state.display)
        previous = st.session_state.previous_number

        if st.session_state.operator == "+":
            result = previous + current
        elif st.session_state.operator == "-":
            result = previous - current
        elif st.session_state.operator == "×":
            result = previous * current
        elif st.session_state.operator == "÷":
            if current == 0:
                st.session_state.display = "Error"
                return
            result = previous / current
        elif st.session_state.operator == "^":
            result = previous ** current
        else:
            return

        # Natijani formatlash
        if result == int(result):
            st.session_state.display = str(int(result))
        else:
            st.session_state.display = f"{result:.8f}".rstrip('0').rstrip('.')

        st.session_state.operator = ""
        st.session_state.previous_number = 0
    except:
        st.session_state.display = "Error"


def add_decimal():
    if "." not in st.session_state.display:
        st.session_state.display += "."


def square_root():
    try:
        current = float(st.session_state.display)
        if current < 0:
            st.session_state.display = "Error"
        else:
            result = math.sqrt(current)
            if result == int(result):
                st.session_state.display = str(int(result))
            else:
                st.session_state.display = f"{result:.8f}".rstrip('0').rstrip('.')
    except:
        st.session_state.display = "Error"


def percentage():
    try:
        current = float(st.session_state.display)
        result = current / 100
        st.session_state.display = str(result)
    except:
        st.session_state.display = "Error"


# Calculator tugmalari
col1, col2, col3, col4 = st.columns(4)

# Birinchi qator
with col1:
    if st.button("C", key="clear"):
        clear()
        st.rerun()

with col2:
    if st.button("√", key="sqrt"):
        square_root()
        st.rerun()

with col3:
    if st.button("%", key="percent"):
        percentage()
        st.rerun()

with col4:
    if st.button("÷", key="divide"):
        add_operator("÷")
        st.rerun()

# Ikkinchi qator
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7", key="7"):
        add_digit(7)
        st.rerun()

with col2:
    if st.button("8", key="8"):
        add_digit(8)
        st.rerun()

with col3:
    if st.button("9", key="9"):
        add_digit(9)
        st.rerun()

with col4:
    if st.button("×", key="multiply"):
        add_operator("×")
        st.rerun()

# Uchinchi qator
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("4", key="4"):
        add_digit(4)
        st.rerun()

with col2:
    if st.button("5", key="5"):
        add_digit(5)
        st.rerun()

with col3:
    if st.button("6", key="6"):
        add_digit(6)
        st.rerun()

with col4:
    if st.button("-", key="subtract"):
        add_operator("-")
        st.rerun()

# To'rtinchi qator
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("1", key="1"):
        add_digit(1)
        st.rerun()

with col2:
    if st.button("2", key="2"):
        add_digit(2)
        st.rerun()

with col3:
    if st.button("3", key="3"):
        add_digit(3)
        st.rerun()

with col4:
    if st.button("+", key="add"):
        add_operator("+")
        st.rerun()

# Beshinchi qator
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("0", key="0"):
        add_digit(0)
        st.rerun()

with col2:
    if st.button(".", key="decimal"):
        add_decimal()
        st.rerun()

with col3:
    if st.button("^", key="power"):
        add_operator("^")
        st.rerun()

with col4:
    if st.button("=", key="equals"):
        calculate()
        st.rerun()

# Qo'shimcha ma'lumot
st.markdown("---")
st.markdown("""
### 🔧 Qo'llanma:
- **Raqamlar**: 0-9 tugmalarini bosing
- **Amallar**: +, -, ×, ÷, ^ (daraja)
- **C**: Hammasini tozalash
- **√**: Kvadrat ildiz
- **%**: Foiz
- **=**: Natijani hisoblash
""")
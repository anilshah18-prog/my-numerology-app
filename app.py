import streamlit as st

# 1. Chaldean Letter Mapping
char_map = {
    'A': 1, 'I': 1, 'J': 1, 'Q': 1, 'Y': 1,
    'B': 2, 'K': 2, 'R': 2,
    'C': 3, 'G': 3, 'L': 3, 'S': 3,
    'D': 4, 'M': 4, 'T': 4,
    'E': 5, 'H': 5, 'N': 5, 'X': 5,
    'U': 6, 'V': 6, 'W': 6,
    'O': 7, 'Z': 7,
    'F': 8, 'P': 8
}

# 2. Planetary (Graha) Data
graha_data = {
    1: "Sun (Surya)",
    2: "Moon (Chandra) - Negative",
    3: "Jupiter (Guru)",
    4: "Rahu (Sun Negative)",
    5: "Mercury (Budh)",
    6: "Venus (Shukra)",
    7: "Ketu (Neptune)",
    8: "Saturn (Shani)",
    9: "Mars (Mangal)"
}

# 3. Maitri (Compatibility) Data
maitri_data = {
    1: {"Friendly": "5, 6", "Neutral": "3, 7, 9", "Enemy": "2, 4, 8"},
    2: {"Friendly": "7", "Neutral": "5, 8", "Enemy": "1, 3, 4, 6, 9"},
    3: {"Friendly": "7", "Neutral": "1, 5", "Enemy": "2, 4, 6, 8, 9"},
    4: {"Friendly": "7", "Neutral": "6, 8", "Enemy": "1, 2, 3, 5, 9"},
    5: {"Friendly": "1, 8", "Neutral": "2, 3, 7", "Enemy": "4, 6, 9"},
    6: {"Friendly": "1, 8", "Neutral": "4, 7, 9", "Enemy": "2, 3, 5"},
    7: {"Friendly": "2, 3, 5, 9", "Neutral": "1, 5, 6, 8", "Enemy": "-"},
    8: {"Friendly": "5, 6", "Neutral": "2, 4, 7", "Enemy": "1, 3, 9"},
    9: {"Friendly": "7", "Neutral": "4, 6", "Enemy": "2, 3, 4, 5, 8"}
}

def reduce_number(n):
    """Helper to reduce any number to a single digit (1-9)."""
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

# --- Web Interface Design ---
st.set_page_config(page_title="Complete Numerology Report", layout="wide")

st.title("🔮 Full Numerology Report")
st.write("Calculations based on Name and Date of Birth using Chaldean & Vedic systems.")

# Input Section
with st.container():
    col_in1, col_in2 = st.columns(2)
    with col_in1:
        name_input = st.text_input("Enter Full Name:", placeholder="e.g. ANIL")
    with col_in2:
        dob_input = st.date_input("Select Date of Birth:", min_value=None)

if name_input and dob_input:
    # --- NAME CALCULATIONS ---
    clean_name = name_input.upper().replace(" ", "")
    name_values = [char_map[c] for c in clean_name if c in char_map]
    name_total = sum(name_values)
    name_destiny = reduce_number(name_total)

    # --- DOB CALCULATIONS ---
    day = dob_input.day
    month = dob_input.month
    year = dob_input.year
    
    # Moolank (Birth Number)
    moolank = reduce_number(day)
    
    # Bhagyank (Destiny Number)
    full_dob_sum = sum(int(d) for d in (str(day).zfill(2) + str(month).zfill(2) + str(year)))
    bhagyank = reduce_number(full_dob_sum)

    st.divider()

    # --- DISPLAY IN THREE COLUMNS ---
    col1, col2, col3 = st.columns(3)

    # Column 1: From Name
    with col1:
        st.header("👤 From Name")
        st.metric("Name Total", name_total)
        st.metric("Name Destiny No.", name_destiny)
        st.write(f"**Ruling Graha:**\n{graha_data[name_destiny]}")
        st.info(f"**Compatibility:**\nFriendly: {maitri_data[name_destiny]['Friendly']}\nEnemy: {maitri_data[name_destiny]['Enemy']}")

    # Column 2: From Birth Date (Moolank)
    with col2:
        st.header("📅 Birth Number")
        st.subheader(f"(Moolank: {moolank})")
        st.write("Derived from the day of birth.")
        st.metric("Moolank", moolank)
        st.write(f"**Ruling Graha:**\n{graha_data[moolank]}")
        st.success(f"**Compatibility:**\nFriendly: {maitri_data[moolank]['Friendly']}\nEnemy: {maitri_data[moolank]['Enemy']}")

    # Column 3: From Birth Date (Bhagyank)
    with col3:
        st.header("🌟 Destiny Number")
        st.subheader(f"(Bhagyank: {bhagyank})")
        st.write("Derived from full date of birth.")
        st.metric("Bhagyank", bhagyank)
        st.write(f"**Ruling Graha:**\n{graha_data[bhagyank]}")
        st.warning(f"**Compatibility:**\nFriendly: {maitri_data[bhagyank]['Friendly']}\nEnemy: {maitri_data[bhagyank]['Enemy']}")

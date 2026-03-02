import streamlit as st

# 1. Chaldean Letter Mapping [cite: 1, 2]
# Source: table for numerology app.pdf
char_map = {
    'A': 1, 'I': 1, 'J': 1, 'Q': 1, 'Y': 1,  # [cite: 3]
    'B': 2, 'K': 2, 'R': 2,                  # [cite: 5, 6, 7]
    'C': 3, 'G': 3, 'L': 3, 'S': 3,          # [cite: 8, 9]
    'D': 4, 'M': 4, 'T': 4,                  # [cite: 10, 11]
    'E': 5, 'H': 5, 'N': 5, 'X': 5,          # [cite: 12, 13]
    'U': 6, 'V': 6, 'W': 6,                  # [cite: 14, 15]
    'O': 7, 'Z': 7,                          # [cite: 16, 17]
    'F': 8, 'P': 8                           # [cite: 18]
}

# 2. Planetary (Graha) & Rashi Data [cite: 19, 20]
# Source: table for numerology app.pdf & numerology_number_graha.jpeg
graha_data = {
    1: "Sun (Surya) | Rashi: Sih",                                # [cite: 22]
    2: "Moon (Chandra) - Negative | Rashi: Kark",                 # [cite: 23]
    3: "Jupiter (Guru) | Rashi: Meen and Dhan",                   # [cite: 24]
    4: "Negative Sun + Harshal | Rashi: Sih",                     # [cite: 25]
    5: "Mercury (Budh) | Rashi: Mithun and Kanya",                # [cite: 26]
    6: "Venus (Shukra) | Rashi: Tula and Vrushabh",               # [cite: 27]
    7: "Positive Chandra + Positive Neptune | Rashi: Kark",       # [cite: 28]
    8: "Saturn (Shani) | Rashi: Makar and Kumbh",                 # [cite: 29]
    9: "Mars (Mangal) | Rashi: Mesh and Vruschik"                 # [cite: 30]
}

# 3. Maitri (Compatibility) Data [cite: 31, 33]
# Source: numerology_number_maitri.jpeg & table for numerology app.pdf
# Note: 'Neutral' represents 'Sam' [cite: 32]
maitri_data = {
    1: {"Friendly": "5, 6", "Enemy": "3, 7, 9", "Neutral": "2, 4, 8"},       # 
    2: {"Friendly": "7", "Enemy": "5, 8", "Neutral": "1, 3, 4, 6, 9"},       # 
    3: {"Friendly": "7", "Enemy": "1, 5", "Neutral": "2, 4, 6, 8, 9"},       # [cite: 36]
    4: {"Friendly": "7", "Enemy": "6, 8", "Neutral": "1, 2, 3, 5, 9"},       # [cite: 36]
    5: {"Friendly": "1, 8", "Enemy": "2, 3, 7", "Neutral": "4, 6, 9"},      # [cite: 36]
    6: {"Friendly": "1, 8", "Enemy": "4, 7, 9", "Neutral": "2, 3, 5"},      # [cite: 36]
    7: {"Friendly": "2, 3, 4, 9", "Enemy": "1, 5, 6, 8", "Neutral": "-"},    # [cite: 37]
    8: {"Friendly": "5, 6", "Enemy": "2, 4, 7", "Neutral": "1, 3, 9"},      # [cite: 38]
    9: {"Friendly": "7", "Enemy": "1, 6", "Neutral": "2, 3, 4, 5, 8"}       # [cite: 39]
}

def reduce_number(n):
    """Reduces a number to a single digit (1-9)."""
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

# --- UI Setup ---
st.set_page_config(page_title="Chaldean Numerology Pro", layout="wide")
st.title("🔮 Advanced Chaldean Numerology")

col_in1, col_in2 = st.columns(2)
with col_in1:
    name_input = st.text_input("Enter Full Name:", placeholder="e.g. ANIL")
with col_in2:
    dob_str = st.text_input("Enter Birth Date (DD/MM/YYYY):", placeholder="01/09/1969")

if name_input and dob_str:
    try:
        # Date Parsing
        date_parts = dob_str.split('/')
        day_val = int(date_parts[0])
        month_val = int(date_parts[1])
        year_val = int(date_parts[2])
        
        # Calculations
        moolank = reduce_number(day_val)
        full_digits = str(day_val) + str(month_val) + str(year_val)
        bhagyank = reduce_number(sum(int(d) for d in full_digits if d.isdigit()))
        
        clean_name = name_input.upper().replace(" ", "")
        name_total = sum(char_map[c] for c in clean_name if c in char_map)
        name_destiny = reduce_number(name_total)

        st.divider()
        c1, c2, c3 = st.columns(3)

        # Reusable Display Function
        def display_results(column, title, sub, val, total=None):
            with column:
                st.subheader(title)
                st.caption(sub)
                if total: st.metric("Total", total)
                st.metric("Number", val)
                st.write(f"**Graha Info:**\n{graha_data[val]}")
                st.write("---")
                st.success(f"**Friendly:** {maitri_data[val]['Friendly']}")
                st.info(f"**Neutral (Sam):** {maitri_data[val]['Neutral']}")
                st.error(f"**Enemy:** {maitri_data[val]['Enemy']}")

        display_results(c1, "👤 Name Analysis", "Name-based vibrations", name_destiny, name_total)
        display_results(c2, "📅 Birth Number", "Moolank (Day of Birth)", moolank)
        display_results(c3, "🌟 Destiny Number", "Bhagyank (Full Date Sum)", bhagyank)

    except (ValueError, IndexError):
        st.error("Format Error: Please enter date as DD/MM/YYYY")

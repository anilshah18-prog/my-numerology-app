import streamlit as st

# 1. Chaldean Letter Mapping [cite: 1, 2, 3, 4, 5, 12, 18]
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

# 2. Planetary (Graha) & Rashi Data [cite: 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30]
graha_data = {
    1: "Sun (Surya) | Rashi: Sih",
    2: "Moon (Chandra) - Negative | Rashi: Kark",
    3: "Jupiter (Guru) | Rashi: Meen and Dhan",
    4: "Negative Sun + Harshal | Rashi: Sih",
    5: "Mercury (Budh) | Rashi: Mithun and Kanya",
    6: "Venus (Shukra) | Rashi: Tula and Vrushabh",
    7: "Positive Chandra + Positive Neptune | Rashi: Kark",
    8: "Saturn (Shani) | Rashi: Makar and Kumbh",
    9: "Mars (Mangal) | Rashi: Mesh and Vruschik"
}

# 3. Maitri (Compatibility) Data [cite: 33, 35, 36, 37, 38, 39]
maitri_data = {
    1: {"Friendly": "5, 6", "Enemy": "3, 7, 9", "Neutral": "2, 4, 8"},
    2: {"Friendly": "7", "Enemy": "5, 8", "Neutral": "1, 3, 4, 6, 9"},
    3: {"Friendly": "7", "Enemy": "1, 5", "Neutral": "2, 4, 6, 8, 9"},
    4: {"Friendly": "7", "Enemy": "6, 8", "Neutral": "1, 2, 3, 5, 9"},
    5: {"Friendly": "1, 8", "Enemy": "2, 3, 7", "Neutral": "4, 6, 9"},
    6: {"Friendly": "1, 8", "Enemy": "4, 7, 9", "Neutral": "2, 3, 5"},
    7: {"Friendly": "2, 3, 4, 9", "Enemy": "1, 5, 6, 8", "Neutral": "-"},
    8: {"Friendly": "5, 6", "Enemy": "2, 4, 7", "Neutral": "1, 3, 9"},
    9: {"Friendly": "7", "Enemy": "1, 6", "Neutral": "2, 3, 4, 5, 8"}
}

def reduce_number_with_steps(n):
    steps = []
    current = n
    while current > 9:
        digits = [int(d) for d in str(current)]
        steps.append(f"{' + '.join(map(str, digits))} = {sum(digits)}")
        current = sum(digits)
    return current, steps

# --- UI Setup ---
st.set_page_config(page_title="Chaldean Numerology System", layout="wide")
st.title("🔮 Detailed Numerology Analysis")

col_in1, col_in2 = st.columns(2)
with col_in1:
    name_input = st.text_input("Enter Full Name:", placeholder="e.g. ANIL")
with col_in2:
    dob_str = st.text_input("Enter Birth Date (DD/MM/YYYY):", placeholder="01/09/1969")

if name_input and dob_str:
    try:
        # 1. Name Math
        clean_name = name_input.upper().replace(" ", "")
        name_values = [char_map[c] for c in clean_name if c in char_map]
        name_total = sum(name_values)
        name_destiny, name_steps = reduce_number_with_steps(name_total)

        # 2. DOB Parsing & Moolank Math
        date_parts = dob_str.split('/')
        day_val = int(date_parts[0])
        moolank, moolank_steps = reduce_number_with_steps(day_val)
        
        # 3. Bhagyank Math
        dob_digits = [int(d) for d in dob_str if d.isdigit()]
        bhagyank_total = sum(dob_digits)
        bhagyank, bhagyank_steps = reduce_number_with_steps(bhagyank_total)

        # --- Display Results ---
        st.divider()
        c1, c2, c3 = st.columns(3)

        def show_col(col, title, num, total=None):
            with col:
                st.subheader(title)
                if total: st.metric("Total", total)
                st.metric("Final Number", num)
                st.write(f"**Graha:** {graha_data[num]}")
                st.write("---")
                st.success(f"**Friendly:** {maitri_data[num]['Friendly']}")
                st.info(f"**Neutral (Sam):** {maitri_data[num]['Neutral']}")
                st.error(f"**Enemy:** {maitri_data[num]['Enemy']}")

        show_col(c1, "👤 Name Analysis", name_destiny, name_total)
        show_col(c2, "📅 Birth (Moolank)", moolank)
        show_col(c3, "🌟 Destiny (Bhagyank)", bhagyank)

        # --- SHOW CALCULATIONS AT THE END ---
        st.divider()
        st.subheader("📝 Calculation Summary")
        
        sum1, sum2, sum3 = st.columns(3)
        
        with sum1:
            st.write("**Name Calculation:**")
            st.write(f"{' + '.join(list(clean_name))}")
            st.write(f"{' + '.join(map(str, name_values))} = **{name_total}**")
            for step in name_steps: st.write(f"↪ {step}")

        with sum2:
            st.write("**Moolank Calculation:**")
            st.write(f"Day of Birth: **{day_val}**")
            for step in moolank_steps: st.write(f"↪ {step}")

        with sum3:
            st.write("**Bhagyank Calculation:**")
            st.write(f"{' + '.join(map(str, dob_digits))} = **{bhagyank_total}**")
            for step in bhagyank_steps: st.write(f"↪ {step}")

    except (ValueError, IndexError):
        st.error("Format Error: Use DD/MM/YYYY (e.g., 01/09/1969)")

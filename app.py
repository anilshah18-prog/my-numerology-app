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
    7: {"Friendly": "2, 3, 5, 9", "Neutral": "1, 5, 6, 8", "Enemy": "None"},
    8: {"Friendly": "5, 6", "Neutral": "2, 4, 7", "Enemy": "1, 3, 9"},
    9: {"Friendly": "7", "Neutral": "4, 6", "Enemy": "2, 3, 4, 5, 8"}
}

# --- GUI Interface ---
st.set_page_config(page_title="Advanced Numerology", page_icon="🔮")

st.title("🔮 Chaldean Numerology & Graha App")
st.write("Calculate your name number and discover its ruling planet and compatibility.")

name_input = st.text_input("Enter Name:", placeholder="Type name here...")

if name_input:
    # Processing
    clean_name = name_input.upper().replace(" ", "")
    individual_numbers = [char_map[c] for c in clean_name if c in char_map]
    total_sum = sum(individual_numbers)
    
    # Reduction to single digit
    final_digit = total_sum
    while final_digit > 9:
        final_digit = sum(int(d) for d in str(final_digit))

    # --- Results Display ---
    st.divider()
    
    # Row 1: Key Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Name Total", total_sum)
    col2.metric("Destiny Number", final_digit)
    col3.write(f"**Ruling Graha:** \n{graha_data[final_digit]}")

    # Row 2: Compatibility (Maitri)
    st.subheader(f"Compatibility for Number {final_digit}")
    m_info = maitri_data[final_digit]
    c1, c2, c3 = st.columns(3)
    c1.success(f"**Friendly:**\n{m_info['Friendly']}")
    c2.info(f"**Neutral:**\n{m_info['Neutral']}")
    c3.error(f"**Enemy:**\n{m_info['Enemy']}")

    # Row 3: Breakdown
    with st.expander("See Calculation Breakdown"):
        st.write(f"**Letters:** {' + '.join(list(clean_name))}")
        st.write(f"**Values:** {' + '.join(map(str, individual_numbers))}")
        if total_sum > 9:
            st.write(f"**Reduction:** {total_sum} → {' + '.join(list(str(total_sum)))} = {final_digit}")

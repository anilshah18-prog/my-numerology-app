import streamlit as st

# 1. Define the Chaldean Mapping
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

# --- Web Interface Design ---
st.set_page_config(page_title="Chaldean Numerology", page_icon="🔢")

st.title("🔢 Chaldean Numerology Calculator")
st.write("Enter a name below to calculate its numerical vibration based on your charts.")

# Input field
name_input = st.text_input("Enter Name:", placeholder="e.g. ANIL")

if name_input:
    name = name_input.upper().replace(" ", "")
    individual_numbers = []
    total_sum = 0

    for char in name:
        if char in char_map:
            num = char_map[char]
            individual_numbers.append(num)
            total_sum += num
    
    # Reduction logic
    final_digit = total_sum
    while final_digit > 9:
        final_digit = sum(int(digit) for digit in str(final_digit))

    # --- Display Results ---
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Sum", total_sum)
    with col2:
        st.metric("Final Number", final_digit)

    st.subheader("Calculation Breakdown")
    st.write(f"**Letters:** {' + '.join(list(name))}")
    st.write(f"**Values:** {' + '.join(map(str, individual_numbers))}")
    
    if total_sum > 9:
        st.info(f"The total {total_sum} reduces to {final_digit} (by adding digits together).")
    
    st.success(f"The final Numerology Number for **{name_input}** is **{final_digit}**")

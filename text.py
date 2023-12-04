# Streamlit app code
st.title("Entity Extraction App")
sentence_input = st.text_input("Enter a sentence:")

if st.button("Extract Entities"):
    if sentence_input:
        results = extract_entities(sentence_input)

        st.subheader("Extracted Entities:")
        for entity, label in results['entities']:
            st.write(f"{entity}: {label}")

        st.subheader("Addresses:")
        for address in results['addresses']:
            st.write(address)

        st.subheader("Emails:")
        for email in results['emails']:
            st.write(email)
    else:
        st.warning("Please enter a sentence.")

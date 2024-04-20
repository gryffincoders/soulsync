import streamlit as st

def sos():
    st.title("SoulSync SOS Assistant")
    st.write("If you're experiencing distress or emotional pain, use this tool to get immediate steps to help manage your condition.")

    # List of symptoms for the user to select from
    symptoms = {
        "Anxiety": "Take deep breaths, try grounding exercises, or use a meditation app.",
        "Panic Attack": "Find a quiet place, focus on slow breathing, and recognize that the panic will pass.",
        "Depression": "Reach out to a friend or family member, engage in an activity you enjoy, or practice mindfulness.",
        "Manic Episode": "Contact your healthcare provider, focus on getting rest, avoid stimulants like caffeine."
    }

    symptom_choice = st.selectbox("Select your current symptom:", list(symptoms.keys()))
    if st.button("Get Immediate Steps"):
        st.subheader("Steps to Follow:")
        st.write(symptoms[symptom_choice])

        # Additional advice or emergency contacts
        st.subheader("Emergency Contact:")
        st.write("If these steps do not help, or if you feel like you are in danger, please call emergency services or a mental health professional immediately.")
        st.markdown("🚨 **National Emergency Number:** Call [112](tel:112) or **Ambulance:** Call [102](tel:102) or your local emergency number.")

if __name__ == "__main__":
    sos()

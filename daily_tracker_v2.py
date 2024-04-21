import httpx
import asyncio
import streamlit as st
from datetime import datetime
import plotly.graph_objects as go
from openai import OpenAI, AsyncOpenAI
client = AsyncOpenAI(api_key="sk-proj-1iMn6aZTpQN4ir2njzLGT3BlbkFJFTea2xc0NZjfmEZtRzN6")


# openai.api_key = "YOUR-OWN-API-KEY"

def mental_health_check_in():
    st.write("## Mental Health Check-In")
    questions = [
        "How are you feeling today? (0 = Terrible, 10 = Great)",
        "How would you rate your level of serenity today? (0 = Poorly, 10 = Very well)",
        "How well did you sleep last night? (0 = Poorly, 10 = Very well)",
        "How productive were you today? (0 = Not at all, 10 = Extremely productive)",
        "How much did you enjoy your day today? (0 = Not at all, 10 = Very much)"
    ]
    answers = [st.slider(question, 0, 10) for question in questions]
    average = sum(answers) / len(answers)
    st.write(f"Your average mental health score today is {average:.1f}")
    
    # Display gauge
    fig = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=average,
        mode="gauge+number",
        title={'text': "Mental Health Score"},
        gauge={'axis': {'range': [0, 10]},
               'steps': [
                   {'range': [0, 2], 'color': "red"},
                   {'range': [2, 4], 'color': "orange"},
                   {'range': [4, 6], 'color': "yellow"},
                   {'range': [6, 8], 'color': "lightgreen"},
                   {'range': [8, 10], 'color': "green"}],
               'threshold': {'line': {'color': "black", 'width': 4}, 'thickness': 0.75, 'value': average}}))
    st.plotly_chart(fig, use_container_width=True)
    st.write("## Mental Health Guidances")
    
    if st.button("Generate guidance"):
        asyncio.run(show_guidance(average))

async def show_guidance(average_score):
    prompt = f"Based on a mental health score of {average_score:.1f}, what guidance can you offer to improve mental health?"
    
    try:
        response = await client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=1024,
            temperature=0.7
        )

        st.write(response.choices[0].text)

        # guidance = response.choices[0].text  # Adjust how response data is accessed based on API changes.
        # st.write(guidance)
    except Exception as e:
        st.write("An error occurred:", e)

# Link to the Dashboard
st.markdown('<a href="http://localhost:8000/dashboard.html" target="_blank"><button style="color: white; background-color: #4CAF50; border: none; padding: 10px 20px; text-align: center; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer;">Go to Dashboard</button></a>', unsafe_allow_html=True)

if __name__ == '__main__':
    mental_health_check_in()
   

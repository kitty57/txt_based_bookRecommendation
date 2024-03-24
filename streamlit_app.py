import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyDKcxALky8LiROaxb0RGMw8TLLOcujMRMY")
llm = genai.GenerativeModel(model_name="gemini-pro")

def prompt(text):
    prompt_parts = [
        f'"Given a text: {text} analyze the text and recommend books that the user will like reading in their current situation/mood.the output should contain the book recommendation in bold in the first line and a line explaining why that book was chosen"'
    ]
    return prompt_parts
def generate_book(text):
    human_prompt = prompt(text)
    response = llm.generate_content(human_prompt)
    return response.text
def main():
    st.title("Book Recommendation based on Text Analysis")
    user_input = st.text_input("Enter your text:")

    if st.button("Generate Book Recommendation"):
        recommendation = generate_book(user_input)
        st.markdown(recommendation)

if __name__ == "__main__":
    main()

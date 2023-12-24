#from langchain.agents import create_csv_agent
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st
import tempfile 


def main():
    load_dotenv()

    # Load the OpenAI API key from the environment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")
        

    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your CSV 📈")

    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    if csv_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temporary_file:
            temporary_file.write(csv_file.getvalue())
            #temporary_file.write(data_str)
            temporary_file.flush()
            llm =OpenAI(temperature=0)

            user_question = st.text_input("Ask a question about your CSV: ")


        #agent = create_csv_agent(
        #    OpenAI(temperature=0), csv_file, verbose=True)
            agent = create_csv_agent(llm, temporary_file.name, verbose=True)

        

            if user_question is not None and user_question != "":
                with st.spinner(text="In progress..."):
                    st.write(agent.run(user_question))


if __name__ == "__main__":
    main()

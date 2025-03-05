import streamlit as st
import pandas as pd
import os
from utils.data_loader import load_data_for_chat
from utils.pandasai_config import (
    PANDAS_AI_AVAILABLE, 
    handle_chart_response
)

def render_chat_component():
    """Render the chat component in the sidebar"""
    with st.sidebar:
        st.header("Chat with Your Data")
        
        # Initialize memory images if it doesn't exist
        if 'memory_images' not in st.session_state:
            st.session_state.memory_images = {}
        
        # Initialize chat history if it doesn't exist
        if 'chat_messages' not in st.session_state:
            st.session_state.chat_messages = []
        
        # Example Questions
        with st.expander("Example Questions", expanded=False):
            examples = [
                "What is the total profit by country?",
                "Show pie chart of loan types",
                "Types of loans",
                "Show a pie chart based on education",
                "Compare performance between segments"
            ]
            
            for i, example in enumerate(examples):
                if st.button(example, key=f"example_{i}", use_container_width=True):
                    # Add to chat history
                    st.session_state.chat_messages.append({"role": "user", "content": example})
                    st.rerun()
        
        # Clear chat history button
        if st.button("Clear Chat History", key="clear_chat", use_container_width=True):
            st.session_state.chat_messages = []
            st.rerun()
        
        # Chat input
        prompt = st.chat_input("Ask a question...")
        
        if PANDAS_AI_AVAILABLE:
            try:
                # Load data
                df = load_data_for_chat()
                
                if df is not None:
                    # Process user input
                    if prompt:
                        # Add user message to chat history
                        st.session_state.chat_messages.append({"role": "user", "content": prompt})
                    
                    # Display chat messages from history
                    for i, message in enumerate(st.session_state.chat_messages):
                        # Display user message
                        if message["role"] == "user":
                            with st.chat_message("user"):
                                st.markdown(message["content"])
                        
                        # Generate and display AI response for user message if not already present
                        if message["role"] == "user" and i == len(st.session_state.chat_messages) - 1:
                            with st.chat_message("assistant"):
                                with st.spinner("Analyzing data..."):
                                    try:
                                        response = df.chat(message["content"])
                                        
                                        # Debug output for better troubleshooting
                                        st.write(f"Debug - Response type: {type(response)}")
                                        st.write(f"Debug - Response value: {response}")
                                        
                                        # Handle the response (chart or text)
                                        success, content, is_image = handle_chart_response(response)
                                        
                                        # Store in chat history
                                        st.session_state.chat_messages.append({
                                            "role": "assistant",
                                            "content": content,
                                            "is_image": is_image
                                        })
                                        
                                    except Exception as e:
                                        error_msg = f"Error analyzing data: {str(e)}"
                                        st.error(error_msg)
                                        import traceback
                                        st.error(traceback.format_exc())
                                        
                                        # Store error message in chat history
                                        st.session_state.chat_messages.append({
                                            "role": "assistant",
                                            "content": error_msg,
                                            "is_image": False
                                        })
                        
                        # Display existing assistant message
                        elif message["role"] == "assistant":
                            with st.chat_message("assistant"):
                                if message.get("is_image", False):
                                    # For an image, we've stored the file path
                                    file_path = message["content"]
                                    
                                    # Display the image if it exists
                                    if os.path.exists(file_path):
                                        st.image(file_path)
                                        
                                        # Add download button with unique key
                                        try:
                                            with open(file_path, "rb") as file:
                                                btn = st.download_button(
                                                    label="Download Image",
                                                    data=file.read(),
                                                    file_name=os.path.basename(file_path),
                                                    mime="image/png",
                                                    key=f"dl_file_hist_{i}"
                                                )
                                        except Exception as e:
                                            st.error(f"Error creating download button: {e}")
                                    else:
                                        st.warning(f"Image file not found: {file_path}")
                                else:
                                    # Regular text message
                                    st.markdown(message["content"])
                else:
                    st.warning(
                        "No data available for analysis. Please ensure data.csv exists and is properly formatted."
                    )
            except Exception as e:
                st.error(f"Error initializing chat: {str(e)}")
                import traceback
                st.error(traceback.format_exc())
        else:
            st.warning("""
            PandasAI package is not available. To enable the chat feature, please install the required packages:
            ```
            pip install "pandasai>=3.0.0b2" pandasai-openai
            ```
            Then restart the application.
            """)
            
import streamlit as st
import io
import os
from PIL import Image
import base64
import uuid

# Initialize session state for storing images
if 'memory_images' not in st.session_state:
    st.session_state.memory_images = {}

# Check PandasAI availability
try:
    import pandasai as pai
    from pandasai_openai import OpenAI
    from pandasai import SmartDataframe
    
    # Print version for debugging
    print(f"PandasAI version: {pai.__version__}")
    
    PANDAS_AI_AVAILABLE = True
except ImportError as e:
    print(f"Error importing PandasAI: {str(e)}")
    PANDAS_AI_AVAILABLE = False

# Helper function to display image from memory
def display_in_memory_image(chart_id):
    """Display an image from memory by chart_id"""
    if chart_id in st.session_state.memory_images:
        image_bytes = st.session_state.memory_images[chart_id]
        # Reset buffer position
        image_bytes.seek(0)
        # Open and display the image
        image = Image.open(image_bytes)
        st.image(image)
        return True
    return False

# Helper function to get bytes from in-memory image
def get_image_bytes(chart_id):
    """Get image bytes for download"""
    if chart_id in st.session_state.memory_images:
        image_bytes = st.session_state.memory_images[chart_id]
        # Reset buffer position
        image_bytes.seek(0)
        # Return bytes for download
        return image_bytes.getvalue()
    return None

# Function to display a file-based image
def display_file_image(file_path):
    """Display and provide download for file-based images"""
    try:
        # Try direct path
        if os.path.exists(file_path):
            st.image(file_path)
            st.text(f"Path: {file_path}")
            
            # Add download button
            with open(file_path, "rb") as file:
                btn = st.download_button(
                    label="Download Image",
                    data=file.read(),
                    file_name=os.path.basename(file_path),
                    mime="image/png"
                )
            return True, file_path, True
            
        # Try with current working directory
        full_path = os.path.join(os.getcwd(), file_path)
        if os.path.exists(full_path):
            st.image(full_path)
            st.text(f"Path: {full_path}")
            
            # Add download button
            with open(full_path, "rb") as file:
                btn = st.download_button(
                    label="Download Image",
                    data=file.read(),
                    file_name=os.path.basename(file_path),
                    mime="image/png"
                )
            return True, file_path, True
            
        # If we get here, the file wasn't found
        st.warning(f"Image file not found: {file_path}")
        st.write(f"Attempted paths: {file_path}, {full_path}")
        return False, f"Image not found: {file_path}", False
        
    except Exception as e:
        st.error(f"Error displaying image: {str(e)}")
        return False, f"Error displaying image: {str(e)}", False

# Function to handle chart response for PandasAI
def handle_chart_response(response):
    """Handle chart response from PandasAI"""
    
    # Check if it's a chart response object (has a save method)
    if hasattr(response, 'save') and callable(response.save):
        try:
            # Create a unique filename
            file_name = f"chart_{uuid.uuid4().hex[:8]}.png"
            file_path = os.path.join("exports/charts", file_name)
            
            # Make sure the directory exists
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            # Save the chart
            response.save(file_path)
            
            # Display the saved file
            if os.path.exists(file_path):
                st.image(file_path)
                
                # Add download button
                with open(file_path, "rb") as file:
                    btn = st.download_button(
                        label="Download Image",
                        data=file.read(),
                        file_name=os.path.basename(file_path),
                        mime="image/png"
                    )
                
                return True, file_path, True  # Success, response content, is_image
            else:
                st.warning(f"Failed to save chart to {file_path}")
                return False, "Chart generation failed", False
                
        except Exception as e:
            st.error(f"Error saving chart: {str(e)}")
            import traceback
            st.error(traceback.format_exc())
            return False, f"Error saving chart: {str(e)}", False
    
    # Check if it's a chart_id in memory
    elif isinstance(response, str) and response.startswith("chart_"):
        if display_in_memory_image(response):
            return True, response, True
    
    # Check if it's a file path for an image
    elif isinstance(response, str) and (
        (response.startswith("exports/") or response.startswith("./exports/")) and 
        (response.endswith(".png") or response.endswith(".jpg") or response.endswith(".jpeg"))
    ):
        success, content, is_image = display_file_image(response)
        return success, content, is_image
    
    # Regular text response
    st.markdown(str(response))
    return True, str(response), False
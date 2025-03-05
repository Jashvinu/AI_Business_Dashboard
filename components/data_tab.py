import streamlit as st
import pandas as pd
from datetime import datetime
from utils.data_loader import load_data

def render_data_tab():
    """Render the Data Table tab content"""
    st.markdown("## Data Table")

    # Load data
    df = load_data()
    
    # Check if data is loaded
    if df.empty:
        st.warning("No data available. Please ensure 'data.csv' exists and is properly formatted.")
        return

    # Create filter section
    st.markdown("### Filters")

    with st.container():
        st.markdown("""
            <div class="filter-container">
        """, unsafe_allow_html=True)

        # Get all available columns that can be used for filtering
        all_columns = df.columns.tolist()
        categorical_columns = [col for col in all_columns if df[col].dtype == 'object' 
                             or col in ["Segment", "Country", "Product", "Discount Band", "Month Name", "Year"]]
        
        # Create two rows of filters with 3 columns each
        col1, col2, col3 = st.columns(3)
        col_map = {0: col1, 1: col2, 2: col3}

        filter_selections = {}

        # Create filters for up to 6 categorical columns
        for i, column in enumerate(categorical_columns[:6]):
            col_idx = i % 3
            with col_map[col_idx]:
                # Get unique values and add "All" option
                unique_values = ["All"]
                if column in df.columns:
                    unique_values += sorted([str(x) for x in df[column].dropna().unique().tolist()])

                # Create the selectbox
                filter_selections[column] = st.selectbox(
                    f"Filter by {column}",
                    unique_values
                )

        # Identify numeric columns for range sliders
        numeric_columns = [col for col in all_columns if pd.api.types.is_numeric_dtype(df[col])]
        
        # Add numeric range sliders
        if numeric_columns:
            col1, col2 = st.columns(2)
            
            # Choose two important numeric columns for filtering
            units_col = next((col for col in numeric_columns if 'unit' in col.lower()), numeric_columns[0])
            profit_col = next((col for col in numeric_columns if 'profit' in col.lower()), 
                             numeric_columns[1] if len(numeric_columns) > 1 else numeric_columns[0])
            
            with col1:
                min_units = float(df[units_col].min())
                max_units = float(df[units_col].max())
                units_range = st.slider(
                    f"{units_col} Range", min_units, max_units, (min_units, max_units))
                
            with col2:
                min_profit = float(df[profit_col].min())
                max_profit = float(df[profit_col].max())
                profit_range = st.slider(
                    f"{profit_col} Range", min_profit, max_profit, (min_profit, max_profit))
        else:
            units_col = None
            profit_col = None
            units_range = None
            profit_range = None
            
        # Date filter if date column exists
        if 'Date' in df.columns:
            col1, col2 = st.columns(2)
            
            with col1:
                min_date = df["Date"].min()
                max_date = df["Date"].max()
                start_date = st.date_input("Start Date", min_date)
                
            with col2:
                end_date = st.date_input("End Date", max_date)
        else:
            start_date = None
            end_date = None

        # Add search box
        search_term = st.text_input("Search in any column", "")

        st.markdown("</div>", unsafe_allow_html=True)

    # Apply filters
    filtered_df = df.copy()

    # Filter by date if date column exists
    if 'Date' in filtered_df.columns and start_date and end_date:
        filtered_df = filtered_df[(filtered_df["Date"] >= start_date) & (filtered_df["Date"] <= end_date)]

    # Apply all column filters
    for column, selection in filter_selections.items():
        if selection != "All" and column in filtered_df.columns:
            filtered_df = filtered_df[filtered_df[column].astype(str) == selection]

    # Filter by units range if applicable
    if units_col and units_range:
        filtered_df = filtered_df[(filtered_df[units_col] >= units_range[0]) & 
                                 (filtered_df[units_col] <= units_range[1])]

    # Filter by profit range if applicable
    if profit_col and profit_range:
        filtered_df = filtered_df[(filtered_df[profit_col] >= profit_range[0]) & 
                                 (filtered_df[profit_col] <= profit_range[1])]

    # Apply search if entered
    if search_term:
        search_mask = filtered_df.astype(str).apply(
            lambda x: x.str.contains(search_term, case=False)).any(axis=1)
        filtered_df = filtered_df[search_mask]

    # Format the DataFrame for display
    display_df = filtered_df.copy()

    # Format currency columns
    currency_columns = ['Manufacturing Price', 'Sale Price', 'Gross Sales',
                        'Discounts', 'Sales', 'COGS', 'Profit']

    for col in currency_columns:
        if col in display_df.columns:
            display_df[col] = display_df[col].apply(
                lambda x: f"${x:,.2f}" if pd.notnull(x) else "")

    # Display filtered data
    st.markdown("### Results")

    with st.container():
        st.markdown("""
            <div class="data-table-container">
        """, unsafe_allow_html=True)

        # Show number of results
        st.write(f"Showing {len(filtered_df)} of {len(df)} entries")

        # Add column selection for the table
        all_columns = filtered_df.columns.tolist()
        with st.expander("Select columns to display"):
            selected_columns = st.multiselect(
                "Choose columns",
                options=all_columns,
                default=all_columns
            )

        # Display the data table with only selected columns
        if selected_columns:
            st.dataframe(display_df[selected_columns], use_container_width=True)
        else:
            st.dataframe(display_df, use_container_width=True)

        # Download button for filtered data
        csv = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Filtered Data",
            data=csv,
            file_name="filtered_data.csv",
            mime="text/csv",
        )

        st.markdown("</div>", unsafe_allow_html=True)
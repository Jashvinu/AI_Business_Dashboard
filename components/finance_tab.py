import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def render_finance_tab():
    """Render the Finance & Reports tab content with dummy values"""
    # Metrics row
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class="metric-container">
                <p style="color: #6B7280; margin-bottom: 5px;">Total Revenue</p>
                <h2 style="margin: 0;">₹1,24,50,000</h2>
                <p style="color: #10B981; margin: 5px 0;">+8.5% vs last month</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="metric-container">
                <p style="color: #6B7280; margin-bottom: 5px;">Budget Utilized</p>
                <h2 style="margin: 0;">78%</h2>
                <p style="color: #6B7280; margin: 5px 0;">₹98,45,000 of ₹1,26,00,000</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="metric-container">
                <p style="color: #6B7280; margin-bottom: 5px;">Pending Approvals</p>
                <h2 style="margin: 0;">12</h2>
                <p style="color: #F59E0B; margin: 5px 0;">4 high priority</p>
            </div>
        """, unsafe_allow_html=True)

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### Revenue vs Expenses")

        # Create sample data for the graph
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        revenue = [100, 120, 125, 130, 140, 160]
        expenses = [110, 105, 100, 95, 100, 105]

        # Create a matplotlib figure instead of plotly to avoid the orjson issue
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(months, revenue, marker='o', linewidth=2, color='#10B981', label='Revenue')
        ax.plot(months, expenses, marker='o', linewidth=2, color='#F59E0B', label='Expenses')
        ax.set_xlabel('Month')
        ax.set_ylabel('Value')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend()
        
        # Use Streamlit's matplotlib display
        st.pyplot(fig)

        st.markdown("### Recent Documents")

        st.markdown("""
            <div class="document-item">
                <div style="margin-right: 20px;">
                    <div style="width: 40px; height: 40px; background-color: #F3F4F6; border-radius: 4px;"></div>
                </div>
                <div style="flex-grow: 1;">
                    <h4 style="margin: 0;">Q1 Financial Report</h4>
                    <p style="color: #6B7280; margin: 5px 0;">Modified 2 days ago</p>
                </div>
                <div style="color: #6B7280;">PDF</div>
            </div>
            
            <div class="document-item">
                <div style="margin-right: 20px;">
                    <div style="width: 40px; height: 40px; background-color: #F3F4F6; border-radius: 4px;"></div>
                </div>
                <div style="flex-grow: 1;">
                    <h4 style="margin: 0;">Budget Analysis 2024</h4>
                    <p style="color: #6B7280; margin: 5px 0;">Modified 1 week ago</p>
                </div>
                <div style="color: #6B7280;">XLSX</div>
            </div>
            
            <div class="document-item">
                <div style="margin-right: 20px;">
                    <div style="width: 40px; height: 40px; background-color: #F3F4F6; border-radius: 4px;"></div>
                </div>
                <div style="flex-grow: 1;">
                    <h4 style="margin: 0;">Tax Documentation</h4>
                    <p style="color: #6B7280; margin: 5px 0;">Modified 3 days ago</p>
                </div>
                <div style="color: #6B7280;">PDF</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("### Quick Links")

        st.markdown("""
            <div style="background-color: white; padding: 15px; border-radius: 8px; margin-bottom: 20px;">
                <div style="padding: 10px 0;"><a href="#" style="color: #111827; text-decoration: none;">HR Portal</a></div>
                <div style="padding: 10px 0;"><a href="#" style="color: #111827; text-decoration: none;">Finance Dashboard</a></div>
                <div style="padding: 10px 0;"><a href="#" style="color: #111827; text-decoration: none;">CRM System</a></div>
                <div style="padding: 10px 0;"><a href="#" style="color: #111827; text-decoration: none;">Policy Documents</a></div>
            </div>
        """, unsafe_allow_html=True)

        # Instead of using HTML markup, let's use Streamlit's native components
        st.markdown("### Recent Transactions")

        with st.container():
            # Create a white background container
            with st.container():
                st.markdown("""
                    <div style="background-color: white; padding: 15px; border-radius: 8px;">
                """, unsafe_allow_html=True)

                # Transaction 1
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown("**Office Supplies**")
                    st.markdown(
                        "<span style='color: #6B7280;'>Mar 21, 2024</span>", unsafe_allow_html=True)
                with col2:
                    st.markdown(
                        "<div style='color: #EF4444; text-align: right;'>-₹12,500</div>", unsafe_allow_html=True)

                st.markdown(
                    "<hr style='margin: 10px 0; border-color: #F3F4F6;'>", unsafe_allow_html=True)

                # Transaction 2
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown("**Client Payment**")
                    st.markdown(
                        "<span style='color: #6B7280;'>Mar 20, 2024</span>", unsafe_allow_html=True)
                with col2:
                    st.markdown(
                        "<div style='color: #10B981; text-align: right;'>+₹1,45,000</div>", unsafe_allow_html=True)

                st.markdown("</div>", unsafe_allow_html=True)
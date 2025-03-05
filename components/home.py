import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import matplotlib as mpl

def render_home():
    """Render the Home page with combined performance metrics across companies"""
    st.header("Combined Performance Dashboard")
    
    # Set a modern aesthetic style for matplotlib
    plt.style.use('seaborn-v0_8-whitegrid')
    
    # Custom color palette
    colors = {
        'primary': '#4361EE',
        'secondary': '#3A0CA3',
        'accent1': '#7209B7',
        'accent2': '#F72585',
        'accent3': '#4CC9F0',
        'success': '#10B981',
        'warning': '#F59E0B',
        'danger': '#EF4444',
        'light': '#F3F4F6',
        'dark': '#111827',
        'background': '#FFFFFF'
    }
    
    # KPI metrics row
    st.subheader("Key Performance Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div class="metric-container" style="border-left: 4px solid #4361EE; padding-left: 16px;">
                <p style="color: #6B7280; margin-bottom: 5px; font-size: 14px;">Total Revenue</p>
                <h2 style="margin: 0; font-size: 28px; font-weight: 700;">₹4.8M</h2>
                <p style="color: #10B981; margin: 5px 0; font-size: 14px;">+12.3% YoY</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="metric-container" style="border-left: 4px solid #7209B7; padding-left: 16px;">
                <p style="color: #6B7280; margin-bottom: 5px; font-size: 14px;">Projects Completed</p>
                <h2 style="margin: 0; font-size: 28px; font-weight: 700;">87</h2>
                <p style="color: #10B981; margin: 5px 0; font-size: 14px;">+8.7% vs target</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="metric-container" style="border-left: 4px solid #F72585; padding-left: 16px;">
                <p style="color: #6B7280; margin-bottom: 5px; font-size: 14px;">Team Productivity</p>
                <h2 style="margin: 0; font-size: 28px; font-weight: 700;">92%</h2>
                <p style="color: #10B981; margin: 5px 0; font-size: 14px;">+5.2% vs last quarter</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
            <div class="metric-container" style="border-left: 4px solid #4CC9F0; padding-left: 16px;">
                <p style="color: #6B7280; margin-bottom: 5px; font-size: 14px;">Customer Satisfaction</p>
                <h2 style="margin: 0; font-size: 28px; font-weight: 700;">4.8/5</h2>
                <p style="color: #10B981; margin: 5px 0; font-size: 14px;">+0.3 vs last year</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<hr style='margin: 20px 0; border: none; height: 1px; background-color: #E5E7EB;'>", unsafe_allow_html=True)
    
    # Revenue by company chart
    st.subheader("Revenue by Company")
    
    # Create dummy data
    companies = ["Company 1", "Company 2", "Company 3", "Company 4", "Company 5"]
    revenue = [1.8, 1.2, 0.9, 0.5, 0.4]  # in millions
    
    # Create the figure and axis with a better size ratio
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Create a color gradient for bars
    bar_colors = [colors['primary'], colors['secondary'], colors['accent1'], colors['accent2'], colors['accent3']]
    
    # Create bars with rounded corners
    bars = ax.bar(
        companies, 
        revenue, 
        color=bar_colors,
        edgecolor='white',
        linewidth=1,
        width=0.4
    )
    
    # Add data labels on top of bars with better formatting
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2., 
            height + 0.05,
            f'₹{height}M', 
            ha='center', 
            va='bottom',
            fontweight='bold',
            fontsize=10,
            color=colors['dark']
        )
    
    # Customize the chart for better aesthetics
    ax.set_ylabel('Revenue (₹ in Millions)', fontsize=11)
    ax.set_title('Revenue by Company - Current Quarter', fontsize=14, pad=15, fontweight='bold')
    ax.grid(axis='y', linestyle='--', alpha=0.3, zorder=0)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_alpha(0.3)
    ax.spines['bottom'].set_alpha(0.3)
    ax.tick_params(axis='both', which='major', labelsize=10)
    
    # Set y-axis to start from 0
    ax.set_ylim(0, max(revenue) + 0.3)
    
    # Add subtle background color
    fig.patch.set_facecolor(colors['background'])
    ax.set_facecolor('#F8FAFC')
    
    # Adjust layout
    plt.tight_layout()
    
    # Display the chart
    st.pyplot(fig)
    
    # Two column layout for additional charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Project Completion Rate")
        
        # Create dummy data for project completion
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        company1 = [85, 87, 90, 91, 92, 95]
        company2 = [80, 82, 83, 85, 88, 90]
        company3 = [75, 78, 80, 82, 85, 88]
        
        # Create chart with better aesthetics
        fig, ax = plt.subplots(figsize=(8, 4.5))
        
        # Create a gradient alpha for line
        ax.plot(months, company1, marker='o', linewidth=3, label='Company 1', 
                color=colors['primary'], markerfacecolor='white', markeredgecolor=colors['primary'], 
                markeredgewidth=2, markersize=8)
        ax.plot(months, company2, marker='s', linewidth=3, label='Company 2', 
                color=colors['accent1'], markerfacecolor='white', markeredgecolor=colors['accent1'], 
                markeredgewidth=2, markersize=8)
        ax.plot(months, company3, marker='^', linewidth=3, label='Company 3', 
                color=colors['accent2'], markerfacecolor='white', markeredgecolor=colors['accent2'], 
                markeredgewidth=2, markersize=8)
        
        # Add value annotations
        for i, month in enumerate(months):
            if i % 2 == 0:  # Add labels for every other point to avoid crowding
                ax.annotate(f"{company1[i]}%", 
                            (i, company1[i]), 
                            xytext=(0, 8),
                            textcoords='offset points',
                            ha='center',
                            fontsize=8,
                            fontweight='bold',
                            color=colors['primary'])
                
                ax.annotate(f"{company2[i]}%", 
                            (i, company2[i]), 
                            xytext=(0, 8),
                            textcoords='offset points',
                            ha='center',
                            fontsize=8,
                            fontweight='bold',
                            color=colors['accent1'])
                
                ax.annotate(f"{company3[i]}%", 
                            (i, company3[i]), 
                            xytext=(0, 8),
                            textcoords='offset points',
                            ha='center',
                            fontsize=8,
                            fontweight='bold',
                            color=colors['accent2'])
        
        # Customize chart for better aesthetics
        ax.set_ylabel('Completion Rate (%)', fontsize=11)
        ax.set_ylim(70, 100)
        ax.grid(True, linestyle='--', alpha=0.3)
        
        # Improved legend with custom positioning
        legend = ax.legend(loc='lower right', frameon=True, framealpha=0.9, 
                   edgecolor='#E5E7EB')
        legend.get_frame().set_facecolor(colors['background'])
        
        # Remove spines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_alpha(0.3)
        ax.spines['bottom'].set_alpha(0.3)
        
        # Set title with better styling
        ax.set_title('Project Completion Trends', fontsize=14, pad=15, fontweight='bold')
        
        # Set background colors
        fig.patch.set_facecolor(colors['background'])
        ax.set_facecolor('#F8FAFC')
        
        # Adjust layout
        plt.tight_layout()
        
        # Display chart
        st.pyplot(fig)
    
    with col2:
        st.subheader("Resource Allocation")
        
        # Create dummy data for resource allocation
        categories = ['Development', 'Design', 'Marketing', 'Support', 'Admin']
        allocation = [40, 25, 15, 12, 8]  # percentage
        
        # Create chart with better aesthetics
        fig, ax = plt.subplots(figsize=(8, 4.5))
        
        # Create custom colors with a professional palette
        pie_colors = [colors['primary'], colors['secondary'], colors['accent1'], colors['accent2'], colors['accent3']]
        
        # Create explode effect for emphasis
        explode = (0.05, 0, 0, 0, 0)  # only "explode" the 1st slice
        
        # Create pie chart with better styling
        wedges, texts, autotexts = ax.pie(
            allocation, 
            labels=None,  # We'll add custom legend instead
            autopct='%1.1f%%', 
            startangle=90,
            colors=pie_colors,
            explode=explode,
            shadow=False,
            wedgeprops={'edgecolor': 'white', 'linewidth': 2, 'antialiased': True},
            textprops={'fontsize': 11, 'fontweight': 'bold', 'color': 'white'}
        )
        
        # Equal aspect ratio ensures that pie is drawn as a circle
        ax.axis('equal')
        
        # Add a circle at the center to make it a donut chart
        centre_circle = plt.Circle((0, 0), 0.3, fc='white', edgecolor='#E5E7EB')
        ax.add_artist(centre_circle)
        
        # Add title to center of donut
        ax.text(0, 0, "Resources", ha='center', va='center', fontsize=12, fontweight='bold')
        
        # Create custom legend
        legend_labels = [f"{cat} ({alloc}%)" for cat, alloc in zip(categories, allocation)]
        ax.legend(wedges, legend_labels, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        
        # Set title with better styling
        ax.set_title('Resource Allocation by Department', fontsize=14, pad=15, fontweight='bold')
        
        # Set background colors
        fig.patch.set_facecolor(colors['background'])
        
        # Adjust layout
        plt.tight_layout()
        
        # Display chart
        st.pyplot(fig)
    
    st.markdown("<hr style='margin: 20px 0; border: none; height: 1px; background-color: #E5E7EB;'>", unsafe_allow_html=True)
    
    # Projects timeline
    st.subheader("Upcoming Project Milestones")
    
    # Create dummy data for project timeline
    projects_data = {
        "Project": ["ERP Implementation", "Mobile App Dev", "Website Redesign", "Data Migration", "Cloud Integration"],
        "Company": ["Company 1", "Company 2", "Company 3", "Company 1", "Company 2"],
        "Deadline": [
            (datetime.now() + timedelta(days=5)).strftime("%b %d, %Y"),
            (datetime.now() + timedelta(days=12)).strftime("%b %d, %Y"),
            (datetime.now() + timedelta(days=8)).strftime("%b %d, %Y"),
            (datetime.now() + timedelta(days=15)).strftime("%b %d, %Y"),
            (datetime.now() + timedelta(days=20)).strftime("%b %d, %Y")
        ],
        "Status": ["On Track", "Delayed", "On Track", "On Track", "On Track"],
        "Completion": [85, 65, 90, 50, 30]
    }
    
    # Create dataframe
    projects_df = pd.DataFrame(projects_data)
    
    # Display project timeline with improved UI
    for idx, row in projects_df.iterrows():
        status_color = colors['success'] if row["Status"] == "On Track" else colors['warning']
        completion = row["Completion"]
        
        # Calculate days remaining
        deadline_date = datetime.strptime(row["Deadline"], "%b %d, %Y")
        days_remaining = (deadline_date - datetime.now()).days
        urgency_text = f"{days_remaining} days left"
        urgency_color = colors['success'] if days_remaining > 10 else (
            colors['warning'] if days_remaining > 5 else colors['danger'])
        
        st.markdown(f"""
            <div class="project-card" style="border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h4 style="margin: 0; font-size: 16px; font-weight: 600;">{row['Project']}</h4>
                        <div style="display: flex; align-items: center; margin-top: 5px;">
                            <span style="color: #6B7280; font-size: 13px;">Company: {row['Company']}</span>
                            <span style="margin: 0 10px; color: #D1D5DB;">|</span>
                            <span style="color: #6B7280; font-size: 13px;">Due: {row['Deadline']}</span>
                            <span style="margin: 0 10px; color: #D1D5DB;">|</span>
                            <span style="color: {urgency_color}; font-size: 13px; font-weight: 500;">{urgency_text}</span>
                        </div>
                    </div>
                    <span style="background-color: {status_color}; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 500;">
                        {row['Status']}
                    </span>
                </div>
                <div style="margin-top: 15px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
                        <span style="font-size: 12px; color: #6B7280;">Progress</span>
                        <span style="font-size: 12px; font-weight: 600;">{completion}%</span>
                    </div>
                    <div style="width: 100%; height: 8px; background-color: #F3F4F6; border-radius: 10px; overflow: hidden;">
                        <div style="width: {completion}%; height: 100%; background-color: {status_color}; border-radius: 10px;"></div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
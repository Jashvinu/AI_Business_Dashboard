import streamlit as st

def render_project_tab():
    """Render the Project Management tab content with dummy values"""
    # Metrics row
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class="metric-container">
                <p style="color: #6B7280; margin-bottom: 5px;">Total Projects</p>
                <h2 style="margin: 0;">24</h2>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="metric-container">
                <p style="color: #6B7280; margin-bottom: 5px;">Team Performance</p>
                <h2 style="margin: 0;">87%</h2>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="metric-container">
                <p style="color: #6B7280; margin-bottom: 5px;">Deadlines Met</p>
                <h2 style="margin: 0;">92%</h2>
            </div>
        """, unsafe_allow_html=True)

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### Project Status")

        # Project 1
        st.markdown("""
            <div class="project-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h4 style="margin: 0;">Website Redesign</h4>
                        <p style="color: #6B7280; margin: 5px 0;">Due: March 30, 2024</p>
                    </div>
                    <span class="status-badge on-track">On Track</span>
                </div>
                <div style="width: 100%; height: 8px; background-color: #F3F4F6; border-radius: 4px; margin-top: 10px;">
                    <div style="width: 75%; height: 100%; background-color: #10B981; border-radius: 4px;"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Project 2
        st.markdown("""
            <div class="project-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h4 style="margin: 0;">Mobile App Dev</h4>
                        <p style="color: #6B7280; margin: 5px 0;">Due: April 15, 2024</p>
                    </div>
                    <span class="status-badge delayed">Delayed</span>
                </div>
                <div style="width: 100%; height: 8px; background-color: #F3F4F6; border-radius: 4px; margin-top: 10px;">
                    <div style="width: 45%; height: 100%; background-color: #F59E0B; border-radius: 4px;"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Project 3
        st.markdown("""
            <div class="project-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h4 style="margin: 0;">CRM Integration</h4>
                        <p style="color: #6B7280; margin: 5px 0;">Due: March 25, 2024</p>
                    </div>
                    <span class="status-badge on-track">On Track</span>
                </div>
                <div style="width: 100%; height: 8px; background-color: #F3F4F6; border-radius: 4px; margin-top: 10px;">
                    <div style="width: 90%; height: 100%; background-color: #10B981; border-radius: 4px;"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("### Upcoming Schedule")

        st.markdown("""
            <div class="project-card">
                <div class="meeting-item">
                    <div class="meeting-dot"></div>
                    <div>
                        <h4 style="margin: 0;">Project Review</h4>
                        <p style="color: #6B7280; margin: 5px 0;">Today, 2:00 PM</p>
                    </div>
                </div>
                <div class="meeting-item">
                    <div class="meeting-dot"></div>
                    <div>
                        <h4 style="margin: 0;">Team Sync</h4>
                        <p style="color: #6B7280; margin: 5px 0;">Tomorrow, 11:00 AM</p>
                    </div>
                </div>
                <div class="meeting-item">
                    <div class="meeting-dot"></div>
                    <div>
                        <h4 style="margin: 0;">Client Meeting</h4>
                        <p style="color: #6B7280; margin: 5px 0;">Mar 25, 3:30 PM</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
def main():
    print("Starting Streamlit app...")
    try:
        initialize_csv()
        init_db()
    except Exception as e:
        logger.error(f"Error during initialization: {str(e)}")
        st.error(f"Initialization failed: {str(e)}")
        return

    if 'page' not in st.session_state:
        st.session_state.page = "Home"
    if 'user_id' not in st.session_state:
        st.session_state.user_id = None
    if 'conversation_history' not in st.session_state:
        st.session_state.conversation_history = []
    if 'stall_registered' not in st.session_state:
        st.session_state.stall_registered = False
    if 'stall_name' not in st.session_state:
        st.session_state.stall_name = None
    if 'is_stall_owner' not in st.session_state:
        st.session_state.is_stall_owner = False

    st.markdown("""
        <style>
            /* CSS styles remain unchanged */
        </style>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """, unsafe_allow_html=True)

    st.markdown('<div class="banner"><h1>Event Management Redefined</h1><p>Redefining your experience</p></div>', unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("<h2>Explore EventHub</h2>", unsafe_allow_html=True)
        page = option_menu(
            menu_title=None,
            options=["Home", "Register", "All Events", "My Events", "Recommendations", "Add Event", "Feedback", "Performance Insights", "Stall Suggestions", "Crowd Monitor", "Admin Dashboard", "Chatbot"],
            icons=["house", "person-plus", "calendar", "bookmark", "lightbulb", "plus-circle", "chat", "graph-up", "shop", "people", "shield-lock", "robot"],
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#2c3e50"},
                "icon": {"color": "#ecf0f1", "font-size": "18px"},
                "nav-link": {"color": "#ecf0f1", "font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#3498db"},
                "nav-link-selected": {"background-color": "#3498db"},
            }
        )
        if page != st.session_state.page:
            st.session_state.page = page
            st.rerun()

    # Page-specific logic remains unchanged but would be split into separate functions if needed
    # For brevity, I'll leave the page handling in main()
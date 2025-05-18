@st.cache_data(show_spinner="Processing backend request...")
def proxy_to_backend(endpoint, method="POST", json_data=None):
    backend_url = f"{BACKEND_URL}{endpoint}"
    try:
        if method == "POST":
            logger.debug(f"Sending to backend: {json_data}")
            response = requests.post(backend_url, json=json_data, timeout=5)
        else:
            response = requests.get(backend_url, params=json_data, timeout=5)
        response.raise_for_status()
        logger.debug(f"Received from backend: {response.text}")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Proxy error: {str(e)}")
        st.error(f"Proxy error: {str(e)}")
        return {"error": str(e)}
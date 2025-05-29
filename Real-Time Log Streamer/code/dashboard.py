# # dashboard.py
# # dashboard.py
# import sqlite3
# import streamlit as st

# st.set_page_config(page_title="Real-Time Log Dashboard", layout="wide")
# st.title("📋 Real-Time Log Viewer")

# # Connect to SQLite
# conn = sqlite3.connect('logs.db')
# c = conn.cursor()

# # Fetch logs
# logs = c.execute("SELECT log_line FROM logs ORDER BY id DESC LIMIT 100").fetchall()

# # Style logs in a better format
# for log in logs:

#     print(log)
#     line = log[0].strip()
    
#     # Basic color coding
#     if "ERROR" in line:
#         st.markdown(f"<span style='color:red;font-family:monospace;'>{line}</span>", unsafe_allow_html=True)
#     elif "WARNING" in line:
#         st.markdown(f"<span style='color:orange;font-family:monospace;'>{line}</span>", unsafe_allow_html=True)
#     elif "INFO" in line:
#         st.markdown(f"<span style='color:green;font-family:monospace;'>{line}</span>", unsafe_allow_html=True)
#     else:
#         st.markdown(f"<span style='font-family:monospace;'>{line}</span>", unsafe_allow_html=True)


# dashboard.py
import sqlite3
import streamlit as st
# import chardet

from charset_normalizer import from_bytes

def try_decode_fallback(raw_text):
    if isinstance(raw_text, str):
        return raw_text
    try:
        result = from_bytes(raw_text.encode('latin1')).best()
        return str(result)
    except:
        return "[Decode Error]"

def try_decode(raw_text):
    try:
        # Attempt to decode assuming it's already a proper string
        if isinstance(raw_text, str):
            return raw_text
        # Else, try bytes decoding with chardet
        if isinstance(raw_text, bytes):
            result = chardet.detect(raw_text)
            return raw_text.decode(result['encoding'], errors='ignore')
        # Catch edge case: string stored as Latin-1-represented UTF-16
        result = chardet.detect(raw_text.encode('latin1'))
        return raw_text.encode('latin1').decode(result['encoding'], errors='ignore')
    except:
        return "[Decode Error]"

# Streamlit layout
st.set_page_config(page_title="📋 Log Viewer", layout="wide")
st.title("📋 Real-Time Log Dashboard with Encoding Detection")

conn = sqlite3.connect('logs.db')
c = conn.cursor()

logs = c.execute("SELECT log_line FROM logs ORDER BY id DESC LIMIT 100").fetchall()

for log in logs:
    clean_log = try_decode_fallback(log[0])
    print(clean_log)
    st.code(clean_log.strip())

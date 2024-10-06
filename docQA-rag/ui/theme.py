JS_THEME = """
function refresh() {
    const url = new URL(window.location);

    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
"""

CSS = """
.btn {
    background-color: #1E293B; /* Darker background */
    color: #FFFFFF; /* White text */
    }

.stop_btn {
    background-color: #FF5E5E; /* Alert color in dark theme */
    color: #FFFFFF;
    }

body {
    background-color: #121212; /* Dark background */
    color: #E0E0E0; /* Light text */
    }

.chat-box {
    background-color: #1E1E1E; /* Chat box in dark mode */
    color: #E0E0E0;
    }
"""

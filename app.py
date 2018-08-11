"""
This script runs the app application using a development server.
"""

# Run a test server.
from app import app
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
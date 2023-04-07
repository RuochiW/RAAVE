"""
@RAAVE
"""

from data.tables import reset_tables
from server import app

# reset_tables()
app.run(host="0.0.0.0", port=1234)

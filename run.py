import os
from app import app

#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=5000, debug=True)

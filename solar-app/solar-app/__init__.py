# import app
from app.solarflaskapp import app

# driver function
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
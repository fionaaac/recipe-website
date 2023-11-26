import os
from recipemain import create_app
from flask_uploads import IMAGES, UploadSet, configure_uploads

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
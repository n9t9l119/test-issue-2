from config import app#, BaseConfig#, TestConfig
import api

import error_handler

if __name__ == '__main__':
    #app.config.from_object(config)
    api.ApiView.register(app)
    app.run(port="8000")



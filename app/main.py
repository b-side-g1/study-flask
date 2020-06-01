from flask import Flask
import config
app = Flask(__name__)

print(config.mysql_config)

@app.route('/', methods=['GET'])
def index():
	return '아아아아~~~~~~'

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=8080)
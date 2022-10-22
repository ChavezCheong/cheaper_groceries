from datetime import datetime
from distutils.log import debug
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)

#Harris Teeter (https://www.harristeeter.com/pl/all/00?fulfillment=all) .kds-Price-promotional--decorated
#Whole Foods (https://www.wholefoodsmarket.com/products/all-products) .sale_price (if sale) .b (if no sale)
#
@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run(debug=True)
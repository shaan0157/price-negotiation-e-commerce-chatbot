from flask import Flask, render_template, jsonify, request, session
from flask_cors import CORS
import os
from dotenv import load_dotenv
from backend.routes.auth import auth_bp
from backend.routes.products import products_bp
from backend.routes.negotiate import negotiate_bp
from backend.routes.orders import orders_bp
from backend.routes.admin import admin_bp
from backend.models.database import init_db

load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = os.getenv('SECRET_KEY', 'negotimart-super-secret-2024')
CORS(app, supports_credentials=True)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(products_bp, url_prefix='/api/products')
app.register_blueprint(negotiate_bp, url_prefix='/api/negotiate')
app.register_blueprint(orders_bp, url_prefix='/api/orders')
app.register_blueprint(admin_bp, url_prefix='/api/admin')

# Initialize database
init_db()

# Frontend routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/product/<int:product_id>')
def product(product_id):
    return render_template('product.html', product_id=product_id)

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

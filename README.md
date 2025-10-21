# FastShip - Shipment Management System

A comprehensive shipment management system built with FastAPI, providing APIs for sellers, delivery partners, and shipment tracking functionality.

## 🚀 Features

- **Seller Management**: Registration, authentication, email verification, password reset
- **Delivery Partner Management**: Partner registration and capacity management
- **Shipment Tracking**: Real-time shipment status updates and timeline tracking
- **Review System**: Customer feedback and rating system
- **Email Notifications**: Automated email notifications for shipment events
- **SMS Notifications**: Twilio integration for SMS alerts
- **Web Interface**: HTML templates for tracking and review submission
- **JWT Authentication**: Secure token-based authentication
- **Redis Caching**: Session management and verification codes

## 🏗️ Architecture

### Database Models
- **Seller**: E-commerce sellers with address and zip code information
- **DeliveryPartner**: Delivery partners with serviceable areas and capacity limits
- **Shipment**: Shipment details with tracking information
- **ShipmentEvent**: Timeline events for shipment status changes
- **Review**: Customer reviews and ratings for completed shipments

### API Endpoints

#### Seller Routes (`/seller`)
- `POST /signup` - Register a new seller
- `POST /token` - Login and get JWT token
- `GET /verify` - Verify seller email
- `GET /forgot_password` - Request password reset
- `GET /reset_password_form` - Password reset form
- `POST /reset_password` - Reset password
- `GET /logout` - Logout and blacklist token

#### Shipment Routes (`/shipment`)
- `GET /track` - Track shipment (web interface)
- `GET /` - Get shipment details by ID
- `POST /` - Create new shipment
- `PATCH /` - Update shipment status
- `GET /cancel` - Cancel shipment
- `GET /review` - Review submission form
- `POST /review` - Submit shipment review

#### Delivery Partner Routes (`/delivery_partner`)
- Similar authentication and management endpoints as sellers

## 🛠️ Technology Stack

- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL with SQLModel/SQLAlchemy
- **Cache**: Redis
- **Authentication**: JWT tokens
- **Email**: SMTP with HTML templates
- **SMS**: Twilio
- **Templates**: Jinja2
- **API Documentation**: Scalar

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL
- Redis
- SMTP email service
- Twilio account (for SMS)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd app
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi uvicorn sqlmodel sqlalchemy asyncpg redis pydantic-settings python-jose[cryptography] passlib[bcrypt] python-multipart jinja2 itsdangerous twilio
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory:
   ```env
   # Database Configuration
   POSTGRES_SERVER=localhost
   POSTGRES_PORT=5432
   POSTGRES_USER=your_username
   POSTGRES_PASSWORD=your_password
   POSTGRES_DB=fastship

   # Redis Configuration
   REDIS_HOST=localhost
   REDIS_PORT=6379

   # Security Configuration
   JWT_SECRET=your_jwt_secret_key
   JWT_ALGORITHM=HS256

   # Email Configuration
   MAIL_USERNAME=your_email@example.com
   MAIL_PASSWORD=your_email_password
   MAIL_FROM=your_email@example.com
   MAIL_PORT=587
   MAIL_SERVER=smtp.gmail.com
   MAIL_FROM_NAME=FastShip
   MAIL_STARTTLS=True
   MAIL_SSL_TLS=False
   USE_CREDENTIALS=True
   VALIDATE_CERTS=True

   # Twilio Configuration
   TWILIO_SID=your_twilio_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_NUMBER=your_twilio_phone_number
   ```

5. **Database Setup**
   ```bash
   # Create PostgreSQL database
   createdb fastship
   
   # Run database migrations (if available)
   # alembic upgrade head
   ```

6. **Start Redis**
   ```bash
   redis-server
   ```

## 🚀 Running the Application

1. **Start the FastAPI server**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Access the application**
   - API: http://localhost:8000
   - API Documentation: http://localhost:8000/scalar
   - Interactive API docs: http://localhost:8000/docs

## 📖 API Usage Examples

### Seller Registration
```bash
curl -X POST "http://localhost:8000/seller/signup" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepassword",
    "address": "123 Main St",
    "zip_code": 12345
  }'
```

### Create Shipment
```bash
curl -X POST "http://localhost:8000/shipment/" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "client_contact_email": "customer@example.com",
    "client_contact_phone": "+1234567890",
    "content": "Electronics",
    "weight": 2.5,
    "destination": 54321
  }'
```

### Track Shipment
```bash
curl -X GET "http://localhost:8000/shipment/track?id=SHIPMENT_UUID"
```

## 🔐 Authentication

The API uses JWT tokens for authentication. Include the token in the Authorization header:

```
Authorization: Bearer YOUR_JWT_TOKEN
```

## 📧 Email Templates

The system includes HTML email templates for:
- Email verification
- Password reset
- Shipment status updates (placed, in transit, out for delivery, delivered, cancelled)

## 🗂️ Project Structure

```
app/
├── api/                    # API routes and schemas
│   ├── routers/           # Route handlers
│   └── schemas/           # Pydantic models
├── core/                  # Core functionality
│   └── security.py       # Security utilities
├── database/             # Database configuration
│   ├── models.py         # SQLModel models
│   ├── session.py        # Database session
│   └── redis.py          # Redis configuration
├── services/             # Business logic
├── templates/            # HTML email templates
├── config.py             # Application configuration
├── main.py               # FastAPI application
└── utils.py              # Utility functions
```

## 🧪 Testing

```bash
# Run tests (if available)
pytest

# Run with coverage
pytest --cov=app
```

## 🚀 Deployment

### Docker (Recommended)
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Production Considerations
- Use environment variables for all sensitive configuration
- Set up proper database connection pooling
- Configure Redis for production
- Set up monitoring and logging
- Use HTTPS in production
- Configure proper CORS settings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support, email support@fastship.com or create an issue in the repository.

## 🔄 Shipment Status Flow

1. **placed** - Initial shipment creation
2. **in_transit** - Shipment picked up and in transit
3. **out_for_delivery** - Shipment out for final delivery
4. **delivered** - Shipment successfully delivered
5. **cancelled** - Shipment cancelled (can occur at any stage)

Each status change creates a timeline event with location and description information.

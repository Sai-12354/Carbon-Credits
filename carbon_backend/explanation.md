# Carbon Credits Backend Project Explanation

## Project Overview

The Carbon Credits backend is a comprehensive Django-based application designed to promote sustainable commuting by tracking, verifying, and rewarding eco-friendly transportation choices. The system implements a complete carbon credit ecosystem where employees can earn credits for sustainable commuting, employers can verify and manage these activities, and banks can facilitate the trading of these credits in a marketplace.

## Root Directory

- **.env**: Environment variables for configuration including database credentials, secret keys, API keys, and other sensitive configuration that shouldn't be hardcoded
- **build.sh**: Deployment script that automates the build process, including collecting static files, running migrations, and configuring the production environment
- **db.sqlite3**: SQLite database file storing all application data (would typically be replaced with PostgreSQL in production)
- **manage.py**: Django's command-line utility for administrative tasks like running the server, creating/applying migrations, and executing custom commands
- **requirements.txt**: Comprehensive list of Python dependencies with specific versions to ensure consistent environments
- **RBAC.md**: Documentation detailing the Role-Based Access Control implementation and permission structures

## carbon_backend/

This is the main Django project configuration folder:

- **settings.py**: Central configuration hub defining database connections, installed apps, middleware, authentication backends, static/media file handling, and custom settings
- **urls.py**: Main URL dispatcher that routes incoming HTTP requests to appropriate view functions based on URL patterns
- **wsgi.py**: Web Server Gateway Interface configuration for communication with web servers like Apache or Nginx in production
- **asgi.py**: Asynchronous Server Gateway Interface configuration for handling asynchronous requests and WebSockets
- **__init__.py**: Makes the directory a Python package and can contain initialization code

## core/

The core module serves as the foundation of the application, providing shared functionality and central routing:

- **admin.py**: Registers models with the Django admin interface and customizes their appearance and behavior
- **admin_urls.py**: Defines URL patterns specifically for administrative functions, separating them from other interfaces
- **apps.py**: Contains the CoreConfig class that configures the core application and initialization code
- **bank_urls.py**: URL patterns for bank-specific views and functionality
- **employee_urls.py**: URL patterns for employee-specific views and functionality
- **employer_urls.py**: URL patterns for employer-specific views and functionality
- **models.py**: Core data models that may be shared across multiple applications
- **tests.py**: Unit and integration tests for the core module functionality
- **urls.py**: Central URL routing for the core module that may include common paths
- **views.py**: View functions that handle HTTP requests and return responses

### core/utils/

Contains utility functions that provide shared functionality across the application:

- **credit_calculator.py**: Implements algorithms to calculate carbon credits based on distance, transportation mode, time of day, and potentially weather conditions
- **distance_calculator.py**: Calculates distances between locations using geospatial calculations, mapping APIs, and caching mechanisms

### core/views/

Contains view functions organized by user role for better separation of concerns:

- **admin_views.py**: Administrative views for system management, user management, configuration, and reporting
- **auth_views.py**: Authentication-related views for login, logout, password reset, and session management
- **bank_views.py**: Views for bank users to monitor trading, manage employer relationships, and generate reports
- **employee_views.py**: Views for employees to log trips, monitor credits, and manage their profile
- **employer_views.py**: Views for employers to manage employees, verify trips, and handle office locations
- **trips_views.py**: Trip-related views that might be shared across different user roles

## marketplace/

Handles the carbon credit marketplace functionality, enabling users to trade credits:

- **admin.py**: Django admin configuration for marketplace models with custom list displays and filters
- **apps.py**: Contains the MarketplaceConfig class for application initialization
- **models.py**: Data models for marketplace entities like listings, transactions, notifications, and price history
- **permissions.py**: Custom permission classes to control access to marketplace features based on user roles
- **serializers.py**: Serializers for converting marketplace data to/from JSON with validation logic
- **tests.py**: Comprehensive tests for marketplace functionality to ensure reliable trading
- **urls.py**: URL patterns for marketplace views organized by feature area
- **views.py**: View functions for creating listings, browsing credits, executing transactions, and viewing history

### marketplace/management/commands/

Custom management commands for the marketplace to facilitate development and testing:

- **create_market_data.py**: Generates realistic test data for the marketplace, useful for development and demonstrations

## trips/

Manages the core functionality of logging, verifying, and rewarding sustainable commuting:

- **admin.py**: Django admin configuration for trip models with custom filters and actions
- **apps.py**: Contains the TripsConfig class for application initialization
- **models.py**: Data models for trips, transport modes, routes, and trip proofs
- **permissions.py**: Custom permission classes to control access to trip-related features
- **serializers.py**: Serializers for trip data with validation logic for API interactions
- **tests.py**: Tests for trip-related functionality including creation, approval, and credit calculation
- **urls.py**: URL patterns for trip-related views and API endpoints
- **utils.py**: Trip-specific utility functions for validation, verification, and route optimization
- **views.py**: View functions for logging trips, viewing history, approving/rejecting trips, and generating reports

### trips/management/commands/

Custom management commands for trips to facilitate testing and development:

- **create_test_credits.py**: Generates test credit data with various transportation modes and distances
- **test_admin_verification.py**: Tests the trip verification workflow for administrators
- **test_employee_features.py**: Tests employee-specific features like trip logging and history viewing

## users/

Handles user management, authentication, and location data:

- **admin.py**: Django admin configuration for user models with custom filters and actions
- **apps.py**: Contains the UsersConfig class for application initialization
- **models.py**: User-related models including custom User model, Profile, Location, and EmployeeInvitation
- **permissions.py**: Custom permission classes based on user attributes and relationships
- **serializers.py**: Serializers for user data with validation logic for API interactions
- **tests.py**: Tests for user-related functionality including registration and authentication
- **urls.py**: URL patterns for user-related views and API endpoints
- **views.py**: View functions for registration, profile management, location settings, and user directory

### users/management/commands/

Custom management commands for user management:

- **createuser.py**: Creates users with specific roles and attributes for testing or initial setup
- **create_locations.py**: Seeds the database with location data for testing or initial setup

## templates/

Contains HTML templates organized by functionality and user role:

- **base.html**: Master template defining common structure, navigation, and shared assets
- **landing.html**: Public-facing landing page with system introduction and login/registration options

### templates/admin/

Admin-specific templates for system management:

- **dashboard.html**: Administrative overview with key metrics and quick access to common tasks
- **reports.html**: Comprehensive reporting interface with filtering and export options
- **users.html**: User management interface with search, filter, and bulk actions
- **user_detail.html**: Detailed view of individual user information, activity, and settings
- **user_hierarchy.html**: Visualization of organizational structure and reporting relationships
- **create_user.html**: Form for creating new user accounts with role-specific fields

### templates/auth/

Authentication templates for user access management:

- **login.html**: User login form with remember-me option and password reset link
- **logout.html**: Logout confirmation and session termination page
- **register.html**: User registration form with role selection and terms acceptance

### templates/bank/

Bank-specific templates for credit trading and management:

- **dashboard.html**: Overview of marketplace activity, credit volume, and key metrics
- **employers.html**: Interface for managing relationships with employer organizations
- **trading.html**: Advanced trading interface with order book, transaction history, and market analytics

### templates/employee/

Employee-specific templates for trip logging and credit management:

- **dashboard.html**: Personal dashboard showing credit balance, recent trips, and sustainability impact
- **trips.html**: Comprehensive trip history with filtering, sorting, and statistics
- **trip_log.html**: Interface for logging new trips with transportation mode selection and proof upload
- **manage_home_location.html**: Settings for updating home location with map integration

### templates/employer/

Employer-specific templates for organization management:

- **dashboard.html**: Organizational dashboard showing company-wide sustainability metrics and trends
- **employees.html**: Employee management interface with invitation, approval, and activity monitoring
- **locations.html**: Interface for managing office locations with map integration
- **pending_trips.html**: Queue of trips awaiting verification with proof review and approval/rejection
- **trading.html**: Interface for organizational credit trading and portfolio management

### templates/registration/

Registration-specific templates for user onboarding:

- **register_employee.html**: Specialized registration form for employees with employer selection
- **register_employer.html**: Specialized registration form for employer organizations with company details
- **pending_approval.html**: Notification page for users awaiting account approval with status updates

## static/

Contains static files including CSS, JavaScript, and images:

### static/js/

JavaScript files enhancing the user interface and experience:

- **employee-registration.js**: Handles dynamic form behavior during registration including validation and employer lookup
- **file-upload.js**: Manages file uploads with drag-and-drop, preview, and validation features
- **trip-log.js**: Enhances trip logging with interactive maps, distance calculation, and transportation selection

## media/

Stores user-uploaded files with appropriate organization:

### media/trip_proofs/

Stores evidence uploaded by employees to verify their sustainable commuting:

- Various image files showing public transport tickets, bicycle parking, carpool verification, etc.

## staticfiles/

Contains collected static files for production deployment, organized by application:

- **Admin interface assets**: CSS, JavaScript, and images for the Django admin interface
- **Django extensions assets**: Additional static files from third-party Django packages
- **REST framework assets**: CSS and JavaScript for the browsable API interface
- **HTMX assets**: JavaScript libraries for dynamic HTML interactions without full page reloads
- **Custom JavaScript files**: Application-specific scripts collected for production serving

## Detailed Functionality

### User Roles and Workflow

The system implements a comprehensive role-based architecture:

1. **Administrators**: System-wide management including user administration, configuration, reporting, and monitoring
2. **Banks**: Financial institutions that facilitate credit trading, manage employer relationships, and ensure market integrity
3. **Employers**: Organizations that manage employees, verify trips, maintain office locations, and participate in credit trading
4. **Employees**: End users who log sustainable commuting trips, earn credits, and can trade them in the marketplace

### Trip Logging Process

The core workflow of the application follows these steps:

1. Employees log trips through an intuitive interface, selecting transportation mode and route
2. For certain modes, proof is required and uploaded to the media/trip_proofs/ directory
3. Employers review pending trips through a dedicated interface, examining proofs when necessary
4. Upon approval, the system calculates carbon credits based on distance, mode, and other factors
5. Credits are awarded to the employee's account and become available for use or trading
6. The system maintains a comprehensive trip history for reporting and verification

### Marketplace Functionality

The carbon credit trading platform operates with these key features:

1. Users can create listings to sell credits, specifying quantity and price
2. Buyers can browse available listings and purchase credits that meet their criteria
3. The system facilitates secure transactions, transferring credits between accounts
4. All transactions are recorded with timestamps, parties involved, and pricing details
5. Users receive notifications about their marketplace activity
6. Banks can monitor trading patterns and ensure compliance with trading rules

### Location Management

Location tracking is essential for accurate distance calculation:

1. Employers maintain office locations through a map-based interface
2. Employees set and update their home locations securely
3. The system calculates commuting distances between these locations
4. Alternative routes and transportation modes may be suggested to maximize sustainability
5. Location data is handled with appropriate privacy considerations

### Authentication and Authorization

Security is implemented through a comprehensive approach:

1. Custom user model with role-based permissions and profile information
2. Multi-step registration workflows tailored to different user types
3. Role-based access control for views, templates, and API endpoints
4. Permission checks at multiple levels to ensure data security
5. Secure password handling and authentication processes

This comprehensive system provides a complete solution for tracking, verifying, and trading carbon credits based on employee commuting patterns, helping organizations reduce their carbon footprint while incentivizing sustainable transportation choices through a gamified and rewarding experience.


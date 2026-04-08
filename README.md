# SHA Bank - E-Wallet Ecosystem

A modern, full-stack digital wallet application designed for seamless financial transactions. This project combines the robustness of **Laravel 13** for the backend architecture and the versatility of **Flutter** for a premium mobile experience.

---

## 🚀 Tech Stack

### Backend
- **Framework:** [Laravel 13](https://laravel.com)
- **Language:** PHP 8.3+
- **Database:** MySQL / PostgreSQL
- **Tools:** Composer, Artisan, Vite

### Mobile
- **Framework:** [Flutter](https://flutter.dev)
- **Language:** Dart
- **State Management:** BLoC (Business Logic Component)
- **UI Architecture:** Clean Architecture
- **Design:** Google Fonts (Outfit/Poppins), Custom UI Kit

---

## 📁 Project Structure

```bash
ewallet/
├── backend/       # Laravel API & Admin Dashboard
├── mobile/        # Flutter Mobile Application
└── README.md      # Project Documentation
```

---

## 🛠️ Getting Started

### Prerequisites
- PHP 8.3 or higher
- Composer
- Node.js & NPM
- Flutter SDK (latest stable)
- Android Studio / Xcode

### 1. Backend Setup (Laravel)

```bash
cd backend

# Install dependencies
composer install
npm install

# Setup environment
cp .env.example .env

# Generate application key
php artisan key:generate

# Run migrations (ensure your database is configured in .env)
php artisan migrate

# Start the development server
php artisan dev
```

### 2. Mobile Setup (Flutter)

```bash
cd mobile

# Get dependencies
flutter pub get

# Run the app
flutter run
```

---

## ✨ Key Features (Roadmap)

- [ ] **Secure Authentication:** JWT-based login, registration, and pin verification.
- [ ] **Wallet Dashboard:** Real-time balance updates and quick actions.
- [ ] **Transaction Logic:** Transfer money, top-up balance, and pay bills.
- [ ] **Interactive Charts:** Visualizing spending habits and income.
- [ ] **Profile Management:** Update personal info, security settings, and KYC.

---

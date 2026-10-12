<p align="center"><img src="assets/banner.png" alt="DevOra E-commerce Suite" width="100%"></p>
<h1 align="center">DevOra E-commerce Suite</h1>
<p align="center"><b>One white-label Flutter codebase that ships as many branded stores — pets, toys, fashion, home services — plus the store-owner admin app.</b></p>
<p align="center">
  <img src="https://img.shields.io/badge/Platform-Android%20%7C%20iOS-0F172A?style=flat-square" alt="Platform">
  <img src="https://img.shields.io/badge/Flutter-3.x-02569B?style=flat-square&logo=flutter&logoColor=white" alt="Flutter">
  <img src="https://img.shields.io/badge/State-Bloc%20%2F%20Cubit-8B5CF6?style=flat-square" alt="Bloc / Cubit">
  <img src="https://img.shields.io/badge/Backend-REST%20%2B%20Socket.IO%20%2B%20Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black" alt="Backend">
  <img src="https://img.shields.io/badge/White--label-4%20live%20brands-FD7E15?style=flat-square" alt="White-label">
  <img src="https://img.shields.io/badge/Case%20Study-portfolio-111827?style=flat-square" alt="Case Study">
</p>
<p align="center">
  <a href="https://play.google.com/store/apps/details?id=com.devora.alife"><img src="https://img.shields.io/badge/Google%20Play-Aleefie-34A853?style=for-the-badge&logo=googleplay&logoColor=white" alt="Aleefie on Google Play"></a>
  <a href="https://apps.apple.com/sa/app/id6753914523"><img src="https://img.shields.io/badge/App%20Store-Aleefie-0D96F6?style=for-the-badge&logo=appstore&logoColor=white" alt="Aleefie on the App Store"></a>
  <a href="https://play.google.com/store/apps/details?id=com.devora.dinotoys"><img src="https://img.shields.io/badge/Google%20Play-Deno%20Store-34A853?style=for-the-badge&logo=googleplay&logoColor=white" alt="Deno Store on Google Play"></a>
  <a href="https://play.google.com/store/apps/details?id=com.devora.starmart"><img src="https://img.shields.io/badge/Google%20Play-StarMart-34A853?style=for-the-badge&logo=googleplay&logoColor=white" alt="StarMart on Google Play"></a>
  <a href="https://play.google.com/store/apps/details?id=com.irtaah.devora"><img src="https://img.shields.io/badge/Google%20Play-Irtaah-34A853?style=for-the-badge&logo=googleplay&logoColor=white" alt="Irtaah on Google Play"></a>
</p>

> ℹ️ Case study — the source code is proprietary to the client and is not included.

## Overview

**DevOra** sells ready-made, branded mobile stores to merchants (mainly in Iraq). Instead of building every store from scratch, I built **one Flutter customer app and one admin app** that can be re-branded per client — name, logo, colours, copy, package id, Firebase project and feature flags — and shipped to Google Play and the App Store as an independent app.

| | |
|---|---|
| **Product** | White-label e-commerce: customer app + store-owner admin app |
| **Market** | Iraq (Arabic-first, RTL, IQD pricing, Iraqi phone auth) |
| **Live brands** | Aleefie (pets), Deno Store (toys), StarMart (fashion), Irtaah (home services) |
| **Other builds** | Pets, Grocery, OCA View, Al-Wathiq storefronts from the same core |
| **My role** | Lead Flutter developer — shared core, white-label workflow, admin app, store releases |
| **Timeline** | 2025 (Aleefie reached the App Store in October 2025) |

## The challenge

- **Many clients, a small team.** Every new merchant wanted "their own app" in weeks, not months. Keeping a separate codebase per store would have multiplied bugs and maintenance.
- **Different verticals, same plumbing.** A pet shop, a toy store, a fashion brand and a home-services company all need catalog, cart, checkout, orders, coupons, notifications and an owner dashboard.
- **Store owners are not technical.** They manage products, orders, banners, coupons and shipping fees from their phone.
- **Arabic-first UX.** RTL layouts, Arabic copy, Iraqi phone numbers and IQD prices across every brand.

## Highlights

**🛍️ Customer app**
- Home with promo banners, categories, sub-categories, "new" and "featured" product rails
- Product details, favourites and a **guest cart** stored locally (Hive) that survives until sign-in
- Checkout with coupons, shipping fees by area and order confirmation; "My orders" history
- Sign-in by **phone OTP**, email/password, **Google** and **Facebook**; biometric unlock (`local_auth`)
- Address and location with Google Maps / geolocation
- Push notifications (FCM + local notifications) and an in-app notifications centre
- Arabic / English with `easy_localization`, light / dark appearance

**🧑‍💼 Store-owner admin (separate app + role-gated screens)**
- Dashboard with charts (`fl_chart` / Syncfusion)
- Orders board with status chips (*not confirmed → in progress → shipped → delivered / canceled*), date filters, bulk selection and status updates
- **PDF export** of orders and customer lists (`pdf` + `printing`)
- Products, categories and inner categories; ads/banners; coupons; shipping zones and fees
- Store info, About and Privacy pages, reviews moderation, customer chat, QR scanner
- Permission-based access (`hasPerm`) so staff only see what their role allows

**🔁 White-label tooling**
- A single `AppConstants` file + brand assets define each store
- A documented 9-step rebrand checklist (name, icon, package id, Firebase project, colours, fonts, copy, SHA keys)

## Screens

<p align="center"><img src="assets/customer-flows.png" alt="Customer flows" width="100%"></p>
<p align="center"><sub>StarMart (Android) and Aleefie (iOS): welcome, sign-in, onboarding, empty states and home — same screens, different brand.</sub></p>

<p align="center"><img src="assets/store-listings.png" alt="Store listings for Aleefie and Deno Store" width="100%"></p>
<p align="center"><sub>Official store screenshots for Aleefie (pets) and Deno Store (toys).</sub></p>

<p align="center"><img src="assets/irtaah-screens.png" alt="Irtaah home services" width="100%"></p>
<p align="center"><sub>Irtaah: the same core configured as a home-services marketplace — services, booking, call / WhatsApp / map actions.</sub></p>

## Signature feature — one codebase, many brands

<p align="center"><img src="assets/brands.png" alt="One codebase, many brands" width="100%"></p>

Every store above runs the **same Flutter code**. What changes is configuration:

<p align="center"><img src="assets/white-label.png" alt="White-label pipeline" width="100%"></p>

**How it works**
1. **Brand config** — `AppConstants` holds the app name, logo, brand colours, onboarding content, allowed countries for phone auth, and content flags (Arabic / English content, inner categories).
2. **Brand assets** — icon, splash, onboarding images and translation files are swapped per brand; launcher icons are generated with `flutter_launcher_icons`.
3. **Identity** — `change_app_package_name` sets the package / bundle id (e.g. `com.devora.alife`, `com.devora.dinotoys`), and each brand gets its own Firebase project (FCM, Crashlytics, Analytics, Remote Config, App Check).
4. **Server-driven content** — banners, categories, products, coupons, shipping and store info come from the backend, so the store owner (through the admin app) controls the storefront without a new release.

Result: a new brand is a configuration task, and a fix in the core ships to every store.

## Architecture & stack

```mermaid
flowchart LR
  subgraph Brand["Brand layer (per client)"]
    C[AppConstants<br/>name · colours · flags]
    A[Assets & translations]
    F[Firebase project]
  end
  subgraph App["Customer app (Flutter)"]
    UI[Feature screens<br/>home · catalog · cart · orders]
    CU[Cubits<br/>App · Auth · Cart · Categories · Notifications]
    D[Domain<br/>use cases · repositories]
    DS[Data<br/>Dio client · Hive · cache]
  end
  subgraph Admin["Admin app (Flutter)"]
    AD[Dashboard · orders · products<br/>coupons · shipping · PDF export]
  end
  API[(REST API)]
  WS((Socket.IO))
  FB[(Firebase<br/>FCM · Crashlytics · Remote Config · App Check)]

  C --> UI
  A --> UI
  F --> FB
  UI --> CU --> D --> DS --> API
  WS -- live refresh --> CU
  AD --> API
  App --> FB
  Admin --> FB
```

| Layer | Tech |
|---|---|
| UI | Flutter, `flutter_screenutil` / `sizer`, Google Fonts, Lottie, shimmer, carousel |
| State | `flutter_bloc` (Cubit) — App, Auth, Admin, Map and per-feature cubits |
| Architecture | Feature folders; cart, categories, products, notifications and phone-auth split into **data / domain / presentation** with use cases and repository interfaces |
| Networking | Dio (REST), `socket_io_client` for real-time events |
| Local data | Hive (guest cart, favourites), shared-preferences cache |
| Auth | Phone OTP, email/password, Google Sign-In, Facebook Login, `local_auth` biometrics |
| Firebase | Messaging, Analytics, Crashlytics, Performance, Remote Config, App Check |
| Maps | `google_maps_flutter`, `geolocator`, `geocoding` |
| Admin | `fl_chart`, `pdf` + `printing`, `mobile_scanner`, `file_picker` |
| i18n | `easy_localization` (Arabic / English, RTL) |

## Engineering notes

- **Brand isolation without forks.** All brand-specific values live in one constants file and the assets folder; the rest of the code reads from them. A written checklist at the top of the file turns a new brand into a repeatable routine (icon → package id → Firebase → colours → copy → signing keys).
- **Guest-first shopping.** Shoppers can browse, favourite and fill a cart before creating an account. The guest cart (with product variants) and favourites live in Hive boxes. After sign-in, the cart is pushed to the server once per session, and only the items the server accepted are removed locally — so nothing is lost on a weak connection, and there is no "sign up first" wall.
- **Live storefront updates.** A Socket.IO connection joins a `users` room; when the owner changes something in the admin app, a `general` event tells the customer app to refresh — no polling.
- **Role- and permission-based admin.** Login stores the user's role and permission list; admin screens and actions check `hasPerm(...)`, so the same admin build serves owners and staff with different rights.
- **Owner-friendly reporting.** Orders and customers can be filtered by status and date and exported as PDF straight from the phone for bookkeeping or the delivery company.
- **Production monitoring per brand.** Crashlytics, Performance and Analytics are initialised at startup, Remote Config drives runtime switches, and App Check protects the Firebase backend for every brand.

## Results

- **4 brands live on Google Play** from one codebase: Aleefie, Deno Store, StarMart, Irtaah.
- **Aleefie also live on the App Store** (Shopping, released October 2025).
- **10 app builds** (customer + admin) maintained from the same core, including the Pets, Grocery, OCA View and Al-Wathiq storefronts.

## بالعربي

**DevOra** منظومة متاجر إلكترونية "وايت ليبل": تطبيق عميل واحد وتطبيق إدارة واحد مبنيين بـ Flutter، ويتم إعادة تسميتهما وتلوينهما لكل عميل ونشرهما كتطبيقات مستقلة.
من نفس الكود خرجت **أليفي** (مستلزمات الحيوانات الأليفة)، **دينو ستور** (ألعاب أطفال)، **ستار مارت** (أزياء)، و**ارتاح** (خدمات منزلية) — كلها منشورة على Google Play، وأليفي على App Store أيضًا.
التطبيق يدعم السلة كزائر، تسجيل الدخول برقم الهاتف وجوجل وفيسبوك، الكوبونات والشحن حسب المنطقة، الإشعارات، والتحديث اللحظي عبر Socket.IO.
وتطبيق الإدارة يتيح لصاحب المتجر إدارة الطلبات والمنتجات والإعلانات والكوبونات وتصدير التقارير PDF من الموبايل.
دوري: قائد تطوير Flutter — بناء النواة المشتركة، آلية الـ white-label، تطبيق الإدارة، والنشر على المتاجر.

## Links

- Aleefie · أليفي — [Google Play](https://play.google.com/store/apps/details?id=com.devora.alife) · [App Store](https://apps.apple.com/sa/app/id6753914523)
- Deno Store · دينو ستور — [Google Play](https://play.google.com/store/apps/details?id=com.devora.dinotoys)
- StarMart · ستار مارت — [Google Play](https://play.google.com/store/apps/details?id=com.devora.starmart)
- Irtaah · ارتاح — [Google Play](https://play.google.com/store/apps/details?id=com.irtaah.devora)

---
<h3 align="center">Built by Mahmoud Shaker — Senior Flutter Engineer</h3>
<p align="center">
  <a href="https://wa.me/201140279111"><img src="https://img.shields.io/badge/WhatsApp-Chat-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp"></a>
  <a href="https://www.linkedin.com/in/anashaker/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://anashaker.github.io/shaker_portfolio/"><img src="https://img.shields.io/badge/Portfolio-Visit-111827?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio"></a>
  <a href="mailto:mahmoudshaker382001@gmail.com"><img src="https://img.shields.io/badge/Email-Hire%20me-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://khamsat.com/user/sheko201566"><img src="https://img.shields.io/badge/Khamsat-Services-F39C12?style=for-the-badge" alt="Khamsat"></a>
  <a href="https://mostaql.com/u/ShekoShaker"><img src="https://img.shields.io/badge/Mostaql-Freelance-2386C8?style=for-the-badge" alt="Mostaql"></a>
  <a href="https://github.com/ANaSHaker"><img src="https://img.shields.io/badge/GitHub-More%20work-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
</p>

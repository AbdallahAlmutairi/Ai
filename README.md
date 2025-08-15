# Ai

مشروع لتحليل الأسهم باستخدام الذكاء الاصطناعي.

## التشغيل المحلي

1. تثبيت المتطلبات:
   ```bash
   pip install -r requirements.txt
   ```
2. تشغيل الخادم:
   ```bash
   uvicorn backend.app:app --reload
   ```
3. فتح المتصفح على `http://localhost:8000` لعرض الواجهة وتجربة واجهة البرمجة.

### نقاط نهاية إضافية

- `GET /api/watchlist` : استرجاع قائمة المتابعة الحالية.
- `POST /api/watchlist/{symbol}` : إضافة رمز إلى قائمة المتابعة.
- `DELETE /api/watchlist/{symbol}` : إزالة رمز من قائمة المتابعة.
- `GET /api/risk-profile` : معرفة ملف المخاطر الحالي.
- `POST /api/risk-profile/{profile}` : تعيين ملف المخاطر (`conservative`، `moderate`، `aggressive`).
- `GET /api/recommendation/{symbol}?tf=15m` : استرجاع توصية لرمز مع التحقق من الإطار الزمني (`15m`، `1h`، `1d`).


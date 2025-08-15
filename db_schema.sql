-- Schema for analytic trading bot database

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT UNIQUE,
    role TEXT CHECK(role IN ('TRADER','ADMIN'))
);

CREATE TABLE stocks (
    stock_id INTEGER PRIMARY KEY AUTOINCREMENT,
    symbol TEXT NOT NULL UNIQUE,
    company_name TEXT,
    sector TEXT,
    exchange TEXT
);

CREATE TABLE price_history (
    price_id INTEGER PRIMARY KEY AUTOINCREMENT,
    stock_id INTEGER NOT NULL,
    timestamp DATETIME NOT NULL,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume INTEGER,
    FOREIGN KEY (stock_id) REFERENCES stocks(stock_id)
);

CREATE TABLE news_articles (
    news_id INTEGER PRIMARY KEY AUTOINCREMENT,
    stock_id INTEGER,
    headline TEXT NOT NULL,
    source TEXT,
    url TEXT,
    published_at DATETIME NOT NULL,
    sentiment_score REAL,
    FOREIGN KEY (stock_id) REFERENCES stocks(stock_id)
);

CREATE TABLE features (
    feature_id INTEGER PRIMARY KEY AUTOINCREMENT,
    stock_id INTEGER NOT NULL,
    timestamp DATETIME NOT NULL,
    atr REAL,
    momentum REAL,
    volatility REAL,
    liquidity_density REAL,
    sentiment_signal REAL,
    FOREIGN KEY (stock_id) REFERENCES stocks(stock_id)
);

CREATE TABLE recommendations (
    recommendation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    stock_id INTEGER NOT NULL,
    timestamp DATETIME NOT NULL,
    action TEXT CHECK(action IN ('BUY','SELL','WAIT')),
    entry_price REAL,
    stop_loss REAL,
    target_price1 REAL,
    target_price2 REAL,
    confidence REAL,
    reasoning TEXT,
    FOREIGN KEY (stock_id) REFERENCES stocks(stock_id)
);

CREATE TABLE performance_metrics (
    metric_id INTEGER PRIMARY KEY AUTOINCREMENT,
    stock_id INTEGER,
    metric_date DATETIME NOT NULL,
    sharpe REAL,
    sortino REAL,
    max_drawdown REAL,
    signal_hit_rate REAL,
    pnl_after_cost REAL,
    precision_buy REAL,
    recall_buy REAL,
    precision_sell REAL,
    recall_sell REAL,
    response_time_ms INTEGER,
    FOREIGN KEY (stock_id) REFERENCES stocks(stock_id)
);

CREATE TABLE audit_logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    recommendation_id INTEGER NOT NULL,
    log_time DATETIME NOT NULL,
    message TEXT,
    FOREIGN KEY (recommendation_id) REFERENCES recommendations(recommendation_id)
);

CREATE TABLE risk_profiles (
    profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    profile_type TEXT CHECK(profile_type IN ('CONSERVATIVE','MODERATE','AGGRESSIVE')),
    max_position_size REAL,
    max_drawdown_limit REAL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE user_watchlist (
    watch_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    stock_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (stock_id) REFERENCES stocks(stock_id)
);


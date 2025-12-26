# ABANDONED
### Due to Twitter API pricing changes

## 🐦 Twitter Interaction Ranker

A real-time analytics system that listens to the Twitter (X) filtered stream, tracks tweets from specific users, ranks their interactions using an ELO rating system, and analyzes sentiment toward named entities.

This project combines live social data, competitive ranking models, and NLP to measure influence and opinion dynamics over time.

## 🚀 Features

Filtered Stream Listener

Tracks tweets from a configurable list of users in real time.

Uses Twitter’s filtered stream endpoint for low-latency ingestion.

MongoDB Tweet & Entity Store

Tweets are stored in a MongoDB Atlas cluster.

Named entities extracted from each tweet are stored and indexed.

Enables scalable historical queries and entity-level analysis.

Interaction Ranking (ELO System)

Models user interactions (mentions, replies, quote tweets) as competitive events.

Assigns and updates ELO ratings to measure relative influence.

Influence scores evolve continuously based on interaction outcomes.

NLP Sentiment Engine

Tweets are passed through an NLP model to detect sentiment toward extracted entities.

Produces per-entity polarity scores (positive, neutral, negative).

SQLite Sentiment Tracker

Sentiment results are written to a lightweight SQLite database.

Tracks how each user feels about each entity over time.

Enables fast local querying and reporting.

---

## 📦 Installation

```

git clone https://github.com/debin2025/twitter-tracker.git
cd twitter-tracker
pip install -r requirements.txt

```

---

## ⚙️ Configuration

Create a .env file:

```

TWITTER_BEARER_TOKEN=your_bearer_token_here
MONGO_URI=mongodb+srv://user:pass@cluster.mongodb.net/twitter
TRACKED_USERS=123456,789012

```

---

## ▶️ Usage

```

python main.py

```



Searchify: Minimalist Full-Text Search Engine

Searchify is a lightweight, high-performance search application built with Python and Flask. It focuses on efficient data retrieval, smart content highlighting, and a "Quiet Luxury" inspired user interface.

💎 Core Value
The primary value of this project is Search Efficiency. Instead of relying on slow, basic pattern matching, Searchify implements SQLite FTS5 (Full-Text Search) virtual tables.

Speed: Instant results across extensive local datasets.

Relevance: Advanced ranking that mimics modern search engine behavior.

Scalability: Optimized indexing that bridges the gap between raw data and dynamic user interaction.

🔍 How to Search
The engine is pre-seeded with diverse articles. Try searching for these specific keywords to see the engine's precision:

Programming & Dev: Python, Flask, Docker, or JavaScript.

AI & Science: Machine Learning, Black Holes, or CRISPR.

Entertainment: Batman, Christopher Nolan, or Stranger Things.

Literature: 1984, The Great Gatsby, or The Alchemist.

Gastronomy: Carbonara, Pasta, or Chocolate.

Global Travel: Tokyo, Bali, or Santorini.

🚀 Key Features
Full-Text Search Engine

Optimized indexing via SQLite FTS5 for rapid, low-latency query execution.

Smart Snippet Highlighting

A custom regex-based utility that extracts the most relevant text segments and wraps matches in <mark> tags for high visibility.

Persistent Search History

Features a "Recent Searches" section using interactive pills for quick re-entry.

Dual-Theme Support

A seamless Dark/Light mode toggle powered by CSS variables and LocalStorage for persistence.

Server-Side Pagination

Efficiently manages large result sets by loading data in precise, manageable chunks.

🛠 Technical Stack
Backend: Python | Flask

Database: SQLite3 (utilizing the FTS5 Extension)

Frontend: Jinja2 | Vanilla JavaScript | CSS3 (Flexbox & Grid)

Text Processing: Python re module for intelligent snippet generation.

📈 Project Logic
The system works by creating a virtual index of all stored text. When a user submits a query, the backend doesn't just look for matches; it identifies the most relevant "snippets" of text, ensures the UI reflects the user's preferred theme, and updates the search history in real-time.

Would you like me to help you customize the Terracotta and Slate color codes in your style.css to match this new README vibe?
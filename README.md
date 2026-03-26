README.md
Searchify: Minimalist Full-Text Search Engine
Searchify is a lightweight, high-performance search application built with Python and Flask. It demonstrates efficient data retrieval, smart content highlighting, and a clean user experience using a relational database.

Core Value
The primary value of this project is Search Efficiency. Instead of basic pattern matching, Searchify uses SQLite’s FTS5 (Full-Text Search) virtual tables. This allows for "Google-like" speed and relevance across local datasets, bridging the gap between raw data and a dynamic, interactive user interface.

How to Search
The engine is pre-seeded with a wide variety of articles. To see the project in action, try searching for these specific terms or topics:

Programming: Search for "Python", "Flask", "Docker", or "JavaScript".

AI & Science: Look up "Machine Learning", "Black Holes", or "CRISPR".

Entertainment: Search for "Batman", "Christopher Nolan", or "Stranger Things".

Literature: Find classics like "1984", "The Great Gatsby", or "The Alchemist".

Recipes: Try searching for ingredients or dishes like "Carbonara", "Pasta", or "Chocolate".

Travel: Explore destinations like "Tokyo", "Bali", or "Santorini".

Key Features
Full-Text Search Engine: Optimized indexing via SQLite FTS5 for rapid query execution.

Smart Snippet Highlighting: A custom regex utility that extracts relevant text segments and wraps matches in <mark> tags.

Persistent Search History: Tracks recent queries and displays them as interactive pills for quick access.

Dual-Theme Support: A persistent dark/light mode toggle utilizing CSS variables and LocalStorage.

Server-Side Pagination: Efficiently handles result sets by loading data in manageable chunks.

Technical Stack
Backend: Python, Flask

Database: SQLite3 (FTS5 Extension)

Frontend: Jinja2, Vanilla JavaScript, CSS3 (Flexbox/Grid)

Text Processing: Python re module for snippet generation.
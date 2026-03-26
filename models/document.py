from database.db import get_connection

# ─────────────────────────────────────────────
# SEARCH FUNCTIONS
# ─────────────────────────────────────────────

def search_like(query, page=1, per_page=5):
    """LIKE-based search with pagination."""
    offset = (page - 1) * per_page
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *,
               (CASE WHEN title LIKE ? THEN 2 ELSE 0 END +
                CASE WHEN content LIKE ? THEN 1 ELSE 0 END) AS score
        FROM documents
        WHERE title LIKE ? OR content LIKE ?
        ORDER BY score DESC
        LIMIT ? OFFSET ?
    """, (f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%", per_page, offset))
    results = [dict(row) for row in cursor.fetchall()]

    cursor.execute("""
        SELECT COUNT(*) as total FROM documents
        WHERE title LIKE ? OR content LIKE ?
    """, (f"%{query}%", f"%{query}%"))
    total = cursor.fetchone()["total"]

    conn.close()
    return results, total


def search_fulltext(query, page=1, per_page=5):
    """FTS5 full-text search with pagination."""
    offset = (page - 1) * per_page
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT d.*, rank AS score
        FROM documents d
        JOIN documents_fts fts ON d.id = fts.rowid
        WHERE documents_fts MATCH ?
        ORDER BY rank
        LIMIT ? OFFSET ?
    """, (query, per_page, offset))
    results = [dict(row) for row in cursor.fetchall()]

    cursor.execute("""
        SELECT COUNT(*) as total
        FROM documents_fts
        WHERE documents_fts MATCH ?
    """, (query,))
    total = cursor.fetchone()["total"]

    conn.close()
    return results, total


# ─────────────────────────────────────────────
# SEARCH HISTORY FUNCTIONS
# ─────────────────────────────────────────────

def save_history(query):
    """Save a search query to history."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO search_history (query) VALUES (?)", (query,))
    conn.commit()
    conn.close()


def get_recent_history(limit=8):
    """Fetch the most recent unique search queries."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT query, MAX(searched_at) as searched_at
        FROM search_history
        GROUP BY query
        ORDER BY searched_at DESC
        LIMIT ?
    """, (limit,))
    history = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return history
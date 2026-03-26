from flask import Flask, render_template, request
from models.document import search_like, search_fulltext, save_history, get_recent_history
from utils.search import highlight

app = Flask(__name__)

# Register highlight as a Jinja2 global so templates can use it
app.jinja_env.globals['highlight'] = highlight

# Toggle this to switch between LIKE and FULLTEXT search
USE_FULLTEXT = False  # Set to True once you're ready to upgrade

@app.route("/")
def home():
    history = get_recent_history()
    return render_template("index.html", history=history)


@app.route("/search")
def search():
    query = request.args.get("q", "").strip()
    page  = int(request.args.get("page", 1))

    if not query:
        return render_template("index.html", history=get_recent_history())

    # Save to history
    save_history(query)

    # Run the appropriate search
    if USE_FULLTEXT:
        results, total = search_fulltext(query, page)
    else:
        results, total = search_like(query, page)

    per_page    = 5
    total_pages = (total + per_page - 1) // per_page

    return render_template(
        "results.html",
        results=results,
        query=query,
        page=page,
        total=total,
        total_pages=total_pages,
        per_page=per_page
    )


if __name__ == "__main__":
    app.run(debug=True)
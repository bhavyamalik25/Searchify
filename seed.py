import sqlite3
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "searchify.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# ── Create tables ──────────────────────────────────────
cursor.executescript("""
    CREATE TABLE IF NOT EXISTS documents (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        title      TEXT,
        content    TEXT,
        category   TEXT,
        created_at TEXT DEFAULT (datetime('now'))
    );

    CREATE TABLE IF NOT EXISTS search_history (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        query       TEXT,
        searched_at TEXT DEFAULT (datetime('now'))
    );

    CREATE VIRTUAL TABLE IF NOT EXISTS documents_fts
    USING fts5(title, content, content='documents', content_rowid='id');
""")

# ── Sample Data ────────────────────────────────────────
articles = [

    # ── Tech ──────────────────────────────────────────
    ("Getting Started with Python",
     "Python is a beginner-friendly, high-level programming language. It uses clean, readable syntax and is widely used in web development, data science, automation, and AI. Installing Python is easy — just visit python.org and download the latest version. Once installed, you can run scripts from the terminal or use an IDE like VS Code or PyCharm.",
     "Programming"),

    ("Understanding Flask Web Framework",
     "Flask is a lightweight Python web framework. It is called a micro-framework because it does not require particular tools or libraries. Flask is easy to get started with and is great for building APIs and small to medium web applications. Key concepts include routes, templates via Jinja2, and the request/response cycle.",
     "Web Dev"),

    ("What is Machine Learning?",
     "Machine learning is a branch of artificial intelligence that allows systems to learn from data and improve over time without being explicitly programmed. Common types include supervised learning, unsupervised learning, and reinforcement learning. Popular Python libraries for ML include scikit-learn, TensorFlow, and PyTorch.",
     "AI / ML"),

    ("MySQL for Beginners",
     "MySQL is one of the most popular open-source relational database management systems. It uses Structured Query Language SQL to manage data. Basic operations include SELECT, INSERT, UPDATE, and DELETE. MySQL is used by millions of websites and applications to store and retrieve data efficiently.",
     "Database"),

    ("Introduction to REST APIs",
     "A REST API allows different software systems to communicate over HTTP. RESTful APIs use standard HTTP methods: GET to retrieve data, POST to create, PUT to update, and DELETE to remove. They are widely used to build web services and are the backbone of modern web apps.",
     "Web Dev"),

    ("CSS Grid vs Flexbox Explained",
     "CSS Grid and Flexbox are both powerful layout systems in CSS. Flexbox is best for one-dimensional layouts — either a row or a column. Grid is designed for two-dimensional layouts — rows and columns simultaneously. Understanding when to use each is key to building clean, responsive web interfaces.",
     "Frontend"),

    ("Version Control with Git",
     "Git is a distributed version control system used to track changes in code. Key commands include git init, git add, git commit, git push, and git pull. GitHub is a popular platform for hosting Git repositories and collaborating with other developers. Every developer should know the basics of Git.",
     "Tools"),

    ("How Search Engines Work",
     "Search engines crawl the web using bots called spiders. They index the content they find and store it in large databases. When a user searches, the engine ranks pages using algorithms that consider relevance, authority, and user signals. Building your own search engine is a great learning project.",
     "Computer Science"),

    ("Introduction to Docker",
     "Docker is a platform that lets developers package applications into containers — lightweight, standalone environments that include everything needed to run the app. Containers are isolated from each other and the host system, making deployment consistent across environments. Docker is widely used in DevOps and cloud deployments.",
     "DevOps"),

    ("JavaScript Async/Await Explained",
     "Async/await is a modern JavaScript syntax for handling asynchronous operations. It is built on top of Promises and makes asynchronous code look and behave more like synchronous code. The async keyword declares an asynchronous function, and await pauses execution until the Promise resolves. This makes code far more readable than nested callbacks.",
     "Programming"),

    # ── Movies & TV Shows ──────────────────────────────
    ("The Dark Knight",
     "The Dark Knight is a 2008 superhero film directed by Christopher Nolan. It follows Batman as he faces the Joker, a criminal mastermind who plunges Gotham City into chaos. Heath Ledger's iconic portrayal of the Joker won him a posthumous Academy Award. The film is widely considered one of the greatest movies ever made, praised for its dark tone, complex characters, and thrilling action sequences.",
     "Movies"),

    ("Breaking Bad",
     "Breaking Bad is an American crime drama television series created by Vince Gilligan. It follows Walter White, a high school chemistry teacher diagnosed with cancer, who teams up with former student Jesse Pinkman to produce methamphetamine. The show is acclaimed for its writing, character development, and cinematography. It ran for five seasons from 2008 to 2013 and is considered one of the greatest TV series ever made.",
     "TV Shows"),

    ("Inception",
     "Inception is a 2010 science fiction thriller directed by Christopher Nolan. The film stars Leonardo DiCaprio as a thief who steals information by entering people's dreams. He is tasked with planting an idea into a target's subconscious. Known for its complex narrative, stunning visuals, and the spinning top ending that sparked endless debate, Inception is a modern classic of science fiction cinema.",
     "Movies"),

    ("Stranger Things",
     "Stranger Things is a science fiction horror drama series on Netflix created by the Duffer Brothers. Set in the 1980s in the fictional town of Hawkins, Indiana, the show follows a group of kids who encounter supernatural forces and secret government experiments. It stars Millie Bobby Brown as Eleven, a girl with psychokinetic abilities. The show is beloved for its nostalgic atmosphere and compelling characters.",
     "TV Shows"),

    ("Interstellar",
     "Interstellar is a 2014 epic science fiction film directed by Christopher Nolan. A team of astronauts travels through a wormhole near Saturn in search of a new home for humanity. The film explores themes of love, time, and survival. It features stunning visual effects and a haunting score by Hans Zimmer. The depiction of black holes in the film was praised by scientists for its accuracy.",
     "Movies"),

    ("Game of Thrones",
     "Game of Thrones is a fantasy drama television series based on George R. R. Martin's novels. It follows noble families fighting for control of the Iron Throne of the Seven Kingdoms. Known for its complex characters, unexpected plot twists, and large scale battles, it became a global phenomenon. The show ran for eight seasons from 2011 to 2019 on HBO.",
     "TV Shows"),

    # ── Books & Literature ─────────────────────────────
    ("To Kill a Mockingbird",
     "To Kill a Mockingbird is a novel by Harper Lee published in 1960. Set in the American South during the 1930s, it follows young Scout Finch as her father, lawyer Atticus Finch, defends a Black man falsely accused of a crime. The novel explores themes of racial injustice, moral growth, and compassion. It won the Pulitzer Prize and is considered a classic of American literature.",
     "Books"),

    ("1984 by George Orwell",
     "1984 is a dystopian novel by George Orwell published in 1949. It is set in a totalitarian society ruled by Big Brother, where the government controls every aspect of life including thought and language. The protagonist Winston Smith works for the Ministry of Truth rewriting history. The novel introduced concepts like doublethink, thoughtcrime, and newspeak that remain culturally relevant today.",
     "Books"),

    ("The Great Gatsby",
     "The Great Gatsby is a novel by F. Scott Fitzgerald published in 1925. Set in the Jazz Age on Long Island, it follows narrator Nick Carraway and his mysterious neighbour Jay Gatsby, who throws lavish parties in hopes of reuniting with his lost love Daisy Buchanan. The novel is a critique of the American Dream and the hollow pursuit of wealth and status.",
     "Books"),

    ("Harry Potter and the Philosopher's Stone",
     "Harry Potter and the Philosopher's Stone is the first novel in J.K. Rowling's Harry Potter series. It follows Harry, an orphan who discovers he is a wizard and enrolls at Hogwarts School of Witchcraft and Wizardry. There he makes friends, learns magic, and uncovers the truth about his parents' death at the hands of the dark wizard Voldemort. The book launched one of the best selling series in history.",
     "Books"),

    ("The Alchemist",
     "The Alchemist is a philosophical novel by Brazilian author Paulo Coelho published in 1988. It follows Santiago, an Andalusian shepherd boy who dreams of finding treasure near the Egyptian pyramids. Along his journey he meets various characters who teach him about following his Personal Legend. The novel has sold over 65 million copies worldwide and has been translated into 80 languages.",
     "Books"),

    # ── Recipes & Food ─────────────────────────────────
    ("Classic Spaghetti Carbonara",
     "Spaghetti Carbonara is a classic Italian pasta dish made with eggs, hard cheese, cured pork, and black pepper. Cook spaghetti until al dente. Fry pancetta or guanciale until crispy. Mix eggs and parmesan in a bowl. Combine hot pasta with pork, remove from heat, add egg mixture and toss quickly. The heat from the pasta cooks the eggs into a creamy sauce without scrambling. Never add cream to a true carbonara.",
     "Recipe"),

    ("Homemade Margherita Pizza",
     "Margherita pizza is the simplest and most iconic Italian pizza. Make dough with flour, yeast, salt, and olive oil. Let it rise for an hour. Spread tomato sauce, add fresh mozzarella slices and basil leaves. Bake at the highest oven temperature for 10 to 12 minutes until crust is golden and cheese is bubbling. Less is more with this classic. The best pizzas use only three or four quality ingredients.",
     "Recipe"),

    ("Chicken Tikka Masala",
     "Chicken Tikka Masala is a rich, creamy curry dish popular worldwide. Marinate chicken in yogurt and spices like cumin, coriander, turmeric, and garam masala. Grill or bake the chicken until slightly charred. Make the masala sauce by cooking onions, garlic, ginger, tomatoes, and cream together. Add the grilled chicken to the sauce and simmer for 15 minutes. Serve hot with naan bread or basmati rice.",
     "Recipe"),

    ("Avocado Toast with Poached Egg",
     "Avocado toast is a quick and nutritious breakfast. Toast sourdough bread until golden and crispy. Mash ripe avocado with lemon juice, salt, and chili flakes. Spread generously on toast. Poach an egg by simmering water with a splash of vinegar, swirling the water and dropping in the egg for 3 minutes. Place on top of the avocado toast and season with black pepper and sea salt.",
     "Recipe"),

    ("Chocolate Lava Cake",
     "Chocolate lava cake is a decadent dessert with a gooey molten center. Melt dark chocolate and butter together. Whisk eggs, egg yolks, and sugar until pale. Fold in the chocolate mixture and a small amount of flour. Pour into buttered ramekins and refrigerate for 30 minutes. Bake at 220 degrees Celsius for exactly 12 minutes. The outside should be set but the center should be liquid. Serve immediately with vanilla ice cream.",
     "Recipe"),

    ("Classic Beef Burger",
     "A great beef burger starts with quality meat. Use 80 percent lean ground beef for the juiciest results. Season with salt and pepper only — let the beef shine. Form patties slightly wider than your bun as they shrink while cooking. Cook on a hot cast iron pan or grill for 3 to 4 minutes per side. Add cheese in the last minute. Toast the buns. Layer with lettuce, tomato, onion, pickles, and your favourite sauce.",
     "Recipe"),

    # ── Travel & Places ────────────────────────────────
    ("Tokyo — The City That Never Sleeps",
     "Tokyo is the capital of Japan and one of the most exciting cities in the world. From the neon lights of Shinjuku to the historic temples of Asakusa, Tokyo blends ancient tradition with futuristic technology. Must visit spots include Shibuya Crossing, Senso-ji Temple, Tsukiji Fish Market, and Akihabara. Japanese cuisine in Tokyo is world class — from ramen and sushi to street food and conveyor belt restaurants.",
     "Travel"),

    ("Paris — The City of Light",
     "Paris is the capital of France and one of the most visited cities in the world. Famous landmarks include the Eiffel Tower, the Louvre Museum, Notre Dame Cathedral, and the Champs-Elysees. Paris is known for its art, fashion, cuisine, and romantic atmosphere. The city's cafe culture, patisseries, and wine bars make it a paradise for food lovers. Best visited in spring or autumn to avoid summer crowds.",
     "Travel"),

    ("Bali — Island of the Gods",
     "Bali is an Indonesian island known for its forested volcanic mountains, iconic rice paddies, beaches, and coral reefs. The island is famous for its Hindu temples, traditional dance performances, and spiritual retreats. Popular areas include Ubud for arts and culture, Seminyak for nightlife, and Uluwatu for surfing. Bali's food scene offers incredible local dishes like nasi goreng, satay, and fresh tropical fruits.",
     "Travel"),

    ("New York City — The Big Apple",
     "New York City is the most populous city in the United States and a global hub for finance, art, fashion, and culture. Iconic attractions include the Statue of Liberty, Central Park, Times Square, the Empire State Building, and the Brooklyn Bridge. NYC is a food lover's paradise with thousands of restaurants representing every cuisine in the world. The city's subway system runs 24 hours a day, seven days a week.",
     "Travel"),

    ("Santorini — Greece's Crown Jewel",
     "Santorini is a stunning Greek island in the Aegean Sea, famous for its whitewashed buildings with blue domed roofs, dramatic cliffs, and breathtaking sunsets. The island was shaped by a massive volcanic eruption thousands of years ago. Oia village is the most photographed spot on the island. Santorini is also known for its unique wines, fresh seafood, and luxurious clifftop hotels with infinity pools.",
     "Travel"),

    # ── Science & Space ────────────────────────────────
    ("Black Holes Explained",
     "A black hole is a region of spacetime where gravity is so strong that nothing, not even light, can escape from it. Black holes form when massive stars collapse at the end of their life cycle. The boundary around a black hole is called the event horizon. At the center lies the singularity where density becomes infinite. In 2019 scientists captured the first ever image of a black hole using the Event Horizon Telescope.",
     "Science"),

    ("The Theory of Relativity",
     "Albert Einstein's theory of relativity consists of two parts: special relativity and general relativity. Special relativity introduced the famous equation E equals mc squared, showing that mass and energy are interchangeable. General relativity describes gravity as the curvature of spacetime caused by mass. These theories revolutionized our understanding of space, time, and the universe and have been confirmed by countless experiments.",
     "Science"),

    ("CRISPR — Gene Editing Explained",
     "CRISPR-Cas9 is a revolutionary gene editing technology that allows scientists to add, remove, or alter DNA sequences in living organisms. It works like molecular scissors, precisely cutting DNA at specific locations. CRISPR has enormous potential in medicine, including treating genetic diseases, developing cancer therapies, and creating disease resistant crops. It was discovered by Jennifer Doudna and Emmanuelle Charpentier who won the Nobel Prize in Chemistry in 2020.",
     "Science"),

    ("The James Webb Space Telescope",
     "The James Webb Space Telescope is the most powerful space telescope ever built. Launched in December 2021, it observes the universe in infrared light and can see further back in time than any previous telescope. Webb is designed to study the formation of the first stars and galaxies, examine exoplanet atmospheres for signs of life, and reveal the mysteries of dark matter and dark energy. Its first images stunned the scientific community.",
     "Science"),

    ("How the Human Brain Works",
     "The human brain is the most complex organ in the known universe. It contains approximately 86 billion neurons connected by trillions of synapses. The brain is divided into regions with specialized functions: the frontal lobe handles decision making, the hippocampus manages memory, and the amygdala processes emotions. The brain consumes about 20 percent of the body's total energy despite being only 2 percent of its weight.",
     "Science"),

    # ── History & Culture ──────────────────────────────
    ("The Rise and Fall of the Roman Empire",
     "The Roman Empire was one of the largest and most powerful empires in history, at its peak spanning from Britain to Mesopotamia. Founded as a republic in 509 BC, Rome transitioned to an empire under Julius Caesar and Augustus. The empire brought roads, aqueducts, law, and architecture to the ancient world. It fell in 476 AD due to a combination of military pressures, economic troubles, and political instability.",
     "History"),

    ("The Renaissance — Rebirth of Art and Science",
     "The Renaissance was a cultural and intellectual movement that began in Italy in the 14th century and spread across Europe. It marked a renewed interest in classical Greek and Roman ideas, art, and science. Leonardo da Vinci, Michelangelo, and Raphael produced some of the world's greatest artworks during this period. The Renaissance also saw major scientific advances by figures like Galileo and Copernicus that challenged established beliefs.",
     "History"),

    ("World War II — A Global Conflict",
     "World War II was the deadliest conflict in human history, lasting from 1939 to 1945. It involved most of the world's nations divided into two opposing alliances: the Allies and the Axis powers. The war began with Germany's invasion of Poland. Key events include the Holocaust, the Battle of Britain, the attack on Pearl Harbor, D-Day, and the atomic bombings of Hiroshima and Nagasaki. The war resulted in an estimated 70 to 85 million deaths.",
     "History"),

    ("Ancient Egypt and the Pyramids",
     "Ancient Egypt was one of the world's earliest and longest lasting civilizations, flourishing along the Nile River for over 3000 years. The Egyptians are famous for their monumental architecture including the Great Pyramids of Giza and the Sphinx. They developed one of the earliest writing systems called hieroglyphics. Ancient Egyptian religion centered around the afterlife, and pharaohs were buried with treasure and mummified to preserve their bodies for eternity.",
     "History"),

    ("The Space Race — USA vs USSR",
     "The Space Race was a mid 20th century competition between the United States and the Soviet Union for supremacy in space exploration. It began with the Soviet launch of Sputnik, the first artificial satellite, in 1957. The Soviets also sent the first human, Yuri Gagarin, into space in 1961. The United States responded by landing astronauts Neil Armstrong and Buzz Aldrin on the Moon in 1969 during the Apollo 11 mission, widely seen as the defining moment of the Space Race.",
     "History"),
]

cursor.executemany(
    "INSERT INTO documents (title, content, category) VALUES (?, ?, ?)",
    articles
)

# Populate FTS index
cursor.execute("""
    INSERT INTO documents_fts (rowid, title, content)
    SELECT id, title, content FROM documents
""")

conn.commit()
conn.close()

print(f"✅ Database created and seeded successfully with {len(articles)} articles!")
print(f"📁 Location: {DB_PATH}")
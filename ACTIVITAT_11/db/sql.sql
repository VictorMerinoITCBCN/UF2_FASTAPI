CREATE TABLE IF NOT EXISTS Language (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Theme (
    id SERIAL PRIMARY KEY,
    langID VARCHAR(50),
    theme VARCHAR(255),
    FOREIGN KEY (langID) REFERENCES Language(id)
);

CREATE TABLE IF NOT EXISTS TextRender (
    id SERIAL PRIMARY KEY,
    langID VARCHAR(50) NOT NULL,
    base TEXT NOT NULL,
    text TEXT NOT NULL,
    FOREIGN KEY (langID) REFERENCES Language(id)
);

CREATE TABLE IF NOT EXISTS Letter (
    id SERIAL PRIMARY KEY,
    langID VARCHAR(50) NOT NULL,
    character CHAR(1) NOT NULL,
    FOREIGN KEY (langID) REFERENCES Language(id),
    CONSTRAINT UC_Letter UNIQUE (langID, character)
);

CREATE TABLE IF NOT EXISTS Word (
    id SERIAL PRIMARY KEY,
    langID VARCHAR(50) NOT NULL,
    word VARCHAR(255) NOT NULL,
    themeID INT NOT NULL,
    FOREIGN KEY (langID) REFERENCES Language(id),
    FOREIGN KEY (themeID) REFERENCES Theme(id)
);

CREATE TABLE IF NOT EXISTS Score (
    id SERIAL PRIMARY KEY,
    playerID INT NOT NULL,
    score INT NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Player (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    win INT DEFAULT 0,
    lose INT DEFAULT 0,
    bestScoreID INT,
    FOREIGN KEY (bestScoreID) REFERENCES Score(id)
);

INSERT INTO TextRender (langID, base, text) VALUES
-- Inglés
('EN', 'start_game', 'start game'),
-- Español
('ES', 'start_game', 'comenzar partida'),

-- Francés
('FR', 'start_game', 'commencer le jeu');

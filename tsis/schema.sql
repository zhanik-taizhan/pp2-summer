-- =========================
-- CONTACTS
-- =========================

CREATE TABLE IF NOT EXISTS contacts(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(100),
    birthday DATE
);

-- =========================
-- GROUPS
-- =========================

CREATE TABLE IF NOT EXISTS groups_table(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- =========================
-- PHONES
-- =========================

CREATE TABLE IF NOT EXISTS phones(
    id SERIAL PRIMARY KEY,
    contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
    phone VARCHAR(20) NOT NULL,
    type VARCHAR(20) CHECK(type IN ('home','work','mobile'))
);

-- =========================
-- CONNECT CONTACTS -> GROUPS
-- =========================

ALTER TABLE contacts
ADD COLUMN IF NOT EXISTS group_id INTEGER REFERENCES groups_table(id);
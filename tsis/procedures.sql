-- ======================================
-- ADD PHONE
-- ======================================

CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    cid INTEGER;
BEGIN
    SELECT id
    INTO cid
    FROM contacts
    WHERE name = p_contact_name;

    IF cid IS NULL THEN
        RAISE NOTICE 'Contact not found';
        RETURN;
    END IF;

    INSERT INTO phones(contact_id, phone, type)
    VALUES (cid, p_phone, p_type);
END;
$$;


-- ======================================
-- MOVE TO GROUP
-- ======================================

CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    gid INTEGER;
BEGIN

    SELECT id
    INTO gid
    FROM groups_table
    WHERE name = p_group_name;

    IF gid IS NULL THEN

        INSERT INTO groups_table(name)
        VALUES (p_group_name);

        SELECT id
        INTO gid
        FROM groups_table
        WHERE name = p_group_name;

    END IF;

    UPDATE contacts
    SET group_id = gid
    WHERE name = p_contact_name;

END;
$$;
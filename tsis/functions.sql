CREATE OR REPLACE FUNCTION search_contacts(
    p_query TEXT
)
RETURNS TABLE(
    name VARCHAR,
    email VARCHAR,
    birthday DATE,
    phone VARCHAR,
    phone_type VARCHAR,
    group_name VARCHAR
)
LANGUAGE plpgsql
AS
$$
BEGIN

RETURN QUERY

SELECT

c.name,
c.email,
c.birthday,
p.phone,
p.type,
g.name

FROM contacts c

LEFT JOIN phones p
ON c.id = p.contact_id

LEFT JOIN groups_table g
ON c.group_id = g.id

WHERE

c.name ILIKE '%' || p_query || '%'

OR

c.email ILIKE '%' || p_query || '%'

OR

p.phone ILIKE '%' || p_query || '%';

END;
$$;
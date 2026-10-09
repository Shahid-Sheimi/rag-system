-- Optional: instant sync for PostgreSQL. Run once, then set REALTIME_POSTGRES=true.
CREATE OR REPLACE FUNCTION rag_notify() RETURNS trigger AS $$
DECLARE rec record;
BEGIN
  IF TG_OP = 'DELETE' THEN rec := OLD; ELSE rec := NEW; END IF;
  PERFORM pg_notify('rag_changes', json_build_object(
      'table', TG_TABLE_NAME,
      'op',    TG_OP,
      'pk',    to_json(rec) ->> TG_ARGV[0]
  )::text);
  RETURN NULL;
END;
$$ LANGUAGE plpgsql;

-- Repeat per table; the argument is the primary-key column name.
DROP TRIGGER IF EXISTS products_rag ON products;
CREATE TRIGGER products_rag
AFTER INSERT OR UPDATE OR DELETE ON products
FOR EACH ROW EXECUTE FUNCTION rag_notify('id');

-- MySQL / SQL Server / Oracle: no LISTEN/NOTIFY. Use the polling sync (works on any database)
-- or stream changes with Debezium -> Kafka and call sync_row() from a consumer.

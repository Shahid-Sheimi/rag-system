-- Near-real-time sync for SQL Server. Run once per database (as a user allowed to create
-- tables/triggers), then set REALTIME_OUTBOX=true and OUTBOX_TABLE=dbo.rag_outbox in .env.

-- 1) Outbox table (shared by all tables)
IF OBJECT_ID('dbo.rag_outbox') IS NULL
CREATE TABLE dbo.rag_outbox (
    id         BIGINT IDENTITY(1,1) PRIMARY KEY,
    table_name NVARCHAR(128) NOT NULL,
    pk         NVARCHAR(128) NOT NULL,
    op         VARCHAR(10)   NOT NULL,                 -- UPSERT | DELETE
    created_at DATETIME2     NOT NULL DEFAULT SYSUTCDATETIME()
);
GO

-- 2) One trigger per table. Replace dbo.customers / 'customers' / the pk column `id`.
--    Works for single and bulk statements (set-based, uses inserted/deleted).
CREATE OR ALTER TRIGGER dbo.trg_customers_rag
ON dbo.customers
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO dbo.rag_outbox (table_name, pk, op)
    SELECT 'customers', CAST(i.id AS NVARCHAR(128)), 'UPSERT' FROM inserted i;

    INSERT INTO dbo.rag_outbox (table_name, pk, op)
    SELECT 'customers', CAST(d.id AS NVARCHAR(128)), 'DELETE'
    FROM deleted d
    WHERE NOT EXISTS (SELECT 1 FROM inserted i WHERE i.id = d.id);
END;
GO

-- 3) Permissions for the app's login (replace rag_user):
--    GRANT SELECT ON dbo.customers TO rag_user;                       -- each indexed table
--    GRANT SELECT, DELETE ON dbo.rag_outbox TO rag_user;

-- Tip: keep the outbox small. The app deletes rows after processing; if the app is down for a
-- long time the polling sync (interval_seconds) reconciles everything when it comes back,
-- so you can safely TRUNCATE TABLE dbo.rag_outbox if it ever grows large.

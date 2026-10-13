CREATE TABLE chart_of_accounts (
    account_id SERIAL PRIMARY KEY,
    account_code VARCHAR(20) UNIQUE NOT NULL,
    account_name VARCHAR(100) NOT NULL,
    normal_balance VARCHAR(10) CHECK (normal_balance IN ('DEBIT','CREDIT')),
    report_classification VARCHAR(50)
);

CREATE TABLE journal_headers (
    header_id SERIAL PRIMARY KEY,
    trx_date DATE NOT NULL,
    reference_no VARCHAR(50) UNIQUE,
    description TEXT,
    status_posting VARCHAR(10) CHECK (status_posting IN ('DRAFT','POSTED','VOID'))
);

CREATE TABLE journal_lines (
    line_id SERIAL PRIMARY KEY,
    header_id INT REFERENCES journal_headers(header_id) ON DELETE RESTRICT,
    account_id INT REFERENCES chart_of_accounts(account_id) ON DELETE RESTRICT,
    debit NUMERIC(15,2) CHECK (debit >= 0) DEFAULT 0,
    credit NUMERIC(15,2) CHECK (credit >= 0) DEFAULT 0,
    CHECK (NOT (debit = 0 AND credit = 0))
);
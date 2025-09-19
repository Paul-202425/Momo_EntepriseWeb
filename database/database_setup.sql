--------------------------------------------------------------------------------
-- Script Name: database_setup.sql
-- Description: Creates and documents the MTN Mobile Money transaction database schema. 
--              Includes table creation, constraints, comments, indexes, and sample data.
-- Author: Gabriella Ange Ahirwe & Oriane Uwineza
-- Date:   2025-09-19
--------------------------------------------------------------------------------

-- Users Table
CREATE TABLE users(
  user_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique identifier for each user',
  msisdn VARCHAR(20)  NOT NULL COMMENT 'Mobile phone number of the user (MSISDN)',
  full_name VARCHAR(120) NULL COMMENT 'Full name of the user, may be null if unknown',
  CONSTRAINT uq_users_msisdn UNIQUE (msisdn),
  CHECK (CHAR_LENGTH(msisdn) BETWEEN 8 AND 20)
) COMMENT='Mobile money users/participants';

-- Transaction_Categories
CREATE TABLE transaction_categories (
  category_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique identifier for each transaction category',
  code VARCHAR(30)  NOT NULL COMMENT 'Short unique code for the category (e.g., DEPOSIT, WITHDRAW)',
  name VARCHAR(80)  NOT NULL COMMENT 'Descriptive name of the category',
  CONSTRAINT uq_categories_code UNIQUE (code)
) COMMENT='Lookup for transaction types';

-- Transactions
CREATE TABLE transactions (
  tx_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique identifier for each transaction',
  amount DECIMAL(12,2) NOT NULL COMMENT 'Transaction amount (positive values only)',
  tx_datetime  DATETIME NOT NULL COMMENT 'Date and time when the transaction occurred',
  category_id  INT NOT NULL COMMENT 'Foreign key linking to the type/category of the transaction',
  CONSTRAINT fk_tx_category
    FOREIGN KEY (category_id) REFERENCES transaction_categories(category_id)
    ON UPDATE RESTRICT ON DELETE RESTRICT,
  CHECK (amount > 0)
) COMMENT='Financial transactions captured from SMS';

-- Helpful indexes
CREATE INDEX ix_tx_datetime ON transactions (tx_datetime);
CREATE INDEX ix_tx_category ON transactions (category_id);

-- Transaction_Participants
CREATE TABLE transaction_participants (
  tx_id INT NOT NULL COMMENT 'Foreign key referencing the related transaction',
  user_id INT NOT NULL COMMENT 'Foreign key referencing the participating user',
  role VARCHAR(20) NOT NULL COMMENT 'Role of the participant in the transaction (sender, receiver, agent, merchant)',
  PRIMARY KEY (tx_id, user_id, role),
  CONSTRAINT fk_tp_tx
    FOREIGN KEY (tx_id) REFERENCES transactions(tx_id)
    ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT fk_tp_user
    FOREIGN KEY (user_id) REFERENCES users(user_id)
    ON UPDATE RESTRICT ON DELETE RESTRICT,
  CHECK (role IN ('sender','receiver','agent','merchant'))
) COMMENT='Participants and roles per transaction';

-- System_Logs
CREATE TABLE system_logs (
  log_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique identifier for each log entry',
  event_type VARCHAR(40) NOT NULL COMMENT 'Type of event being logged (e.g., parsed, validated, inserted, error)',
  message TEXT NOT NULL COMMENT 'Detailed description of the log event or error message',
  tx_id INT NULL COMMENT 'Optional reference to the related transaction (if applicable)',
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Timestamp when the log entry was created',
  CONSTRAINT fk_log_tx
    FOREIGN KEY (tx_id) REFERENCES transactions(tx_id)
    ON UPDATE CASCADE ON DELETE SET NULL
) COMMENT='ETL/process logs linked to transactions when relevant';

-- categories
INSERT INTO transaction_categories (code, name) VALUES
('P2P','Peer to Peer Transfer'),
('AIRTIME','Airtime Top-up'),
('BILL','Bill Payment'),
('CASHOUT','Cash Withdrawal'),
('MERCHANT','Merchant Payment');

-- users
INSERT INTO users (msisdn, full_name) VALUES
('250788000001','Alice U'),
('250788000002','Bob V'),
('250788000003','Chantal W'),
('250788000004','David X'),
('250788000005','Eva Y');

-- transactions
INSERT INTO transactions (amount, tx_datetime, category_id) VALUES
(12500.00, '2025-09-18 09:12:00', 1),
(  500.00, '2025-09-18 10:05:00', 2),
( 3200.00, '2025-09-18 10:07:10', 5),
( 9000.00, '2025-09-18 11:22:45', 3),
( 2500.00, '2025-09-18 12:00:00', 4);

-- participants (roles)
INSERT INTO transaction_participants (tx_id, user_id, role) VALUES
(1,1,'sender'), (1,2,'receiver'),
(2,1,'sender'),
(3,3,'sender'), (3,5,'merchant'),
(4,2,'sender'), (4,4,'receiver'),
(5,5,'sender');

-- logs (some attached to tx, some generic)
INSERT INTO system_logs (event_type, message, tx_id) VALUES
('parsed','Parsed message OK',1),
('validated','All checks passed',1),
('error','Missing category in payload',NULL),
('inserted','Row inserted',2),
('parsed','Parsed message OK',3);
)



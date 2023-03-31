--NOT UP TO DATE
--DO NOT USE
CREATE TABLE Account
(
    accountID INT AUTO_INCREMENT
        PRIMARY KEY,
    type      INT DEFAULT 1 NOT NULL,
    username  VARCHAR       NULL
        UNIQUE,
    firstName VARCHAR       NULL,
    lastName  VARCHAR       NULL,
    email     VARCHAR       NULL
);

CREATE TABLE Category
(
    categoryID   INT AUTO_INCREMENT
        PRIMARY KEY,
    owner        INT           NULL,
    name VARCHAR       NULL,
    visibility   INT DEFAULT 0 NULL,
    description  VARCHAR       NULL,
    FOREIGN KEY (owner) REFERENCES Account (accountID)
);

CREATE TABLE Course
(
    categoryID INT     NOT NULL
        PRIMARY KEY
        UNIQUE
        REFERENCES Category (categoryID),
    department VARCHAR NULL,
    course     INT     NULL,
    section    INT     NULL,
    startDate  DATE    NULL,
    endDate    DATE    NULL,
    FOREIGN KEY (categoryID) REFERENCES Category (categoryID)
)
    COMMENT 'Specialized Category';

CREATE TABLE Subscription
(
    course     INT NOT NULL,
    subscriber INT NOT NULL,
    FOREIGN KEY (course) REFERENCES Course (categoryID),
    FOREIGN KEY (subscriber) REFERENCES Account (accountID)
)
    COMMENT 'Subscription relationship table';

CREATE TABLE Event
(
    categoryID INT           NULL,
    eventID    INT AUTO_INCREMENT
        PRIMARY KEY,
    type       INT DEFAULT 0 NULL,
    name       VARCHAR       NULL,
    startDate  DATE          NULL,
    endDate    DATE          NULL,
    visibility INT DEFAULT 0 NULL,
    FOREIGN KEY (categoryID) REFERENCES Category (categoryID)
);

CREATE TABLE Deliverable
(
    eventID      INT  NULL
        PRIMARY KEY
        UNIQUE,
    weight       INT  NULL,
    timeEstimate TIME NULL,
    timeSpent    TIME NULL,
    FOREIGN KEY (eventID) REFERENCES Event (eventID)
)
    COMMENT 'Specialized Event';

CREATE TABLE Notification
(
    notifyID   INT AUTO_INCREMENT
        PRIMARY KEY,
    eventID    INT     NULL,
    accountID  INT     NULL,
    notifyDate DATE    NULL,
    info       VARCHAR NULL,
    FOREIGN KEY (eventID) REFERENCES Event (eventID),
    FOREIGN KEY (accountID) REFERENCES Account (accountID)
);

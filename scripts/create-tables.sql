
-- Create the database
CREATE DATABASE Tulip;
GO

-- Create the tables

USE Tulip;
GO

-- Users Table
CREATE TABLE Users (
    UserID INT IDENTITY(1,1) PRIMARY KEY,
	Firstname NVARCHAR(150),
	Email NVARCHAR(150),
    Password NVARCHAR(150)
);

-- Images Table
CREATE TABLE Images (
    ImageID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT FOREIGN KEY REFERENCES Users(UserID),
    ImagePath NVARCHAR(MAX),
    UploadDate DATETIME
);

-- Likes Table
CREATE TABLE Likes (
    LikeID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT FOREIGN KEY REFERENCES Users(UserID),
    ImageID INT FOREIGN KEY REFERENCES Images(ImageID),
    LikeDate DATETIME,
);

-- Downloads Table
CREATE TABLE Downloads (
    DownloadID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT FOREIGN KEY REFERENCES Users(UserID),
    ImageID INT FOREIGN KEY REFERENCES Images(ImageID),
    DownloadDate DATETIME,
);

-- Tags Table
CREATE TABLE Tags (
    TagID INT IDENTITY(1,1) PRIMARY KEY,
    TagName NVARCHAR(50),
);

-- ImageTags Table (Associative Table for M:N relationship between Images and Tags)
CREATE TABLE ImageTags (
    ImageTagID INT IDENTITY(1,1) PRIMARY KEY,
    ImageID INT FOREIGN KEY REFERENCES Images(ImageID),
    TagID INT FOREIGN KEY REFERENCES Tags(TagID),
);

-- DominantColors Table
CREATE TABLE Colors (
    ColorID INT IDENTITY(1,1) PRIMARY KEY,
    ImageID INT FOREIGN KEY REFERENCES Images(ImageID),
    ColorHex NVARCHAR(7), -- Assuming a standard hexadecimal color representation (e.g., "#RRGGBB")
);

GO

-- Create Logins

USE master;
GO

CREATE LOGIN TulipAppLogin WITH PASSWORD = 'T$l1p4pp!0g1n'

GO

-- Create Users and Assign Permissions

USE Tulip;
GO

CREATE USER TulipAppUser FOR LOGIN TulipAppLogin;

GO

GRANT SELECT, INSERT, UPDATE ON Users TO TulipAppUser;

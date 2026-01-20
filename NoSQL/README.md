# NoSQL - MongoDB

## Description

This project introduces **NoSQL databases** using **MongoDB**.  
It covers the core concepts of NoSQL, the differences between SQL and NoSQL databases, and how to perform basic database operations using both **MongoDB shell scripts** and **Python (PyMongo)**.

The project is designed to help understand how document-based databases work and how they are used in backend development.

---

## Learning Objectives

At the end of this project, you should be able to explain:

- What NoSQL means
- The difference between SQL and NoSQL
- What ACID is
- What a document-oriented database is
- The different types of NoSQL databases
- The benefits of NoSQL databases
- How to query information from a NoSQL database
- How to insert, update, and delete data in a NoSQL database
- How to use MongoDB
- How to use MongoDB with Python (PyMongo)

---

## Technologies

- **MongoDB 4.4**
- **MongoDB Shell**
- **Python 3.9**
- **PyMongo 4.8.0**
- **Ubuntu 20.04 LTS**

---

## Requirements

### MongoDB Command Files

- All files are interpreted using **MongoDB 4.4**
- All files end with a new line
- The first line of each file is a comment:
  ```js
  // my comment
File length is checked using wc

Python Scripts

Interpreted using Python 3.9

First line must be:

#!/usr/bin/env python3


All files end with a new line

Code follows pycodestyle (v2.5.*)

All modules and functions include documentation

Code is not executed on import

Uses PyMongo 4.8.0

File length is checked using wc

MongoDB Installation (Sandbox / Ubuntu 22.04)

MongoDB 4.4 requires libssl1.1, which is not included by default in Ubuntu 22.04.

Install dependency
echo "deb http://security.ubuntu.com/ubuntu focal-security main" | sudo tee /etc/apt/sources.list.d/focal-security.list
sudo apt update
sudo apt install -y libssl1.1
sudo rm /etc/apt/sources.list.d/focal-security.list
sudo apt update

Add MongoDB repository
curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt update

Install MongoDB
sudo apt install -y mongodb-org

Start MongoDB
sudo mkdir -p /var/lib/mongodb /var/log/mongodb
sudo chown -R mongodb:mongodb /var/lib/mongodb /var/log/mongodb
sudo -u mongodb /usr/bin/mongod --config /etc/mongod.conf &

Verify installation
mongod --version

Files
File	Description
0-list_databases	Lists all databases in MongoDB
README.md	Project documentation

Additional tasks include:

Creating databases and collections

Inserting documents

Querying documents

Updating documents

Deleting documents

Using MongoDB with Python (PyMongo)

Usage

Run MongoDB command files using:

cat <file_name> | mongo


Example:

cat 0-list_databases | mongo

Author

Suleyman Hajizada

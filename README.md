---
title: "Flask App Documentation"
author: "Mouad Ait Khouya"
date: "01-31-2025`"
output: html_document
---

## Flask App Overview

This document provides an overview of the Flask app for managing student data. The app allows users to:

- View a list of students.
- Add new students.
- Update student information.
- Delete students.

The app uses a **MySQL database** to store student data and is built using the **Flask** web framework.

---

## App Structure

The Flask app consists of the following components:

1. **`app.py`**: The main Flask application file.
2. **`templates/`**: Contains HTML templates for rendering the UI.
3. **`static/`**: Contains CSS file. 

---

## Database Schema

The app uses a MySQL database with the following schema:

```sql
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Age INT,
    Grade VARCHAR(10),
    Email VARCHAR(100)
);

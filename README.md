# Overview

As a software engineer, I aimed to enhance my skills in cloud database integration by developing a ToDo application. The application allows users to manage their tasks efficiently by leveraging Firebase Realtime Database for data storage.

The ToDo application is a command-line interface program written in Python. It integrates with Firebase Realtime Database to store user tasks securely in the cloud. Users can sign up, sign in, add tasks, view tasks, and delete tasks seamlessly through the program.

The purpose of developing this software was to gain practical experience in integrating cloud databases into applications and to understand the workflow of user authentication and data management in cloud-based environments.

[Software Demo Video](https://www.youtube.com/watch?v=O8kfQX3pxUI)

# Cloud Database

The cloud database used in this project is Firebase Realtime Database, provided by Google Firebase. Firebase Realtime Database is a NoSQL cloud database that provides real-time synchronization and offline support for data.

The structure of the database consists of a single collection named "tasks," where each user's tasks are stored under their unique user ID as documents. Each task document contains the task content.

# Development Environment

- Firebase Realtime Database
- Python
- Firebase Admin SDK
- firebase-admin Python library

# Useful Websites

- [Firebase Console](https://console.firebase.google.com/): Used for managing Firebase projects and accessing Firebase Realtime Database.
- [Firebase Documentation](https://firebase.google.com/docs): Provided comprehensive documentation for integrating Firebase services into the application.

# Future Work

- Implement user authentication using email and password.
- Enhance error handling and input validation in the command-line interface.
- Implement additional features such as task prioritization and due dates.
- Develop a graphical user interface (GUI) for a more user-friendly experience.

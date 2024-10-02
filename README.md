# AirBnB Clone - Console View

Welcome to the AirBnB Clone repository! This project is the first step toward building a full web application that mimics the functionalities of the popular rental platform, AirBnB. In this stage, we focus on creating a command interpreter to manage our AirBnB objects.

## Table of Contents
- [Overview](#overview)
- [Project Description](#project-description)
- [Command Interpreter](#command-interpreter)
- [Using the Command Interpreter](#using-the-command-interpreter)
- [Examples](#examples)
- [Files and Directories](#files-and-directories)
- [Storage](#storage)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## Overview

The command interpreter serves as a foundational tool that will help us manage various AirBnB objects, including but not limited to Users, States, Cities, and Places. This project will lay the groundwork for future enhancements like HTML/CSS templating, database storage, API development, and front-end integration.

## Project Description

The goal of this project is to develop a command interpreter that provides a simplified interface for managing AirBnB objects. The interpreter will allow users to perform operations such as creating, retrieving, updating, and deleting objects. This functionality will be crucial for the overall AirBnB application, providing the necessary backend management before integrating other components like a web front-end and database storage.

## Command Interpreter

The command interpreter acts like a shell, enabling interaction with the AirBnB objects in a straightforward way. It provides various commands that users can execute to manipulate the objects.

### Starting the Command Interpreter

To start the command interpreter, simply run the following command in your terminal:

```bash
python console.py
```
Once started, you will be greeted with a prompt ((hbnb)) where you can enter commands.

## Using the Command Interpreter

### Basic Commands

Here are some of the basic commands you can use in the command interpreter:

- `create <class_name>`: Creates a new object of the specified class.
- `show <class_name> <id>`: Displays the string representation of an object based on the class name and ID.
- `destroy <class_name> <id>`: Deletes an object of the specified class.
- `all <class_name>`: Displays all objects of the specified class or all objects if no class is specified.
- `update <class_name> <id> <attribute_name> <attribute_value>`: Updates an object's attribute.

### Examples

1. **Creating a User**:
```bash
(hbnb) create User
```

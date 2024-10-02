# AirBnB Clone - Console

Welcome to the AirBnB Clone repository! This project is the first step toward building a full web application that mimics the functionalities of the popular rental platform, AirBnB. In this stage, we were focused on creating a command interpreter to manage our AirBnB objects.

## Table of Contents
- [Overview](#overview)
- [Description](#description)
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

## Description

The goal of this project is to develop a command interpreter that provides a simplified interface for managing AirBnB objects. The interpreter will allow users to perform operations such as creating, retrieving, updating, and deleting objects. This functionality will be crucial for the overall AirBnB application, providing the necessary backend management before integrating other components like a web front-end.

## Command Interpreter

The command interpreter acts like a shell, enabling interaction with the AirBnB objects in a straightforward way. It provides various commands that users can execute to manipulate the objects.

### Starting the Command Interpreter

To start the command interpreter, simply run the following command in your terminal:

```bash
python console.py
```
Once started, you will be greeted with a prompt ('(hbnb)') where you can enter commands.

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
This command will create a new User object and display its ID.

2. **Showing an Object**:
```bash
(hbnb) show User 1234-5678-9012
```
Replace '1234-5678-9012' with the actual ID of the User you created.

3. **Updating an Object**:
```bash
(hbnb) update User 1234-5678-9012 name "John Doe"
```
This command updates the 'name' attribute of the User object.

4. **Destroying an Object**:
```bash
(hbnb) destroy User 1234-5678-9012
```
This command deletes the User object with the specified ID.

5. **Listing All Objects**:
```bash
(hbnb) all
```
This command lists all objects created so far.

## Files and Directories

Here’s a breakdown of the project's structure:
```bash
airbnb_clone/ │ ├── console.py # Entry point for the command interpreter ├── models/ # Contains all classes used in the project │ ├── base_model.py # Base class for all models │ └── engine/ # Storage classes │ └── file_storage.py ├── tests/ # Unit tests for the project
```

### Models Directory

- Contains the class 'BaseModel', which all other classes representing various AirBnB objects inherit from: Amenity, City, Place, State, User, and Review.
- `BaseModel` includes common attributes like `id`, `created_at`, and `updated_at`, along with methods like `save()` and `to_json()`.

### Engine Directory

- Contains the class 'FileStorage' which houses all of the methods initially focusing on file storage.

## Storage

Persistency is crucial for any web application. This project will initially use file storage to ensure that objects created during one execution can be retrieved in the next.

### Why Separate Storage Management?

Separating storage management from the model allows for modularity and independence, making it easier to swap out storage methods without extensive code changes.

### JSON Serialization

The project will utilize JSON to serialize and deserialize object instances, ensuring compatibility across different programming languages and facilitating data sharing.

## Getting Started

To get started with the AirBnB Clone:

1. **Clone the Repository**:
```bash
git clone https://github.com/yourusername/airbnb_clone.git
cd airbnb_clone
```
2. **Run the Console**:
```bash
python console.py
```

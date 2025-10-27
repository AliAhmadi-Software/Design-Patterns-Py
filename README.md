# Design Patterns in Python

This repository contains Python implementations of various software design patterns. Design patterns are general, reusable solutions to common problems that arise during software design. They represent best practices that can be adapted to fit specific situations.

## Table of Contents

- [Introduction](#introduction)
- [Folder Structure](#folder-structure)
- [Patterns Implemented](#patterns-implemented)
  - [Creational Patterns](#creational-patterns)
  - [Structural Patterns](#structural-patterns)
  - [Behavioral Patterns](#behavioral-patterns)
- [Usage](#usage)

## Introduction

Software design patterns are proven solutions to recurring design problems encountered during software development. Understanding and implementing these patterns can significantly improve the maintainability, scalability, and readability of your code.

This repository aims to provide clear and concise implementations of these patterns in Python, serving as a valuable resource for developers looking to enhance their software design skills.

## Folder Structure

The repository is organized into three main directories, each corresponding to a category of design patterns:

- `01-Creational-Design-Patterns/`: Contains patterns that deal with object creation mechanisms.
- `02-Structural-Design-Patterns/`: Includes patterns that focus on the composition of classes and objects.
- `03-Behavioral-Design-Patterns/`: Features patterns that manage algorithms, relationships, and responsibilities among objects.

Each directory contains Python files that implement specific design patterns, along with example usage.

## Patterns Implemented

### Creational Patterns

- **Singleton**: Ensures a class has only one instance and provides a global point of access to it.
- **Factory Method**: Defines an interface for creating objects, but lets subclasses alter the type of objects that will be created.
- **Abstract Factory**: Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
- **Builder**: Allows the construction of a complex object step by step.
- **Prototype**: Specifies the kind of objects to create using a prototypical instance and creates new objects by copying this prototype.

### Structural Patterns

- **Adapter**: Allows incompatible interfaces to work together by providing a wrapper that translates calls.
- **Bridge**: Decouples an abstraction from its implementation so that the two can vary independently.
- **Composite**: Composes objects into tree structures to represent part-whole hierarchies.
- **Decorator**: Attaches additional responsibilities to an object dynamically.
- **Facade**: Provides a simplified interface to a complex subsystem.
- **Flyweight**: Reduces the cost of creating and manipulating a large number of similar objects.
- **Proxy**: Provides a surrogate or placeholder for another object to control access to it.

### Behavioral Patterns

- **Chain of Responsibility**: Passes a request along the chain of potential handlers until one handles it.
- **Command**: Encapsulates a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations.
- **Interpreter**: Implements an expression interface to interpret a sentence in a language.
- **Iterator**: Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
- **Mediator**: Defines an object that encapsulates how a set of objects interact.
- **Memento**: Captures and externalizes an object's internal state without violating encapsulation.
- **Observer**: Defines a dependency between objects so that when one object changes state, all its dependents are notified.
- **State**: Allows an object to alter its behavior when its internal state changes.
- **Strategy**: Defines a family of algorithms, encapsulates each one, and makes them interchangeable.
- **Template Method**: Defines the skeleton of an algorithm in the method, deferring some steps to subclasses.
- **Visitor**: Lets you define a new operation without changing the classes of the elements on which it operates.

## Usage

To explore and run the examples:

1. Clone the repository:

   ```bash
   git clone https://github.com/AliAhmadi-Software/Design-Patterns-Py.git
   cd Design-Patterns-Py
   cd 01-Creational-Design-Patterns
   python singleton.py
   ```
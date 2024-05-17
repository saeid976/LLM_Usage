# Real Estate Consultant LLM Microservice

Welcome to the Real Estate Consultant LLM Microservice! This project provides an API endpoint for extracting features of a house from user prompts using a large language model (LLM) tailored for real estate consultation. The microservice is built with FastAPI and deployed using Docker and Docker Compose for easy setup and scalability.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

The Real Estate Consultant LLM Microservice is designed to assist with real estate consultation by leveraging a large language model. The API endpoint allows users to input prompts related to houses, and the model will extract relevant features such as location, size, price, and amenities.

## Features

- **FastAPI**: Utilizes FastAPI for creating the API endpoint, providing high performance and easy integration.
- **Feature Extraction**: Extracts detailed features of a house from user prompts.
- **Dockerized**: Easily deployable using Docker and Docker Compose.
- **Scalable**: Designed to handle multiple requests efficiently.

## Installation

To get started with the Real Estate Consultant LLM Microservice, follow these steps:

### Prerequisites

- Docker
- Docker Compose

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/saeid976/LLM_Usage.git
    cd real-estate-consultant-llm
    ```

2. **Build and start the Docker containers**:
    ```bash
    docker-compose up --build
    ```

The FastAPI server will be up and running, typically on `http://localhost:8000`.

## Usage

Once the server is running, you can interact with the API using the following endpoint:

- **POST /extract-features**: Extracts features of a house based on the input prompt.

### Example Request

```bash
  "user_prompt": ""
}'

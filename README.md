# Machine learning model API project

API that returns the price prediction for a house or apartment in Belgium.

## Description

A machine learning model is used to predict real estate prices based on its characteristics.

The API contains:
- A route at `/` that accept:
    - `GET` request and return `"alive"` if the server is alive.
- A route at `/predict` that accept:
    - `POST` request that receives the data of a house in JSON format.
    - `GET` request returning a string to explain what the `POST` expect (data and format).

## Usage

This can be deployed on any web server and queried for Belgian real estate price prediction.

## Timing

5-day project (from 17 Oct 2022 to 21 Oct 2022)
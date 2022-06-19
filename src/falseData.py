from adapters.getImageAsBase64 import getImageAsBase64
from os import path

falseData = [
    {
        "id": 8,
        "name": "Jogging Babucha Negro",
        "price": 4999.99,
        "images": [getImageAsBase64(path.abspath("images/ropa8.jpg"))]
    },
    {
        "id": 1,
        "name": "Remera Negra",
        "price": 3000,
        "images": [getImageAsBase64(path.abspath("images/ropa1.jpg"))]
    },
    {
        "id": 5,
        "name": "Jean Mom",
        "price": 10000,
        "images": [getImageAsBase64(path.abspath("images/ropa5.jpg"))]
    },
    {
        "id": 6,
        "name": "Suéter Negro",
        "price": 7999.99,
        "images": [getImageAsBase64(path.abspath("images/ropa6.jpg"))]
    },
    {
        "id": 2,
        "name": "Buzo Negro con Capucha",
        "price": 8000,
        "images": [getImageAsBase64(path.abspath("images/ropa2.jpg"))]
    },
    {
        "id": 3,
        "name": "Chomba Oxford Polo",
        "price": 5999.99,
        "images": [getImageAsBase64(path.abspath("images/ropa3.jpg"))]
    },
    {
        "id": 4,
        "name": "Jean Kevingston",
        "price": 10000,
        "images": [getImageAsBase64(path.abspath("images/ropa4.jpg"))]
    }
]

from flask import Flask, render_template, jsonify, request, redirect
import pymongo.errors
from app import app, baseDatos, productos
from werkzeug.utils import secure_filename
import os
import pymongo


@app.router("/")
def inicio():
    try:
        listaProductos=productos.find()
        return  
from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Fonction pour créer une connexion à la base de données MySQL
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='db',  # Remplacez par votre hôte MySQL
            user='root',  # Remplacez par votre nom d'utilisateur MySQL
            password='rootpassword',  # Remplacez par votre mot de passe MySQL
            database='test_db'  # Remplacez par le nom de votre base de données
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Erreur lors de la connexion à MySQL: {e}")
        return None

# Route pour créer la table 'messages' si elle n'existe pas
@app.route('/init-db', methods=['GET'])
def init_db():
    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Connexion à la base de données échouée"}), 500

    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            content TEXT NOT NULL
        )
    """)
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"message": "Table 'messages' créée avec succès"}), 200

# Route pour récupérer les messages depuis la table 'messages'
@app.route('/', methods=['GET'])
def get_messages():
    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Connexion à la base de données échouée"}), 500

    cursor = connection.cursor()
    
    # Création de la table si elle n'existe pas encore
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            content TEXT NOT NULL
        )
    """)
    
    cursor.execute("SELECT * FROM messages")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()

    messages = [{"id": row[0], "content": row[1]} for row in rows]
    return jsonify(messages)

# Route pour ajouter un message à la table 'messages'
@app.route('/add-message', methods=['POST'])
def add_message():
    content = request.json.get('content')
    if not content:
        return jsonify({"error": "Le contenu du message est requis"}), 400

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Connexion à la base de données échouée"}), 500

    cursor = connection.cursor()
    cursor.execute("INSERT INTO messages (content) VALUES (%s)", (content,))
    connection.commit()
    cursor.close()
    connection.close()

    return jsonify({"message": "Message ajouté avec succès"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

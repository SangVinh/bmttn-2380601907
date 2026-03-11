from flask import Flask, request, jsonify

app = Flask(__name__)

def caesar_encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result


@app.route('/api/caesar/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    text = data.get("text")
    key = data.get("key")

    encrypted = caesar_encrypt(text, key)
    return jsonify({
        "encrypted_message": encrypted
    })


if __name__ == '__main__':
    app.run(debug=True)
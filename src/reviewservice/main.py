from flask import Flask, request, jsonify

app = Flask(__name__)
reviews = {}

@app.route("/reviews/<product_id>", methods=["GET"])
def get_reviews(product_id):
    return jsonify(reviews.get(product_id, []))

@app.route("/reviews/<product_id>", methods=["POST"])
def add_review(product_id):
    review = request.json
    reviews.setdefault(product_id, []).append(review)
    return {"status": "success"}, 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

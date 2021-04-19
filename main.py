from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://main:01012015@localhost/iot-test-db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Bra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_of_hooks = db.Column(db.Integer, unique=False)
    cups_size = db.Column(db.String(15), unique=False)

    def update(self, number_of_hooks, cups_size):
        self.number_of_hooks = number_of_hooks
        self.cups_size = cups_size


class BraSchema(ma.Schema):
    class Meta:
        fields = ('id', 'number_of_hooks', 'cups_size')


@app.route("/", methods=["GET"])
def get_bras():
    bras = Bra.query.all()
    return bras_schema.jsonify(bras)


@app.route("/<id>", methods=["GET"])
def get_bra(id):
    bra = Bra.query.get(id)
    if not bra:
        abort(404)
    return bra_schema.jsonify(bra)


@app.route("/", methods=["POST"])
def add_bra():
    fields = bra_schema.load(request.json)
    bra = Bra(**fields)
    db.session.add(bra)
    db.session.commit()
    return bra_schema.jsonify(bra)


@app.route("/<id>", methods=["DELETE"])
def delete_bear(id):
    bra = Bra.query.get(id)
    if not bra:
        abort(404)
    db.session.delete(bra)
    db.session.commit()
    return jsonify(success=True)


@app.route("/<id>", methods=["PUT"])
def update_bear(id):
    bra = Bra.query.get(id)
    if not bra:
        abort(404)
    fields = bra_schema.load(request.json)
    bra.update(**fields)
    # bra.number_of_hooks = request.json["number_of_hooks"]
    # bra.cups_size = request.json["cups_size"]
    db.session.commit()
    return jsonify(success=True)


if __name__ == '__main__':
    bra_schema = BraSchema()
    bras_schema = BraSchema(many=True)
    app.run(debug=True)

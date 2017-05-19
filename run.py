from kmujournal import app

from flask import request, jsonify
from kmujournal import manager

@app.route("/")
def yellow_keyboard2():
    message, code = manager.save_userkey(request)
    return jsonify(message), code

@app.route("/keyboard", methods=["GET"])
def yellow_keyboard():
    message, code = manager.first_process()
    return jsonify(message), code

@app.route("/message", methods=["POST"])
def yellow_message():
    # msg = request.json['content']
    message, code = manager.af_clk_procees(request)
    return jsonify(message), code


@app.route("/friend", methods=["POST"])
def yellow_friend_add():
    code = manager.add_friend(request)
    return jsonify(code)


@app.route("/friend/<key>", methods=["DELETE"])
def yellow_friend_block(key):
    code = manager.delete_friend(key)
    return jsonify(code)


@app.route("/chat_room/<key>", methods=["DELETE"])
def yellow_exit(key):
    code = manager.delete_friend(key)
    return jsonify(code)


if __name__ == '__main__':
    app.run(debug=True)
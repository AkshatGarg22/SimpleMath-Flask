from flask import Blueprint

router = Blueprint("router", __name__)

@router.route("/hello")
def check():
    return "Congratulations! Your app works. :)"
@router.route("/hello")
def hello():
    return "it does!!!!. :)"

@router.route("/add", methods=["POST"])
def add():
    # Add logic here
    return

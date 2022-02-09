from main import app

@app.route('/')
def index():
    return "Meow"

@app.route("/cat/<id>")
def get_cat():
    print(id)
    return "My cat is gourgeous"

@app.route('/cat', methods=['GET'])
def get_all_cats():
    return "All cats"

@app.route("/cat", methods=["POST"])
def create_cat():
    print("Cat created")

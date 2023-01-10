# Put your app in here.

from flask import Flask, request

app = Flask(__name__)

POSTS = {
    add: def add(a, b):
        return a + b
    sub: def sub(a, b):
        return a - b 
    mult: def mult(a, b):
        return a * b
    div: def div(a, b):
        return a / b
}       

@app.rout('/posts/<id>')
def do_maths():
    """
    show form for getting a and b values 
    """
    return """
    <h1>Add Values</h1>
    <form method=""POST">
    <input type = 'int' placeholder='A value' name="a">
    <input type = 'int' placeholder='b value' name="b">
    <button>Submit</button>
    </form>
    """
    
    
    
    
def find_post(id):
    post = POSTS.get(id, "post not found")
    return         
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:47:19 2020

@author: sxw17
"""

# Harvard’s CS50 Week 8 - Python 
# https://www.youtube.com/watch?v=5aP9Bl9hcqI&t=7330s


## Intro to Python

print("hello, world")


def main():
    print("hello, world")

if __name__ == "__main__":
    main()
    
while True:
    print("hello, world")
    

for i in range(50):
    print("hello, world")
    
    
i = 0
x  = 100 
y = 10 

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
    
    
#########################################
    
## First Programs
import cs50

s = cs50.get_string()
print("hello, {}".format(s))

s = input("name: ")
print("hello, {}".format(s))


import cs50

i = cs50.get_int()
print("hello, {}".format(i))


print("{:.55f}".format(1 / 10))


import cs50

# prompt user for x
print("x is ", end="")
x = cs50.get_int()

# prompt user for y
print("y is ", end="")
y = cs50.get_int()

# perform calculations for user
print("{} plus {} is {}".format(x, y, x + y))
print("{} minus {} is {}".format(x, y, x - y))
print("{} times {} is {}".format(x, y, x * y))
print("{} divided by {} is {}".format(x, y, x / y))
print("{} divided by {} (and floored) is {}".format(x, y, x // y))
print("remainder of {} divided by {} is {}".format(x, y, x % y))


import cs50

f = cs50.get_float()
c = 5.0 / 9.0 * (f - 32.0)
print("{:.1f}".format(c))


#########################################
## Logical Programs
import cs50

c = cs50.get_char()
if c == "Y" or c == "y":
    print("yes")
elif c == "N" or c == "n":
    print("no")
else:
    print("error")
    
"""
#include <stdio.h>

int get_positive_int();

int main(void)
{
    int i = get_positive_int();
    printf("%i is a positive integer\n", i);
}

int get_positive_int(void)
{
    int n;
    do
    {
        printf("n is ");
        n = get_int();
    }
    while (n < 1);
    return n;
"""


import cs50

def main():
    i = get_positive_int()
    print("{} is a positive integer".format(i))

def get_positive_int():
    while True:
        print("n is ", end="")
        n = cs50.get_int()
        if n > 0:
            break
    return n

if __name__ == "__main__":
    main()
    
    
print("cough")
print("cough")
print("cough")


for i in range(3):
    print("cough")
    
    
def main():
    for i in range(3):
        cough()

def cough():
    print("cough")

if __name__ == "__main__":
    main()
    
    
def main():
    cough(3)

def cough(n):
    for i in range(n):
        print("cough")

if __name__ == "__main__":
    main()
    
    
def main():
    cough(3)
    sneeze(3)

def cough(n):
    say("cough", n)

def sneeze(n):
    say("achoo", n)

def say(word, n):
    for i in range(n):
        print(word)

if __name__ == "__main__":
    main()
    
   
    
#########################################
# More Complex Programs
"""
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = get_string();
    int n = 0;
    while (s[n] != '\0')
    {
        n++;
    }
    printf("%i\n", n);
}

"""

import cs50

s = cs50.get_string()
print(len(s))
    

for i in range(65, 65 + 26):
    print("{} is {}".format(chr(i), i))
    
import sys

if len(sys.argv) == 2:
    print("hello, {}".format(sys.argv[1]))
else:
    print("hello, world")


import sys

for i in range(len(sys.argv)):
    print(sys.argv[i])
    
    
import sys

for s in sys.argv:
    for c in s:
        print(c)
    print()
    
    
import cs50
import sys

if len(sys.argv) != 2:
    print("missing command-line argument")
    exit(1)

print("hello, {}".format(sys.argv[1]))
exit(0)    
    

import cs50
import sys

print("s: ", end="")
s = cs50.get_string()

print("t: ", end="")
t = cs50.get_string()

if s != None and t != None:
    if s == t:
        print("same")
    else:
        print("different")
        
        
import cs50
import sys

print("s: ", end="")
s = cs50.get_string()

if s == None:
    exit(1)

t = s.capitalize()

print("s: {}".format(s))
print("t: {}".format(t))

exit(0)

######################################### 

def main():
    x = 1
    y = 2

    print("x is {}".format(x))
    print("y is {}".format(y))
    print("Swapping...")
    swap(x, y)
    print("Swapped.")
    print("x is {}".format(x))
    print("y is {}".format(y))

def swap(a, b):
    tmp = a
    a = b
    b = tmp

if __name__ == "__main__":
    main()


x = 1
y = 2

print("x is {}".format(x))
print("y is {}".format(y))
print("Swapping...")
x, y = y, x
print("Swapped.")
print("x is {}".format(x))
print("y is {}".format(y))


#########################################  
    
    
import cs50
from student import Student

students = []
for i in range(3):

    print("name: ", end="")
    name = cs50.get_string()

    print("dorm: ", end="")
    dorm = cs50.get_string()

    students.append(Student(name, dorm))

for student in students:
    print("{} is in {}.".format(student.name, student.dorm))
    
class Student:
    def __init__(self, name, dorm):
        self.name = name
        self.dorm = dorm    
    

######################################### 
        
import cs50
import csv
from student import Student

students = []
for i in range(3):

    print("name: ", end="")
    name = cs50.get_string()

    print("dorm: ", end="")
    dorm = cs50.get_string()

    students.append(Student(name, dorm))

file = open("students.csv", "w")
writer = csv.writer(file)
for student in students:
    writer.writerow((student.name, student.dorm))
file.close()



        
#########################################     
class Dictionary:

    def __init__(self):
        self.words = set()

    def check(self, word):
        return word.lower() in self.words

    def load(self, dictionary):
        file = open(dictionary, "r")
        for line in file:
            self.words.add(line.rstrip("\n"))
        file.close()
        return True

    def size(self):
        return len(self.words)

    def unload(self):
        return True
    
    
######################################### 
# Web Servers       
from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # send response status code
        self.send_response(200)

        # send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # determine message to send to client
        if self.path == "/":
            message = "Hello, world!"
        else:
            name = self.path[1:]
            message = "Hello, {}!".format(name)

        # write message
        self.wfile.write(bytes(message, "utf8"))
        return

#########################################
    
def run():
  print('starting server...')

  # set up server
  port = 8080
  server_address = ('127.0.0.1', port)
  httpd = HTTPServer(server_address, HTTPServer_RequestHandler)

  # run server
  print('running server on port {}...'.format(port))
  httpd.serve_forever()


run()

#########################################

from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if request.form["name"] == "" or request.form["dorm"] == "":
        return render_template("failure.html")
    return render_template("success.html")
        
        
        
from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "shhh"

@app.route("/", methods=["GET", "POST"])
def store():
    if request.method == "POST":
        for item in ["foo", "bar", "baz"]:
            if item not in session:
                session[item] = int(request.form[item])
            else:
                session[item] += int(request.form[item])
        return redirect(url_for("cart"))
    return render_template("store.html")

@app.route("/cart")
def cart():
    cart = []
    for item in ["foo", "bar", "baz"]:
        cart.append({"name":item.capitalize(), "quantity":session[item]})
    return render_template("cart.html", cart=cart)

      
    
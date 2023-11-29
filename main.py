from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/html', methods=['GET'])
def get_html_quiz():
    quiz_data = [
  {
    "title": "Why We Use <br> Element?",
    "answer_1": "To Make Text Bold",
    "answer_2": "To Make Text Italic",
    "answer_3": "To Add Breakline",
    "answer_4": "To Create Horizontal Line",
    "right_answer": "To Add Breakline"
  },
  {
    "title": "Is <img> Element Has Attribute href?",
    "answer_1": "Yes",
    "answer_2": "No Its For Anchor Tag",
    "answer_3": "All Elements Has This Attribute",
    "answer_4": "Answer 1 And 3 Are Right",
    "right_answer": "No Its For Anchor Tag"
  },
  {
    "title": "How Can We Make Element Text Bold?",
    "answer_1": "Putting It Inside <b> Tag",
    "answer_2": "Putting It Inside <strong> Tag",
    "answer_3": "Customizing It With Font-Weight Property In CSS",
    "answer_4": "All Answers Are Correct",
    "right_answer": "All Answers Are Correct"
  },
  {
    "title": "What Is The Right Hierarchy For Creating Part Of Page?",
    "answer_1": "<h2> Then <p> Then <h1> Then <p> Then <h3> Then <p> Then <img>",
    "answer_2": "<h1> Then <p> Then <h3> Then <p> Then <h2> Then <p> Then <img>",
    "answer_3": "<h2> Then <p> Then <h3> Then <p> Then <h1> Then <p> Then <img>",
    "answer_4": "All Solutions Are Wrong",
    "right_answer": "All Solutions Are Wrong"
  },
  {
    "title": "How Can We Include External Page Inside Our HTML Page?",
    "answer_1": "By Using Include in HTML",
    "answer_2": "By Using Load In HTML",
    "answer_3": "By Using iFrame Tag",
    "answer_4": "All Solutions Is Wrong",
    "right_answer": "By Using iFrame Tag"
  },
  {
    "title": "What Is The Tag That Not Exists in HTML?",
    "answer_1": "<object>",
    "answer_2": "<basefont>",
    "answer_3": "<abbr>",
    "answer_4": "All Tags Exist in HTML",
    "right_answer": "All Tags Exist in HTML"
  },
  {
    "title": "How We Specify Document Type Of HTML5 Page?",
    "answer_1": "<DOCTYPE html>",
    "answer_2": "<DOCTYPE html5>",
    "answer_3": "<!DOCTYPE html5>",
    "answer_4": "<!DOCTYPE html>",
    "right_answer": "<!DOCTYPE html>"
  },
  {
    "title": "What Is The Element Thats Not Exists in HTML5 Semantics?",
    "answer_1": "<article>",
    "answer_2": "<section>",
    "answer_3": "<blockquote>",
    "answer_4": "<aside>",
    "right_answer": "<blockquote>"
  },
  {
    "title": "In HTML Can We Use This Way To Add Attributes?",
    "answer_1": "<div class='class-name'>",
    "answer_2": "<div class=class-name>",
    "answer_3": "<div class=\"class-name\">",
    "answer_4": "All Are Correct",
    "right_answer": "All Are Correct"
  },
  {
    "title": "What does HTML stand for?",
    "answer_1": "High Trace Mahine Learning",
    "answer_2": "Home Tool Markup Language",
    "answer_3": "Hyper Text Markup Language",
    "answer_4": "Hyperlinks and Text Markup Language",
    "right_answer": "Hyper Text Markup Language"
  },
  {
    "title": "Choose the correct HTML element for the largest heading:",
    "answer_1": "<h2>",
    "answer_2": "<head>",
    "answer_3": "<h6>",
    "answer_4": "<heading>",
    "right_answer": "<h2>"
  },
  {
    "title": "Choose the correct HTML element to define important text?",
    "answer_1": "<strong>",
    "answer_2": "<i>",
    "answer_3": "<b>",
    "answer_4": "<important>",
    "right_answer": "<strong>"
  },
  {
    "title": "What is the correct HTML for making a checkbox?",
    "answer_1": "<checkbox>",
    "answer_2": "<input type='checkbox'>",
    "answer_3": "<input type='check'>",
    "answer_4": "<check>",
    "right_answer": "<input type='checkbox'>"
  },
  {
    "title": "What is the correct HTML for inserting an image?",
    "answer_1": "<img src='image.gif' alt='MyImage'>",
    "answer_2": "<image src='image.gif' alt='MyImage'>",
    "answer_3": "<img href='image.gif' alt='MyImage'>",
    "answer_4": "<img alt='MyImage'>image.gif</img>",
    "right_answer": " <img src='image.gif' alt='MyImage'>"
  },
  {
    "title": "In HTML, which attribute is used to specify that an input field must be filled out?",
    "answer_1": "placeholder",
    "answer_2": "required",
    "answer_3": "validate",
    "answer_4": "formvalidate",
    "right_answer": "required"
  }
]
    return jsonify(quiz_data)

@app.route('/python', methods=['GET'])
def get_python_quiz():
    quiz_data = [
  {
    "title": "What is the latest stable version of Python?",
    "answer_1": "Python 3.7",
    "answer_2": "Python 3.8",
    "answer_3": "Python 3.9",
    "answer_4": "Python 3.10",
    "right_answer": "Python 3.10"
  },
  {
    "title": "Which keyword is used to define a function in Python?",
    "answer_1": "def",
    "answer_2": "function",
    "answer_3": "define",
    "answer_4": "funct",
    "right_answer": "def"
  },
  {
    "title": "What does the 'self' keyword represent in a class?",
    "answer_1": "Instance",
    "answer_2": "Class",
    "answer_3": "Method",
    "answer_4": "Object",
    "right_answer": "Instance"
  },
  {
    "title": "How do you open a file in Python for reading?",
    "answer_1": "open_file('filename', 'r')",
    "answer_2": "file_open('filename', 'read')",
    "answer_3": "open('filename', 'read')",
    "answer_4": "open('filename', 'r')",
    "right_answer": "open('filename', 'r')"
  },
  {
    "title": "What is the purpose of the 'if __name__ == '__main__':' statement in Python?",
    "answer_1": "Defines a class",
    "answer_2": "Checks if a function is defined",
    "answer_3": "Executes code only if the script is run as the main program",
    "answer_4": "Creates an instance of a class",
    "right_answer": "Executes code only if the script is run as the main program"
  },
  {
    "title": "Which module is used for regular expressions in Python?",
    "answer_1": "regex",
    "answer_2": "re",
    "answer_3": "regexpy",
    "answer_4": "string",
    "right_answer": "re"
  },
  {
    "title": "What is the output of 'print(3 * 'abc')' in Python?",
    "answer_1": "9",
    "answer_2": "'abcabcabc'",
    "answer_3": "TypeError",
    "answer_4": "'abc abc abc'",
    "right_answer": "'abcabcabc'"
  },
  {
    "title": "How do you comment multiple lines in Python?",
    "answer_1": "# This is a comment",
    "answer_2": "/* This is a comment */",
    "answer_3": "''' This is a comment '''",
    "answer_4": "// This is a comment",
    "right_answer": "''' This is a comment '''"
  },
  {
    "title": "Which of the following is not a valid data type in Python?",
    "answer_1": "int",
    "answer_2": "char",
    "answer_3": "float",
    "answer_4": "str",
    "right_answer": "char"
  },
  {
    "title": "How can you convert a string to uppercase in Python?",
    "answer_1": "str.toUpper()",
    "answer_2": "string.upper()",
    "answer_3": "str.uppercase()",
    "answer_4": "string.toUpper()",
    "right_answer": "string.upper()"
  },
  {
    "title": "What is the purpose of the 'pass' statement in Python?",
    "answer_1": "Exits the program",
    "answer_2": "Skips the current block of code",
    "answer_3": "Defines a function",
    "answer_4": "Prints a message",
    "right_answer": "Skips the current block of code"
  },
  {
    "title": "Which module is used for working with dates and times in Python?",
    "answer_1": "datetime",
    "answer_2": "time",
    "answer_3": "date",
    "answer_4": "calendar",
    "right_answer": "datetime"
  },
  {
    "title": "What is the result of '10 / 2' in Python?",
    "answer_1": "5.0",
    "answer_2": "5",
    "answer_3": "2.0",
    "answer_4": "2",
    "right_answer": "5.0"
  },
  {
    "title": "How do you import a module named 'mymodule' in Python?",
    "answer_1": "import mymodule",
    "answer_2": "include mymodule",
    "answer_3": "import module(mymodule)",
    "answer_4": "require mymodule",
    "right_answer": "import mymodule"
  },
  {
    "title": "Which statement is used for exiting a loop prematurely in Python?",
    "answer_1": "break",
    "answer_2": "exit",
    "answer_3": "stop",
    "answer_4": "end",
    "right_answer": "break"
  }
]
    return jsonify(quiz_data)

@app.route('/lol', methods=['GET'])
def get_lol_quiz():
    quiz_data = [
  {
    "title": "When was the online game League of Legends released?",
    "answer_1": "It was released at 2010",
    "answer_2": "It was released at 2011",
    "answer_3": "It was released at 2009",
    "answer_4": "It was released at 2012",
    "right_answer": "It was released at 2009"
  },
  {
    "title": "How many lanes are there in the Summoner's Rift map of the game League of Legends?",
    "answer_1": "The are Two lanes",
    "answer_2": "The are Four lanes",
    "answer_3": "The are Three lanes",
    "answer_4": "The Is Only One lane",
    "right_answer": "The are Three lanes"
  },
  {
    "title": "Which League of Legends character leads the Winter's Claw tribe?",
    "answer_1": "Lissandra",
    "answer_2": "Sejuani",
    "answer_3": "Volibear",
    "answer_4": "Sayls",
    "right_answer": "Sejuani"
  },
  {
    "title": "Which League of Legends champion helps Caitlyn fight crime?",
    "answer_1": "Jayce",
    "answer_2": "Viktor",
    "answer_3": "Vi",
    "answer_4": "Jinx",
    "right_answer": "Vi"
  },
  {
    "title": "Who is the champion Tryndamere married to in League of Legends?",
    "answer_1": "Fiora",
    "answer_2": "Ashe",
    "answer_3": "Illaoi",
    "answer_4": "Katarina",
    "right_answer": "Ashe"
  },
  {
    "title": "How many champions in League of Legneds?",
    "answer_1": "There are 162 champions",
    "answer_2": "There are 141 champions",
    "answer_3": "There are 155 champions",
    "answer_4": "There are 149 champions",
    "right_answer": "There are 162 champions"
  },
  {
    "title": "Which League of Legends champion does not come from the Void?",
    "answer_1": "Cho'Gath",
    "answer_2": "Kha'Zix",
    "answer_3": "Rek'sai ",
    "answer_4": "Karthus",
    "right_answer": "Karthus"
  },
  {
    "title": "Which League of Legends character killed Lucian's wife Senna?",
    "answer_1": "Hecarim",
    "answer_2": "Mordekaiser",
    "answer_3": "Viego",
    "answer_4": "Thresh",
    "right_answer": "Thresh"
  },
  {
    "title": "In the Popular League of Legends Serie 'Arcane' what was Vi's younger sister's first name?",
    "answer_1": "Jinx",
    "answer_2": "Powder",
    "answer_3": "Annie",
    "answer_4": "Lulu",
    "right_answer": "Powder"
  },
  {
    "title": "Which Champ Makes A Sexy Voice When Dying?",
    "answer_1": "Janna",
    "answer_2": "Ahri",
    "answer_3": "Evelynn",
    "answer_4": "Lillia",
    "right_answer": "Ahri"
  },
  {
    "title": "When Does The Baron Nashor Swpans?",
    "answer_1": "It spawns at minute 18",
    "answer_2": "It spawns at minute 19",
    "answer_3": "It spawns at minute 20",
    "answer_4": "It spawns at minute 21",
    "right_answer": "It spawns at minute 20"
  },
  {
    "title": "How many rift herald can spwan?",
    "answer_1": "Exactly 4 Rift herald",
    "answer_2": "Exactly 1 Rift herald",
    "answer_3": "Exactly 2 Rift herald",
    "answer_4": "Exactly 3 Rift herald",
    "right_answer": "Exactly 2 Rift herald"
  },
  {
    "title": "Which of these Demacian champs landed from the sky?",
    "answer_1": "Lux",
    "answer_2": "Galio",
    "answer_3": "Garen",
    "answer_4": "Jarvan IV",
    "right_answer": "Galio"
  },
  {
    "title": "Which of these champs has this voice line “Shurima! Your emperor has returned!”?",
    "answer_1": "Brand",
    "answer_2": "Graves",
    "answer_3": "Azir",
    "answer_4": "Draven",
    "right_answer": "Azir"
  },
  {
    "title": "How many ultimate  skins exists in League of Legends",
    "answer_1": "League has 4 ultimate skins",
    "answer_2": "League has 5 ultimate skins",
    "answer_3": "League has 6 ultimate skins",
    "answer_4": "League has 3 ultimate skins",
    "right_answer": "League has 6 ultimate skins"
  }
]
    return jsonify(quiz_data)

if __name__ == '__main__':
    app.run(debug=True)

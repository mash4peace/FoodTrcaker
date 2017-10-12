from flask import Flask, render_template, request
import sqlite3
conn = sqlite3.connect("food_tracker.db")
conn.row_factory = sqlite3.Row

app = Flask(__name__)
c = conn.cursor()
"""
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

"""
c.execute("Create Table IF NOT EXISTS log_date(id Integer PRIMARY KEY AUTOINCREMENT ,"
          "entry_date date NOT NULL )")

c.execute("Create Table IF NOT EXISTS food(id Integer PRIMARY KEY AUTOINCREMENT ,name text not NULL ,"
          "carbohydarates Integer NOT NULL , fat Integer NOT NULL,calories Integer NOT NULL )")

c.execute("Create Table IF NOT EXISTS food_date(food_id Integer NOT NULL ,"
          "log_date_id Integer  NOT NULL, PRIMARY KEY (food_id, log_date_id))")


print("Database is succesfully created as well three tables were created !!")

@app.route('/')
def index():
    #c.close()
    return render_template("home.html")
@app.route("/view")
def view():
    #c.close()
    return render_template("day.html")

@app.route("/food", methods= ['GET', 'POST'])
def food():
    if request.method == 'POST':

        # food-name protein  carbohydrates fat
        food_name = str(request.form["food-name"])
        protein = int(request.form["protein"])
        carbonhyrdrates = int(request.form["carbohydrates"]) #
        fat =int(request.form["fat"])
        calories = protein * 4 + carbonhyrdrates *4 + fat*9
        #print(calories)
        c.execute("Insert into food (food_name, protein, carbonhyrdrates, fat, calories) VALUES (?, ?, ?,?, ?)")
        #conn.commit()
        """
        return '<h1> Name: {} Protein : {} Carbs :{} Fat {}</h1>'.format(request.form['food-name'],
                                                                         request.form['protein'], request.form['carbohydrates'], request.form['fat'])
        """

    return render_template("add_food.html")


if __name__ == '__main__':
    app.run(debug=True)
    c.close()

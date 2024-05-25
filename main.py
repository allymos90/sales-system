# importing the flask class
from flask import Flask ,render_template,request,redirect,url_for,flash,session

from database import get_data,insert_products,insert_sales,profit_product,profit_day,sales_per_product, sales_per_day,register_user,check_email,compare_email_pass

 

# create a flask instance
app=Flask(__name__)
app.secret_key = "Ali Moha"

# route
@app.route("/")
def hello():
    return render_template("index.html")
  
# @app.route("/login",methods=["POST","GET"])
# def login():
    
#     mail=request.form['email']
#     passw=request.form['password']
#     print(login)
#     return render_template("login.html")
@app.route("/login", methods=["POST", "GET"])
def login():
    # get form data
    if request.method == "POST":
 
        email = request.form['email']
        password = request.form['password']

        v_email=check_email(email)
        if v_email==None:
            flash("email does not exist,register ")
            return redirect(url_for("register"))
        else:
            ch_pass=compare_email_pass(email,password)
            if len(ch_pass)<1:
                flash("invalid email or password")
            else:
                session["email"]=email

                flash("login successfully")
                return redirect(url_for("dashboard"))

 
    return render_template("login.html")
# @app.route("/login")
# def login():
    

#     return redirect(url_for('login'))


@app.route("/register" , methods=["GET", "POST"]  )
def register():


# get form data
    if request.method == "POST":

        full_name = request.form['full name']
        e_mail = request.form['email']
        password = request.form['password']
        # insert to db
        # check email
        c_email=check_email(e_mail)

        if c_email==None:

            user1=(full_name, e_mail, password )
            register_user(user1)
            flash("registered successfully")    
            return redirect(url_for("login"))
        else:
            flash("email already exist use a different email or login")

    return render_template("register.html")
    

    

@app.route("/product")
 
def product ():
    if "email" not in session:
        flash("login to access this page")
        return redirect(url_for("login"))

    products=get_data("products")
   
    return render_template("product.html",prods=products)
# add products
@app.route("/add_products",methods=["POST","GET"])
def add_prod():
    # get form data

    p_name=request.form ['product_name']
    b_price=request.form['buying_price']
    s_price=request.form['selling_price']
    s_quantity=request.form['stock_quanity']

# insert to db
    Prod_one=(p_name,b_price,s_price,s_quantity)

    insert_products(Prod_one)

    return redirect(url_for("product"))


@app.route("/sales")
 
def sales ():
    if "email" not in session:
        flash("login to access this page")
        return redirect(url_for("login"))
    # fetch sales
    sales=get_data("sales") 
    # dislpay the name
    products=get_data("products")
    
    return  render_template("sales.html",sales=sales,products=products)

# Create route for sales
@app.route("/make_sales" ,methods=["POST","GET"])
def make_sale():

    # get form data
    pid=request.form['pid']
    quantity=request.form['quantity']

#   make sales
    new_sale=(pid,quantity)
    insert_sales(new_sale)
    return redirect(url_for("sales"))



@app.route("/dashboard")
 
def dashboard():
    if "email" not in session:
        flash("login to access this page")
        return redirect(url_for("login"))
    pr_profit=profit_product()
    
    p_name=[]
    p_profit=[]
     
    for i in pr_profit:
        p_name.append(i[0])
        p_profit.append(float(i[1]))


        day_profit=profit_day()
        print(day_profit)


        dates=[]
        date_profit=[]

        for i in day_profit:
            dates.append(str(i[0]))
            date_profit.append(float(i[1]))

    sales_s=sales_per_product()   
    pr_name=[]   
    T_sales=[]
    for i in sales_s:
        pr_name.append(i[0])
        T_sales.append(float(i[1]))

        total_profit=sales_per_day()
        print(total_profit)


        dates=[]
        date_profit=[]
        for i in sales_s:
            dates.append(str(i[0]))
            date_profit.append(float(i[1]))
    return render_template("dashboard.html", 
                            p_name=p_name, 
                            p_profit=p_profit, 
                            dates=dates, 
                            date_profit=date_profit,
                            pr_name=pr_name,
                            T_sales=T_sales,
                            )

@app.route("/logout")

def logout():
    # remove the email from the session if it's there
    session.pop('email',None)
    flash("you are logged out ,log in")
    return redirect(url_for('login'))









      
    









    
    return  render_template("dashboard.html",p_name=p_name,p_profit=p_profit,dates=dates,date_profit=date_profit)



app.run(debug=True)



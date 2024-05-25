import psycopg2
conn=psycopg2.connect(
    user="postgres",
    dbname="myduka",
    password="198466",
    port=5432,
    host="localhost",

)

cur=conn.cursor()









# def get_products():

#     curr.execute("SELECT * FROM products;")
#     prods=curr.fetchall()
#     for i in prods:
#     print(i)

# get_products  

# def get_sales():

#     curr.execute("SELECT * FROM sales;")
#     sales=curr.fetchall()
#     for i in sales:

#     print(i)

# get_sales 

# get any data from database
def get_data(table_name):
    
    cur.execute(f"select * from {table_name}")
    data=cur.fetchall()

    return data

x=get_data("products")



# print(x)
        


# get_data('sales')
# get_data('products')


# # insert data




def insert_products(values):
    insert="insert into products(name,buying_price,selling_price,stock_quantity)\
    values(%s,%s,%s,%s);"
    cur.execute(insert,values)
    conn.commit()


# product_values=("tilapia",200,500,8)
# insert_products(product_values)
# get_data('sales')
# get_data('products')


# # insert sales
def insert_sales(values):
    insert=" insert into sales (pid,quantity,created_at)values(%s,%s,now()) "
    cur.execute(insert,values)
    conn.commit()



# def sales_date():
#     query="      "
#     cur.execute(query)
#     data=cur.fetchall()
#     print(data)

# Add these functions to your database.py file


def sales_per_product():
    query = " SELECT products.name as product_name, SUM(quantity) as total_sales FROM products  JOIN sales ON products.id = sales.pid  GROUP BY products.name  "
    cur.execute(query)
    data = cur.fetchall()
    print(data)
   
    return data
sales_per_product()

def sales_per_day():
    query = "SELECT DATE(sales.created_at) AS sales_date, SUM((products.selling_price - products.buying_price) * sales.quantity) AS total_profit FROM products JOIN sales ON sales.pid = products.id GROUP BY sales_date"
    cur.execute(query)
    data = cur.fetchall()
    print(data)
  
    return data
sales_per_day()


def profit_product():
    query = "SELECT    NAME,      SUM((SELLING_PRICE-BUYING_PRICE)*QUANTITY) AS PROFIT FROM PRODUCTS JOIN SALES ON PRODUCTS.ID=SALES.PID GROUP BY NAME"

    cur.execute(query)
    data=cur.fetchall()
    return(data)

def profit_day():
    query=" select date(sales.created_at) as sales_date,sum((selling_price-buying_price)*quantity)as profits from products join sales on sales.pid=products.id group by sales_date order by sales_date asc "
    cur.execute(query)
    data=cur.fetchall()
    # return(data)
    return(data)


# get data
def register_user(values):
    insert=" insert into users (full_name, email, password)values(%s,%s,%s) "
    cur.execute(insert,values)
    conn.commit()


def check_email(email):
    query='select * from users where email=%s'
    cur.execute(query,(email,))
    data=cur.fetchone()
    return data

def compare_email_pass(email,password):
    query='select * from users where email=%s and password=%s'
    cur.execute(query, (email, password))
    data=cur.fetchall()
    return data


import streamlit as st
import pandas as pd
import mysql.connector

mydb=mysql.connector.connect(

    host='localhost',
    user='root',
    database='bookstore2'

)

cur=mydb.cursor()
def sql_excecutor(raw_code):
    cur.execute(raw_code)
    data=cur.fetchall()
    return data



def create():
    # col1,col2=st.columns(2)
    # with col1:
    order_id= st.text_input("order_id:")
    order_date = st.text_input("order_date:")
    customer_id=st.text_input("customer_id:")
    if st.button("Add orders"):
        cur.execute('INSERT INTO orders(order_id, order_date, customer_id) VALUES (%s,%s,%s)',(order_id, order_date, customer_id))
        mydb.commit()
        st.success("Successfully added orders: {}".format(order_date))



def View():
    query_result=sql_excecutor("select * from orders")
    query_df=pd.DataFrame(query_result)
    st.dataframe(query_df)




def view_only_order_dates():
    cur.execute('select order_id from orders')
    data = cur.fetchall()
    return data

def get_orders(order_id):
    cur.execute('SELECT * FROM orders WHERE order_id="{}"'.format(order_id))
    data = cur.fetchall()
    return data








def Edit():
    list_of_orders=[i[0] for i in view_only_order_dates()]
    selected_order=st.selectbox("orders to Edit",list_of_orders)
    selected_result=get_orders(selected_order)
    if selected_result:
        order_id = selected_result[0][0]
        order_date = selected_result[0][1]
        # City = selected_result[0][2]
        customer_id = selected_result[0][2]
        # PhoneNum = selected_result[0][4]
        # Manager=selected_result[0][5]


        # col1,col2=st.columns(2)
        # with col1:
        new_order_id= st.text_input("order_id:")
        new_order_date = st.text_input("order_date:")
        # with col2:
        # new_City=st.selectbox("City", ["Bangalore", "Chennai", "Mumbai"])
        new_customer_id=st.text_input("customer_id:")
        # new_PhoneNum=st.text_input("Phone_number")
        # new_Manager=st.text_input("Manager_Name")
        if st.button("Update orders"):
                cur.execute("UPDATE orders SET order_id=%s, order_date=%s, customer_id=%s WHERE order_id=%s and order_date=%s and customer_id=%s", (new_order_id, new_order_date, new_customer_id, order_id, order_date, customer_id))
                mydb.commit()
                st.success("Successfully updated:: {} to ::{}".format(order_date, new_order_date))



def Remove():
    list_of_orders=[i[0] for i in view_only_order_dates()]
    selected_order=st.selectbox("order to delete",list_of_orders)
    # selected_result=get_orderss(selected_orderss)
    st.warning("Do you want to delete ::{}".format(selected_order))
    if st.button("Delete order"):
        cur.execute('DELETE FROM orders WHERE order_id="{}"'.format(selected_order))
        mydb.commit()
        st.success("order has been deleted successfully")

def orders_customer():
    query_result=sql_excecutor("select * from orders, customer where orders.customer_id=customer.customer_id")
    query_df=pd.DataFrame(query_result)
    st.dataframe(query_df)


# def book_orderss_orderss():
#     query_result=sql_excecutor("select * from book_orderss,orderss where book_orderss.customer_id=orderss.customer_id")
#     query_df=pd.DataFrame(query_result)
#     st.dataframe(query_df)




def orders():
    st.title("orders")
    menu=["Add", "View_all", "Edit", "Remove", "orders_customer"]
    choice=st.sidebar.selectbox("Operations",menu)
    # query_result=sql_excecutor("select * from ordersss LIMIT 0,3")
    # with st.expander("Show_ordersss"):
    #     query_df=pd.DataFrame(query_result)
    #     st.dataframe(query_df)
    if choice=="Add":
        create()
    elif choice=="View_all":
        View()
    elif choice=="Edit":
        Edit()
        View()
    elif choice=="Remove":
        View()
        Remove()
    elif choice == "orders_customer":
        orders_customer()
    # elif choice == "book_orderss_orderss":
    #     book_orderss_orderss()
    

    # elif choice=="supporters":
    #     supporters()


    # elif choice=="See_The_schedule":
    #     See_The_schedule()












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
    customer_id = st.text_input("customer_id:")
    customer_name = st.text_input("customer_name:")
    customer_surname=st.text_input("customer_surname")
    customer_email=st.text_input("customer_email")
    customer_city_code=st.text_input("customer_city_code")
    

    if st.button("Add customer"):
        cur.execute('INSERT INTO customer(customer_id, customer_name, customer_surname, customer_email, customer_city_code) VALUES (%s,%s,%s,%s,%s)',(customer_id, customer_name, customer_surname, customer_email, customer_city_code))
        mydb.commit()
        st.success("Successfully added customer: {}".format(customer_id))



def View():
    query_result=sql_excecutor("select * from customer")
    query_df=pd.DataFrame(query_result)
    st.dataframe(query_df)




def view_only_customer_names():
    cur.execute('select customer_id from customer')
    data = cur.fetchall()
    return data

def get_customer(customer_id):
    cur.execute('SELECT * FROM customer WHERE customer_id="{}"'.format(customer_id))
    data = cur.fetchall()
    return data


def Edit():
    list_of_customer=[i[0] for i in view_only_customer_names()]
    selected_customer=st.selectbox("customer to Edit",list_of_customer)
    selected_result=get_customer(selected_customer)
    if selected_result:
        customer_id = selected_result[0][0]
        customer_name = selected_result[0][1]
        customer_surname = selected_result[0][2]
        customer_email=selected_result[0][3]
        customer_city_code=selected_result[0][4]



        new_customer_id= st.text_input("Order_id:")
        new_customer_name = st.text_input("Shop_id:")
        new_customer_surname=st.text_input("Customer_id")
        new_customer_email=st.number_input("Price")
        # new_customertatus=st.text_input("order_status")
        new_customer_city_code=st.text_input("customer_city_code")
        # new_orderDate=st.date_input("order_date")
        # new_orderAddress=st.text_input("Address")
           
        if st.button("Update customer"):
                cur.execute("UPDATE customer SET customer_id=%s, customer_name=%s, customer_surname=%s, customer_email=%d, customer_city_code=%s WHERE customer_id=%s and customer_name=%s and customer_surname=%s and and customer_email=%d and customer_city_code=%s"  , (new_customer_id, new_customer_name, new_customer_surname, new_customer_email, new_customer_city_code, customer_id, customer_name, customer_surname, customer_email, customer_city_code))
                mydb.commit()
                st.success("Successfully updated:: {} to ::{}".format(customer_id, new_customer_id))



def Remove():
    list_of_customer=[i[0] for i in view_only_customer_names()]
    selected_customer=st.selectbox("order to delete",list_of_customer)
    # selected_result=get_shop(selected_shop)
    st.warning("Do you want to delete ::{}".format(selected_customer))
    if st.button("Delete order"):
        cur.execute('DELETE FROM customer WHERE customer_id="{}"'.format(selected_customer))
        mydb.commit()
        st.success("Customer has been deleted successfully")

# def See_The_schedule():
#     query_result=sql_excecutor("select * from shops,schedule where shops.customer_name=schedule.customer_name")
#     query_df=pd.DataFrame(query_result)
#     st.dataframe(query_df)


# def supporters():
#     query_result=sql_excecutor("select * from shops,supporters where shops.customer_name=supporters.customer_name")
#     query_df=pd.DataFrame(query_result)
#     st.dataframe(query_df)


def customer_city():
    query_result=sql_excecutor("select * from customer, city where customer.customer_city_code=city.customer_city_code")
    query_df=pd.DataFrame(query_result)
    st.dataframe(query_df)


# def No_of_Order():
#     query_result=sql_excecutor("select * from customer,orderproduct where customer.customer_id=orderproduct.customer_id")
#     query_df=pd.DataFrame(query_result)
#     st.dataframe(query_df)



# def Description():
#     query_result=sql_excecutor("select * from customer,orderdescription_logs where customer.customer_id=orderdescription_logs.customer_id")
#     query_df=pd.DataFrame(query_result)
#     st.dataframe(query_df)







def customer():
    st.title("customer")
    menu=["Add", "View_all", "Edit", "Remove","customer_city"]
    choice=st.sidebar.selectbox("Operations",menu)
    # query_result=sql_excecutor("select * from shops LIMIT 0,3")
    # with st.expander("Show_Shops"):
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
    elif choice=="customer_city":
        customer_city()
    # elif choice=="No_of_Order":
    #     No_of_Order()
    # elif choice=="Description":
    #     Description()
    

    # elif choice=="supporters":
    #     supporters()


    # elif choice=="See_The_schedule":
    #     See_The_schedule()

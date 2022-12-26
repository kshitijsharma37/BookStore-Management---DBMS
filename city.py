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
    customer_city_code= st.text_input("customer_city_code:")
    customer_city = st.text_input("customer_city:")
    # city_surname=st.text_input("city_surname:")
    if st.button("Add city"):
        cur.execute('INSERT INTO city(customer_city_code, customer_city) VALUES (%s,%s)',(customer_city_code, customer_city))
        mydb.commit()
        st.success("Successfully added city: {}".format(customer_city))



def View():
    query_result=sql_excecutor("select * from city")
    query_df=pd.DataFrame(query_result)
    st.dataframe(query_df)




def view_only_customer_citys():
    cur.execute('select customer_city_code from city')
    data = cur.fetchall()
    return data

def get_city(customer_city_code):
    cur.execute('SELECT * FROM city WHERE customer_city_code="{}"'.format(customer_city_code))
    data = cur.fetchall()
    return data








def Edit():
    list_of_citys=[i[0] for i in view_only_customer_citys()]
    selected_city=st.selectbox("city to Edit",list_of_citys)
    selected_result=get_city(selected_city)
    if selected_result:
        customer_city_code = selected_result[0][0]
        customer_city = selected_result[0][1]
        # City = selected_result[0][2]
        # city_surname = selected_result[0][2]
        # PhoneNum = selected_result[0][4]
        # Manager=selected_result[0][5]


        # col1,col2=st.columns(2)
        # with col1:
        new_customer_city_code= st.text_input("customer_city_code:")
        new_customer_city = st.text_input("Name:")
        # with col2:
        # new_City=st.selectbox("City", ["Bangalore", "Chennai", "Mumbai"])
        # new_city_surname=st.text_input("city_surname:")
        # new_PhoneNum=st.text_input("Phone_number")
        # new_Manager=st.text_input("Manager_Name")
        if st.button("Update city"):
                cur.execute("UPDATE city SET customer_city_code=%s, customer_city=%s WHERE customer_city_code=%s and customer_city=%s", (new_customer_city_code, new_customer_city, customer_city_code, customer_city))
                mydb.commit()
                st.success("Successfully updated:: {} to ::{}".format(customer_city, new_customer_city))



def Remove():
    list_of_citys=[i[0] for i in view_only_customer_citys()]
    selected_city=st.selectbox("city to delete",list_of_citys)
    # selected_result=get_city(selected_city)
    st.warning("Do you want to delete ::{}".format(selected_city))
    if st.button("Delete city"):
        cur.execute('DELETE FROM city WHERE customer_city_code="{}"'.format(selected_city))
        mydb.commit()
        st.success("city has been deleted successfully")

# def See_The_schedule():
#     query_result=sql_excecutor("select * from citys,schedule where citys.customer_city_code=schedule.customer_city_code")
#     query_df=pd.DataFrame(query_result)
#     st.dataframe(query_df)


# def supporters():
#     query_result=sql_excecutor("select * from citys,supporters where citys.customer_city_code=supporters.customer_city_code")
#     query_df=pd.DataFrame(query_result)
#     st.dataframe(query_df)




def city():
    st.title("citys")
    menu=["Add", "View_all", "Edit", "Remove"]
    choice=st.sidebar.selectbox("Operations",menu)
    # query_result=sql_excecutor("select * from citys LIMIT 0,3")
    # with st.expander("Show_citys"):
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
    

    # elif choice=="supporters":
    #     supporters()


    # elif choice=="See_The_schedule":
    #     See_The_schedule()












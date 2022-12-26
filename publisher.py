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
    publisher_id= st.text_input("publisher_id:")
    publisher_name = st.text_input("publisher_name:")
    # City=st.selectbox("City", ["Bangalore", "Chennai", "Mumbai"])
    # shopID=st.text_input("shop_id:")
    publisher_phone=st.text_input("publisher_phone")
    if st.button("Add publisher"):
        cur.execute('INSERT INTO publisher(publisher_id, publisher_name, publisher_phone) VALUES (%s,%s,%s)',(publisher_id, publisher_name, publisher_phone))
        mydb.commit()
        st.success("Successfully added publisher: {}".format(publisher_name))



def View():
    query_result=sql_excecutor("select * from publisher")
    query_df=pd.DataFrame(query_result)
    st.dataframe(query_df)




def view_only_publisher_names():
    cur.execute('select publisher_id from publisher')
    data = cur.fetchall()
    return data

def get_publisher(publisher_id):
    cur.execute('SELECT * FROM publisher WHERE publisher_id="{}"'.format(publisher_id))
    data = cur.fetchall()
    return data








def Edit():
    list_of_publishers=[i[0] for i in view_only_publisher_names()]
    selected_publisher=st.selectbox("publisher to Edit",list_of_publishers)
    selected_result=get_publisher(selected_publisher)
    if selected_result:
        publisher_id = selected_result[0][0]
        publisher_name = selected_result[0][1]
        # shopID = selected_result[0][2]
        publisher_phone = selected_result[0][2]


        # col1,col2=st.columns(2)
        # with col1:
        new_publisher_id= st.text_input("publisher_id:")
        new_publisher_name = st.text_input("Name:")
        # new_shopID=st.text_input("shop_id:")
        new_publisher_phone=st.text_input("publisher_phone")
        if st.button("Update publisher"):
                cur.execute("UPDATE publisher SET publisher_id=%s, publisher_name=%s, publisher_phone=%s WHERE publisher_id=%s and publisher_name=%s and publisher_phone=%s"  , (new_publisher_id, new_publisher_name, new_publisher_phone, publisher_id, publisher_name, publisher_phone))
                mydb.commit()
                st.success("Successfully updated:: {} to ::{}".format(publisher_name, new_publisher_name))



def Remove():
    list_of_publishers=[i[0] for i in view_only_publisher_names()]
    selected_publisher=st.selectbox("Publisher to delete",list_of_publishers)
    # selected_result=get_shop(selected_shop)
    st.warning("Do you want to delete ::{}".format(selected_publisher))
    if st.button("Delete publisher"):
        cur.execute('DELETE FROM publisher WHERE publisher_id="{}"'.format(selected_publisher))
        mydb.commit()
        st.success("publisher has been deleted successfully")


def publisher():
    st.title("publishers")
    menu=["Add", "View_all", "Edit", "Remove"]
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

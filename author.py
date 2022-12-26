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
    author_id= st.text_input("author_id:")
    author_name = st.text_input("author_name:")
    author_surname=st.text_input("author_surname:")
    if st.button("Add author"):
        cur.execute('INSERT INTO author(author_id, author_name, author_surname) VALUES (%s,%s,%s)',(author_id, author_name, author_surname))
        mydb.commit()
        st.success("Successfully added author: {}".format(author_name))



def View():
    query_result=sql_excecutor("select * from author")
    query_df=pd.DataFrame(query_result)
    st.dataframe(query_df)




def view_only_author_names():
    cur.execute('select author_id from author')
    data = cur.fetchall()
    return data

def get_author(author_id):
    cur.execute('SELECT * FROM author WHERE author_id="{}"'.format(author_id))
    data = cur.fetchall()
    return data








def Edit():
    list_of_authors=[i[0] for i in view_only_author_names()]
    selected_author=st.selectbox("author to Edit",list_of_authors)
    selected_result=get_author(selected_author)
    if selected_result:
        author_id = selected_result[0][0]
        author_name = selected_result[0][1]
        # City = selected_result[0][2]
        author_surname = selected_result[0][2]
        # PhoneNum = selected_result[0][4]
        # Manager=selected_result[0][5]


        # col1,col2=st.columns(2)
        # with col1:
        new_author_id= st.text_input("author_id:")
        new_author_name = st.text_input("Name:")
        # with col2:
        # new_City=st.selectbox("City", ["Bangalore", "Chennai", "Mumbai"])
        new_author_surname=st.text_input("author_surname:")
        # new_PhoneNum=st.text_input("Phone_number")
        # new_Manager=st.text_input("Manager_Name")
        if st.button("Update author"):
                cur.execute("UPDATE author SET author_id=%s, author_name=%s, author_surname=%s WHERE author_id=%s and author_name=%s and author_surname=%s", (new_author_id, new_author_name, new_author_surname, author_id, author_name, author_surname))
                mydb.commit()
                st.success("Successfully updated:: {} to ::{}".format(author_name, new_author_name))



def Remove():
    list_of_authors=[i[0] for i in view_only_author_names()]
    selected_author=st.selectbox("author to delete",list_of_authors)
    # selected_result=get_author(selected_author)
    st.warning("Do you want to delete ::{}".format(selected_author))
    if st.button("Delete author"):
        cur.execute('DELETE FROM author WHERE author_id="{}"'.format(selected_author))
        mydb.commit()
        st.success("author has been deleted successfully")

# def See_The_schedule():
#     query_result=sql_excecutor("select * from authors,schedule where authors.author_id=schedule.author_id")
#     query_df=pd.DataFrame(query_result)
#     st.dataframe(query_df)


# def supporters():
#     query_result=sql_excecutor("select * from authors,supporters where authors.author_id=supporters.author_id")
#     query_df=pd.DataFrame(query_result)
#     st.dataframe(query_df)




def author():
    st.title("authors")
    menu=["Add", "View_all", "Edit", "Remove"]
    choice=st.sidebar.selectbox("Operations",menu)
    # query_result=sql_excecutor("select * from authors LIMIT 0,3")
    # with st.expander("Show_authors"):
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












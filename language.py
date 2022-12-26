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
    country_id= st.text_input("country_id:")
    book_released_country = st.text_input("book_released_country:")
    book_language=st.text_input("book_language:")
    if st.button("Add language"):
        cur.execute('INSERT INTO language(country_id, book_released_country, book_language) VALUES (%s,%s,%s)',(country_id, book_released_country, book_language))
        mydb.commit()
        st.success("Successfully added language: {}".format(book_language))



def View():
    query_result=sql_excecutor("select * from language")
    query_df=pd.DataFrame(query_result)
    st.dataframe(query_df)




def view_only_language_names():
    cur.execute('select country_id from language')
    data = cur.fetchall()
    return data

def get_language(country_id):
    cur.execute('SELECT * FROM language WHERE country_id="{}"'.format(country_id))
    data = cur.fetchall()
    return data



def Edit():
    list_of_language=[i[0] for i in view_only_language_names()]
    selected_language=st.selectbox("language to Edit",list_of_language)
    selected_result=get_language(selected_language)
    if selected_result:
        country_id = selected_result[0][0]
        book_released_country = selected_result[0][1]
        book_language = selected_result[0][2]
        # Address = selected_result[0][3]
        # PhoneNum = selected_result[0][4]
        # ShopID=selected_result[0][5]


        # col1,col2=st.columns(2)
        # with col1:
        new_country_id= st.text_input("country_id:")
        new_book_released_country = st.text_input("book_released_country:")
        new_book_language=st.text_input("book_language:")
        if st.button("Update language"):
                cur.execute("UPDATE language SET country_id=%s, book_released_country=%s WHERE country_id=%s and book_released_country=%s and book_language=%s", (new_country_id, new_book_released_country, new_book_language, country_id, book_released_country, book_language))
                mydb.commit()
                st.success("Successfully updated:: {} to ::{}".format(book_released_country, new_book_released_country))



def Remove():
    list_of_language=[i[0] for i in view_only_language_names()]
    selected_language=st.selectbox("language to delete",list_of_language)
    # selected_result=get_shop(selected_shop)
    st.warning("Do you want to delete ::{}".format(selected_language))
    if st.button("Delete language"):
        cur.execute('DELETE FROM language WHERE book_released_country="{}"'.format(selected_language))
        mydb.commit()
        st.success("language has been deleted successfully")

# def See_The_schedule():
#     query_result=sql_excecutor("select * from shops,schedule where shops.ShopID=schedule.shopID")
#     query_df=pd.DataFrame(query_result)
#     st.dataframe(query_df)



def language():
    st.title("language")
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
    # elif choice=="See_The_schedule":
    #     See_The_schedule()

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
    isbn= st.text_input("isbn:")
    book_name = st.text_input("book_name:")
    publisher_id = st.text_input("publisher_id:")
    book_category = st.text_input("book_category:")
    book_released_year = st.text_input("book_released_year:")
    country_id = st.text_input("country_id:")
    book_price = st.text_input("book_price:")
    book_stock = st.text_input("book_stock:")

    if st.button("Add Books"):
        cur.execute('INSERT INTO book(isbn, book_name, publisher_id, book_category, book_released_year, country_id, book_price, book_stock) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(isbn, book_name, publisher_id, book_category, book_released_year, country_id,book_price, book_stock))
        mydb.commit()
        st.success("Successfully added Book: {}".format(book_name))



def View():
    query_result=sql_excecutor("select * from book")
    query_df=pd.DataFrame(query_result)
    st.dataframe(query_df)




def view_only_book_id():
    cur.execute('select isbn from book')
    data = cur.fetchall()
    return data

def get_books(isbn):
    cur.execute('SELECT * FROM book WHERE isbn="{}"'.format(isbn))
    data = cur.fetchall()
    return data



def Edit():
    list_of_books=[i[0] for i in view_only_book_id()]
    selected_books = st.selectbox("Books to Edit", list_of_books)
    selected_result=get_books(selected_books)
    if selected_result:
        isbn = selected_result[0][0]
        book_name = selected_result[0][1]
        publisher_id = selected_result[0][2]
        book_category = selected_result[0][3]
        book_released_year = selected_result[0][4]
        country_id=selected_result[0][5]
        book_price=selected_result[0][6]
        book_stock=selected_result[0][7]



        new_isbn= st.text_input("isbn:")
        new_book_name = st.text_input("book_name:")
        new_publisher_id=st.text_input("publisher_id:")
        new_book_category=st.text_input("book_category:")
        new_book_released_year=st.text_input("book_released_year:")
        new_country_id=st.text_input("country_id:")
        new_book_price=st.text_input("book_price:")
        new_book_stock=st.text_input("book_stock:")
        # new_book_price=st.text_input("Shop_id")
        # new_book_stock=st.text_input("book_stock:")
        if st.button("Update Book"):
                cur.execute("UPDATE book SET isbn=%s, book_name=%s, publisher_id=%s, book_category=%s, book_released_year=%s,country_id=%s,book_price=%s, book_stock=%s WHERE isbn=%s and book_name=%s and publisher_id=%s and book_category=%s and book_released_year=%s and country_id=%s and book_price=%s and book_stock=%s"   , (new_isbn, new_book_name, new_publisher_id, new_book_category, new_book_released_year, new_country_id,new_book_price, new_book_stock, isbn, book_name, publisher_id, book_category,book_released_year, country_id, book_price, book_stock))
                mydb.commit()
                st.success("Successfully updated:: {} to ::{}".format(isbn, new_isbn))



def Remove():
    list_of_books=[i[0] for i in view_only_book_id()]
    selected_books=st.selectbox("Books to Edit",list_of_books)
    # selected_result=get_shop(selected_shop)
    st.warning("Do you want to delete ::{}".format(selected_books))
    if st.button("Delete books"):
        cur.execute('DELETE FROM book WHERE isbn="{}"'.format(selected_books))
        mydb.commit()
        st.success("Book has been deleted successfully")

# def See_The_schedule():
#     query_result=sql_excecutor("select * from shops,schedule where shops.new_book_price=schedule.new_book_price")
#     query_df=pd.DataFrame(query_result)
#     st.dataframe(query_df)



def book():
    st.title("Book")
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
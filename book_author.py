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
    book_author_id= st.text_input("book_author_id:")
    isbn = st.text_input("isbn:")
    author_id=st.text_input("author_id:")
    if st.button("Add author"):
        cur.execute('INSERT INTO author(book_author_id, isbn, author_id) VALUES (%s,%s,%s)',(book_author_id, isbn, author_id))
        mydb.commit()
        st.success("Successfully added author: {}".format(isbn))



def View():
    query_result=sql_excecutor("select * from author")
    query_df=pd.DataFrame(query_result)
    st.dataframe(query_df)




def view_only_isbns():
    cur.execute('select book_author_id from author')
    data = cur.fetchall()
    return data

def get_author(book_author_id):
    cur.execute('SELECT * FROM author WHERE book_author_id="{}"'.format(book_author_id))
    data = cur.fetchall()
    return data








def Edit():
    list_of_authors=[i[0] for i in view_only_isbns()]
    selected_author=st.selectbox("author to Edit",list_of_authors)
    selected_result=get_author(selected_author)
    if selected_result:
        book_author_id = selected_result[0][0]
        isbn = selected_result[0][1]
        # City = selected_result[0][2]
        author_id = selected_result[0][2]
        # PhoneNum = selected_result[0][4]
        # Manager=selected_result[0][5]


        # col1,col2=st.columns(2)
        # with col1:
        new_book_author_id= st.text_input("book_author_id:")
        new_isbn = st.text_input("ISBN:")
        # with col2:
        # new_City=st.selectbox("City", ["Bangalore", "Chennai", "Mumbai"])
        new_author_id=st.text_input("author_id:")
        # new_PhoneNum=st.text_input("Phone_number")
        # new_Manager=st.text_input("Manager_Name")
        if st.button("Update author"):
                cur.execute("UPDATE author SET book_author_id=%s, isbn=%s, author_id=%s WHERE book_author_id=%s and isbn=%s and author_id=%s", (new_book_author_id, new_isbn, new_author_id, book_author_id, isbn, author_id))
                mydb.commit()
                st.success("Successfully updated:: {} to ::{}".format(isbn, new_isbn))



def Remove():
    list_of_authors=[i[0] for i in view_only_isbns()]
    selected_author=st.selectbox("author to delete",list_of_authors)
    # selected_result=get_author(selected_author)
    st.warning("Do you want to delete ::{}".format(selected_author))
    if st.button("Delete author"):
        cur.execute('DELETE FROM author WHERE book_author_id="{}"'.format(selected_author))
        mydb.commit()
        st.success("author has been deleted successfully")

def book_author_book():
    query_result=sql_excecutor("select * from book_author, book where book_author.isbn=book.isbn")
    query_df=pd.DataFrame(query_result)
    st.dataframe(query_df)


def book_author_author():
    query_result=sql_excecutor("select * from book_author,author where book_author.author_id=author.author_id")
    query_df=pd.DataFrame(query_result)
    st.dataframe(query_df)




def book_author():
    st.title("authors")
    menu=["Add", "View_all", "Edit", "Remove", "book_author_book", "book_author_author"]
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
    elif choice == "book_author_book":
        book_author_book()
    elif choice == "book_author_author":
        book_author_author()
    

    # elif choice=="supporters":
    #     supporters()


    # elif choice=="See_The_schedule":
    #     See_The_schedule()












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
    isbn = st.text_input("isbn:")
    book_quantity=st.text_input("book_quantity:")
    if st.button("Add book_order"):
        cur.execute('INSERT INTO book_order(order_id, isbn, book_quantity) VALUES (%s,%s,%s)',(order_id, isbn, book_quantity))
        mydb.commit()
        st.success("Successfully added book_order: {}".format(isbn))



def View():
    query_result=sql_excecutor("select * from book_order")
    query_df=pd.DataFrame(query_result)
    st.dataframe(query_df)




def view_only_author_id():
    cur.execute('select order_id, isbn from book_order')
    data = cur.fetchall()
    return data

def get_book_order(order_id, isbn):
    cur.execute('SELECT * FROM book_order WHERE order_id, isbn="{}"'.format(order_id, isbn))
    data = cur.fetchall()
    return data








def Edit():
    list_of_book_orders=[i[0] for i in view_only_author_id()]
    selected_book_order=st.selectbox("book_order to Edit",list_of_book_orders)
    selected_result=get_book_order(selected_book_order)
    if selected_result:
        order_id = selected_result[0][0]
        isbn = selected_result[0][1]
        # City = selected_result[0][2]
        book_quantity = selected_result[0][2]
        # PhoneNum = selected_result[0][4]
        # Manager=selected_result[0][5]


        # col1,col2=st.columns(2)
        # with col1:
        new_order_id= st.text_input("order_id:")
        new_isbn = st.text_input("ISBN:")
        # with col2:
        # new_City=st.selectbox("City", ["Bangalore", "Chennai", "Mumbai"])
        new_book_quantity=st.text_input("book_quantity:")
        # new_PhoneNum=st.text_input("Phone_number")
        # new_Manager=st.text_input("Manager_Name")
        if st.button("Update book_order"):
                cur.execute("UPDATE book_order SET order_id=%s, isbn=%s, book_quantity=%s WHERE order_id=%s and isbn=%s and book_quantity=%s", (new_order_id, new_isbn, new_book_quantity, order_id, isbn, book_quantity))
                mydb.commit()
                st.success("Successfully updated:: {} to ::{}".format(isbn, new_isbn))



def Remove():
    list_of_book_orders=[i[0] for i in view_only_author_id()]
    selected_book_order=st.selectbox("book_order to delete",list_of_book_orders)
    # selected_result=get_book_order(selected_book_order)
    st.warning("Do you want to delete ::{}".format(selected_book_order))
    if st.button("Delete book_order"):
        cur.execute('DELETE FROM book_order WHERE order_id="{}"'.format(selected_book_order))
        mydb.commit()
        st.success("book_order has been deleted successfully")

# def book_book_order_book():
#     query_result=sql_excecutor("select * from book_book_order, book where book_book_order.isbn=book.isbn")
#     query_df=pd.DataFrame(query_result)
#     st.dataframe(query_df)


# def book_book_order_book_order():
#     query_result=sql_excecutor("select * from book_book_order,book_order where book_book_order.book_quantity=book_order.book_quantity")
#     query_df=pd.DataFrame(query_result)
#     st.dataframe(query_df)




def order_book():
    st.title("book_orders")
    menu=["Add", "View_all", "Edit", "Remove"]#, "book_book_order_book", "book_book_order_book_order"]
    choice=st.sidebar.selectbox("Operations",menu)
    # query_result=sql_excecutor("select * from book_orders LIMIT 0,3")
    # with st.expander("Show_book_orders"):
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
    # elif choice == "book_book_order_book":
    #     book_book_order_book()
    # elif choice == "book_book_order_book_order":
    #     book_book_order_book_order()
    

    # elif choice=="supporters":
    #     supporters()


    # elif choice=="See_The_schedule":
    #     See_The_schedule()












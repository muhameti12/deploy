import pandas as pd
import streamlit as st
import plotly.express as px

books_df=pd.read_csv('bestsellers_with_categories_2022_03_27.csv')
#2. importing the data from the file

st.title('Best selling books')
st.write("This app analyzes the Amazone top selling books from 2009 to 2022")
#3. set title for this app


st.subheader('Summery statics')
total_books=books_df.shape[0]
unique_title=books_df['Name'].nunique()
average_rating=books_df['User Rating'].mean()
average_price=books_df['Price'].mean()
#4. summery statictics

col1, col2, col3, col4= st.columns(4)

col1.metric('Total Books', total_books)
col2.metric('Unique Title', unique_title)
col3.metric('Average Rating', f"{average_rating:.2f}")
col4.metric('Average Price', f"${average_price:.2f}")
#dataset priview

st.subheader('Dataset review')
st.write(books_df.head())

col1,col2=st.columns(2)

with col1:
    st.header("Top 10 rated titles")
    top_titles=books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.header("Top 10 Authors")
    top_authors=books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

st.subheader("Genre Distribution")
fig=px.pie(books_df,names='Genre',title='Genre Distribution', color="Genre", color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Number of fictional and non fictional books over the years")
size=books_df.groupby(["Year","Genre"]).size().reset_index(name="Counts")
fig=px.bar(size, x="Year", y="Counts",title="Number of Fictional and Non-Fictional Books",color_discrete_sequence=px.colors.sequential.Plasma,barmode="group")
st.plotly_chart(fig)


st.subheader("Top 15 authors")
top_authors=books_df['Author'].value_counts().head(15).reset_index()
top_authors.columns=['Author','Count']
fig=px.bar(top_authors,x="Count",y="Author",orientation='h',title="Top 15 authors",labels={'Count':'Counts of Books published','Author':'Author'},
           color='Count', color_continuous_scale=px.colors.sequential.Plasma)

st.plotly_chart(fig)

st.subheader("Filter data by Genre")
genre_filter=st.selectbox("Select Genre",books_df["Genre"].unique())
filter_df=books_df[books_df["Genre"]==genre_filter]
st.write(filter_df)


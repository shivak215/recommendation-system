
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


bk=pd.read_csv("Desktop/book.csv",sep=';',error_bad_lines=False,encoding="Latin-1")


# In[3]:


bk.head(10)


# In[25]:


bk.describe()


# In[4]:


print(bk.shape)


# In[5]:


bk.drop(['Image-URL-S','Image-URL-M','Image-URL-L'],axis=1,inplace=True)


# In[6]:


bk.head(2)


# In[7]:


bk.dtypes


# In[8]:


x=bk.Year-Of-Publication.unique()


# In[9]:


bk.columns=['ISBN','booktitle','author','yearofpublication','publisher']


# In[10]:


bk.yearofpublication.unique()


# In[11]:


bk.ISBN.unique()


# In[12]:


bk.publisher.unique()


# In[13]:


pd.set_option('display.max_colwidth',-1)
bk.loc[bk.yearofpublication=='DK Publishing Inc',:]


# In[14]:


bk.loc[bk.publisher.isnull(),:]


# In[15]:


bk.loc[bk.ISBN=='078946697X','yearofpublication']=2000


# In[16]:


bk.loc[bk.ISBN=='078946697X','author']="Michael Teitelbaum"
bk.loc[bk.ISBN=='078946697X','booktitle']="DK Readers: Creating the X-Men, How It All Began (Level 4: Proficient Readers)"
bk.loc[bk.ISBN=='078946697X','publisher']="DK Publishing Inc"
bk.loc[bk.ISBN=='0789466953','yearofpublication']=2000
bk.loc[bk.ISBN=='0789466953','author']="James Buckley"
bk.loc[bk.ISBN=='0789466953','booktitle']="DK Readers: Creating the X-Men, How Comic Books Come to Life (Level 4: Proficient Readers)"
bk.loc[bk.ISBN=='0789466953','publisher']="DK Publishing Inc"


# In[17]:


pd.set_option('display.max_colwidth',-1)
bk.loc[bk.yearofpublication=='Gallimard',:]


# In[18]:


bk.loc[bk.ISBN=='2070426769','yearofpublication']=2003
bk.loc[bk.ISBN=='2070426769','author']="Jean-Marie Gustave Le ClÃ?Â©zio"
bk.loc[bk.ISBN=='2070426769','booktitle']="Peuple du ciel, suivi de 'Les Bergers"
bk.loc[bk.ISBN=='2070426769','publisher']="Gallimard"


# In[19]:


bk.yearofpublication.unique()


# In[20]:


bk.yearofpublication=pd.to_numeric(bk.yearofpublication,errors='ignore')


# In[21]:


bk.yearofpublication.unique()


# In[22]:


bk.loc[bk.yearofpublication==0,'yearofpublication']=np.nan
bk.yearofpublication.fillna(round(bk.yearofpublication.mean()),inplace=True)


# In[23]:


bk.yearofpublication.unique()


# In[24]:


bk.loc[bk.yearofpublication>2018,'yearofpublication']=2018


# In[25]:


bk.publisher.unique()


# In[26]:


bk.loc[bk.publisher.isnull(),:]


# In[27]:


bk.loc[bk.ISBN=='193169656X','publisher']='recordnotthere'
bk.loc[bk.ISBN=='1931696993','publisher']='recordnotthere'


# In[28]:


bk.loc[bk.ISBN.isnull(),:]


# In[29]:


bk.loc[bk.booktitle.isnull(),:]


# In[30]:


bk.loc[bk.author.isnull(),:]


# In[31]:


bk.loc[bk.ISBN=='9627982032','author']='rowling'


# In[32]:


bk.loc[bk.yearofpublication.isnull(),:]


# In[33]:


users = pd.read_csv('Desktop/user.csv', sep=';', error_bad_lines=False, encoding="latin-1")
users.columns = ['userID', 'Location', 'Age']
ratings = pd.read_csv('Desktop/rat.csv', sep=';', error_bad_lines=False, encoding="latin-1")
ratings.columns = ['userID', 'ISBN', 'bookRating']


# In[34]:


users.shape


# In[36]:


users.head(10)


# In[37]:


users.userID.unique()


# In[38]:


users.Location.unique()


# In[39]:


users.Age.unique()


# In[40]:


users.loc[(users.Age > 90) | (users.Age < 5), 'Age'] = np.nan


# In[41]:


users.Age = users.Age.fillna(users.Age.mean())


# In[42]:


users.Age = users.Age.astype(np.int32)


# In[43]:


ratings.shape


# In[44]:


#rating*user =total 
ratings.head(10)


# In[45]:


ratings.bookRating.unique()


# In[47]:


ratings_new = ratings[ratings.ISBN.isin(bk.ISBN)]
##coz some isbn not in my original dset bk


# In[48]:


ratings_new = ratings_new[ratings_new.bookRating != 0]


# In[50]:


print(ratings_new.shape)


# In[52]:


import seaborn as sb
import matplotlib.pyplot as plt
sb.countplot(data=ratings_new , x='bookRating')
plt.show()


# In[53]:


ratings_cnt = pd.DataFrame(ratings_new.groupby(['ISBN'])['bookRating'].sum())##pb....nou use nhi kiya think
top = ratings_cnt.sort_values('bookRating',ascending=False).head(100)
print("Following books are recommended")
top.merge(bk,left_index=True,right_on='ISBN')


# In[56]:


ratings_cnt = pd.DataFrame(ratings_new.groupby(['ISBN'])['bookRating'].mean())##pb....nou use nhi kiya think
top = ratings_cnt.sort_values('bookRating',ascending=False).head(100)
print("Following books are recommended")
top.merge(bk,left_index=True,right_on='ISBN')


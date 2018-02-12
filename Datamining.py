import pandas as pd

Papers = pd.read_table('Papers.tsv',header=None,names=['paper_id','title','publish_year','publish_year','conferece_id','conference_abbrv'])
#Open Papers.tsv and add columns header
Affi = pd.read_table('Affiliations.tsv',header=None,names= ['affilifation_id','name'])
#open Affi.tsv and add columns header
Paper_author = pd.read_table('PaperAuthorAffilliations.tsv',header=None,names=['paper_id','author_id','affilifation_id]','affi','name','count'])
#open Paer Author Affiliations.tsv and add columns header

df=pd.merge(Papers,Paper_author,on='paper_id')
#Connect Papers.tsv and Paper_author.tsv with paper_id
df=pd.merge(df,Affi,on='affilifation_id')
#Connect first df and Affi.tsv with affilifation_id

df1=df(['paper_id','publish_year','conference_abbrv','affilifation_id'])
#start to do paper_count csv
df1=df1.drop.duplicates('paper_id')
#duplicates paper_id
grouped=df1.groupby(['paper_id','publish_year','conference_abbrv','affilifation_id'])
#group the data under these header to use sort function
values=grouped['affilifation_id'].value_counts()
#Count values
df2=df1[['publish_year','conference_abbrv','affiliation_id']].drop_duplicates() #delet duplicates
df2['paper_counts']=list(values)
df3=df2[['conference_abbrv','publish_year','affiliation_id','paper_counts']].sort_values('paper_counts')[::-1]
#sort values from greates to samllest
df3.to_csv('paper_count.csv',index=False)
df4=df3 #output file in csv by excel

df1=df[['author_id','publish_year','conference_abbrv','affiliation_id']]
df1=df1.drop_duplicates('author_id')
grouped=df1.groupby(['publish_year','conference_abbrv','affiliation_id'])
values=grouped['affiliation_id'].value_counts()
df2=df1[['publish_year','conference_abbrv','affiliation_id']].drop_duplicates()
df2['author_counts']=list(values)
df3=df2[['conference_abbrv','publish_year','affiliation_id','author_counts']].sort_values('author_counts')[::-1]
#Sort author from greatest to samllest
df3.to_csv('author_count.csv',index=False)
# print df3 in csv by excel

df5=pd.merge(df3,df4,on=['conference_abbrv','publish_year','affiliation_id'],how='outer')
df5=df5.fillna(0)# use 0 fill in missing data
# print(df5)
df5['score']=df5['author_counts']*0.8+df5['paper_counts']*0.2  #given weight to author_counts and paper_counts, then rank data
print(df5.sort_values('score')[::-1]) #greatest to samllest
df5.to_csv('score.csv',index=False)
#outpot score in csv by excel
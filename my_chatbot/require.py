import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

##xlsx=pd.read_excel('wellness_data.xlsx')
##xlsx.to_csv("wellness_data.csv")

model=SentenceTransformer('jhgan/ko-sroberta-multitask')


df=pd.read_csv("wellness_data.csv")
df.head()
df=df.drop(columns=['Unnamed: 3'])
df=df[~df['챗봇'].isna()]
df['embedding']=pd.Series([[]]*len(df))

df['embedding']=df['유저'].map(lambda x:list(model.encode(x)))
print(df.head())






'''while True:
    text=input("질문: ")
    embedding=model.encode(text)
    df['distance']=df['embedding'].map(lambda x:cosine_similarity([embedding],[x]).squeeze())
    df.head()
    answer=df.loc[df['distance'].idxmax()]
    #print('구분: ',answer['구분'])
    print('유사한 질문: ',answer['유저'])
    print('챗봇 답변: ',answer['챗봇'])
    print('유사도: ',answer['distance'])'''

def check_similarity(question):
    embedding=model.encode(question)
    df['distance']=df['embedding'].map(lambda x:cosine_similarity([embedding],[x]).squeeze())
    df.head()
    answer=df.loc[df['distance'].idxmax()]
    if answer['distance']>0.7:
        print("similarity: {}".format(answer['distance']))
        print("Chatbot > {}".format(answer['챗봇']))
        return True
    else:
        print("KoGPT2로 문장생성")
        print("similarity: {}".format(answer['distance']))
        
        return False
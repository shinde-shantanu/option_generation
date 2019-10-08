import pickle

from gensim.models.keyedvectors import KeyedVectors
glove_model = KeyedVectors.load_word2vec_format("gensim_glove_vectors.txt", binary=False)

s=""
while s!="exit":
    try:
        s=input("\nEnter word: ")
        op=glove_model.most_similar([s])
        for x in op:
            print(x[0])
    except:
        print("Word not in corpora")
        pass

def mk_option(ip):
    try:
        s=input("\nEnter word: ")
        op=glove_model.most_similar([s])
        return(op)
    except:
        return("Word not in corpora")

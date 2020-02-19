import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def pure_aloha_throughput(G):
    return G*np.exp(-2*G)    

def pure_aloha_sim(data):
    data['Throughput'] = data['Avg Load'].apply(pure_aloha_throughput)
    plt.plot(data['Avg Load'],data['Throughput'],marker ='',color = 'red',linewidth='2.5')
    plt.xlabel("Load offered (G)")
    plt.ylabel("Throughput (S)")
    plt.savefig('Pure_Aloha.png')
    plt.show() 




if __name__ == "__main__":
    load = np.arange(0.0,2.1,0.1)

    data = { "Avg Load" : load}
    df = pd.DataFrame(data)

    pure_aloha_sim(df)
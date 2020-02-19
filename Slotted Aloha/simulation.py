import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import random


Simulation_duration = 10000

def next_pkt(load):
    return (-1/load)*np.log(random.random())

def slotted_aloha_throughput_theoretical(G):
    return G*np.exp(-G)    

def slotted_aloha_throughput(G):
    time = 0
    pkt = []
    for i in range(0,Simulation_duration):
        time += next_pkt(G)
        pkt.append(np.ceil(time))


    
    success = 0
    for x in range(1,len(pkt)-1):
        if (pkt[x] != pkt[x-1]  and pkt[x+1] != pkt[x]):
            success += 1

    

    return float(success)/len(pkt) * G

def slotted_aloha_sim(data):
    data['Throughput Theoretical'] = data['Avg Load'].apply(slotted_aloha_throughput_theoretical)
    plt.plot(data['Avg Load'],data['Throughput Theoretical'],marker ='',color = 'red',linewidth='2.5')
    plt.xlabel("Load offered (G)")
    plt.ylabel("Throughput (S)")
    plt.grid(True)
    plt.savefig('Slotted_Aloha_Theoretical.png')
    plt.show() 

    data['Throughput'] = data['Avg Load'].apply(slotted_aloha_throughput)
    plt.plot(data['Avg Load'],data['Throughput'],marker ='',color = 'red',linewidth='2.5')
    plt.xlabel("Load offered (G)")
    plt.ylabel("Throughput (S)")
    plt.grid(True)
    plt.savefig('Slotted_Aloha.png')
    plt.show() 





if __name__ == "__main__":
    load = np.arange(0.1,2.1,0.1)

    data = { "Avg Load" : load}
    df = pd.DataFrame(data)

    slotted_aloha_sim(df)
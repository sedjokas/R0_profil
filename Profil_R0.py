#Author: Selain Kasereka
#Purpose: Research article on Covid-19 (2019-nCov)
#Description: Profile of R0 as a function of the incubation period (1 to 100 days)
#With Prof Dr Emile-Franc Doungmo Goufo and Prof Dr Morgan (all from UNISA)

#load and import libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as si

#Parameters of the model
Lambda=0.003
beta_h=0.015
beta_F=0.001
pi=0.02
d_h=0.0002
sigma_h=0.1
w_2=0.9
e_1=0.0001
e_2=0.0001
gamma_1=0.00000002
gamma_2=0.00000002
e=0.0002
phi=0.003

#Define the incubation period
w_1 = np.arange(100)+1  #Define the time of the model (incubation period), Nota: avoid zero
w_1

#Compute the R0 
for i in w_1:
    R0=(beta_h*Lambda/(d_h*((1-sigma_h)*1/(w_1) + sigma_h*w_2+d_h)))*((((1-sigma_h)*1/(w_1))/(e_1 + d_h + phi)) + ((pi*sigma_h*w_2)/(e_2 + d_h)))

#Plot the profile of R0
t_start=0
t_end=100
t_step=100
T=np.linspace(t_start, t_end, t_step) # our space
plt.figure('my graph') # Create another page for plotting
plt.plot(T,R0,label="R0", linewidth=3) # Plot T and R0 to pbtain R0 profile
plt.legend(bbox_to_anchor=[0.98, 0.98]) # Label the plots on this position
plt.xlabel('Incubation period in day')
plt.ylabel('Basic Reproduction Number R0')
plt.show() #Show the plot
# The End of the program

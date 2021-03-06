import matplotlib.pyplot as plt
import math

'''
Try two other choices for Ie(t) (A periodic function for example).  
Add the graphs showing the current and voltage traces to your notes.
'''

# Collaborated with Cat G and Raveen K

# Set constants

R_membrane = 1 * 10 ** 7
V_threshold = -50 * (10 ** -3)
tau = 0.01
dt = 1 * (10**-5)
EL = -0.065
dv = 0

# Initialize dictionaries to place calculated values

V = {}
I_e = {}

t = 0
V[t] = EL
t_f = 0.3

# Count resets
counter = 0

# Obtain potentials by scanning across time range

while t < t_f:
    I_e_sine = math.sin(t / t_f * 2 * math.pi) * 5 * (10 ** -9)
    I_e[t] = I_e_sine
    dv = (dt / tau) * ((EL - V[t]) + (R_membrane * I_e_sine))

    V_temp = V[t] + dv
    t = t + dt

    V[t] = V_temp

    if V[t] >= V_threshold:
        V[t] = EL
        counter = counter + 1

# Plot axes

plt.plot(list(V.keys()), list(V.values()), color='#444444', linestyle='--', label='')
plt.xlabel('Time (s)')
plt.ylabel('Potential (mV)')
plt.title('Sine Potentials for ' + str(counter) + ' Trials')
plt.show()

plt.plot(list(I_e.keys()), list(I_e.values()), color='#444444', linestyle='--', label='')
plt.xlabel('Time (s)')
plt.ylabel('Current (nA)')
plt.title('Sine Currents')
plt.show()

print(counter)

'''
# clear
V.clear()
V[t] = EL

t = 0

# Obtain potentials by scanning across time range

while t < t_f:
    I_e_cosine = math.cos(t / t_f * (360))
    dv = (dt / tau) * ((EL - V[t]) + (R_membrane * I_e_cosine))
    V_temp = V[t] + dv
    t = t + dt

    V[t] = V_temp

    if V[t] >= V_threshold:
        V[t] = EL

# Plot axes

plt.plot(list(V.keys()), list(V.values()), color='#444444', linestyle='--', label='')
plt.xlabel('Time (s)')
plt.ylabel('Potential (mV)')
plt.title('Cosine Regression')
plt.show()
'''
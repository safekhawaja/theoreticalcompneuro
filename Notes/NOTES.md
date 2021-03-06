# Theoretical & Computational Neuroscience

#### 1. SINGLE NEURONS
- Biophysics of spike generation and action potential propagation 
- Neural coding and decoding –models of neural response, spike-triggered characterizations of response
- Measuring neural information
- Adaptation of neural responses 
- Normative models of function 

#### 2. NEURAL POPULATIONS
- Receptive field maps 
- Parallel Channels 
- Correlations and interactions 
- Network structure and computation 
 

#### 3. HIGHER LEVEL FUNCTIONS
- Memory – the Hopfield model 
- Decision making and Bayesian analysis 

## Structure of the Brain

High degree of localization / segregation and differentiated specialization — each region of the brain has individual function though the whole brain lights up for each activity. There is further localization within each region as certain circuit motifs and types of neurons exist. The different types of neurons feed forward and backword synchronously with large diversity in form and function. 

Evolution is variation followed by selection and, though the architecture occurs by chance, you can't explain it any more than the coastline of Norway. The structure adapts to the nature of the world (you become what you do) — the brain is molded by experience for faster performance. If there are principles that guide this selection, those who are looking for it are more likely to find it!

![](/Images/brain.png)

## Neurons: The Computational Units of the Brain

The brain is an extremely complex circuit made up of neurons: the circuit elements. There are other elements such as glia perform support functions. THe key specialization of neurons are the electrically excitable membranes through potential differences that allow them to generate circuits. There are also morphological specializations (shapes) that help — dendrites, the input wires or psynapses, can be proximal or distal; the axon is the output wire that branches into the axonal arbor that is made of hundreds of psynapes. Using 2% of bodyweight but 20% of metabolic power, there is almost 4km of wire in the brain! 

![](/Images/neuronspecialization.png)

The psynapes have ion channels that adjust the open voltage across the cleff (there are many!) as well as pumps that maintain a concentration gradient that upholds this potential. THe pumps use ATP to restore the ionic concentration, which is where most energy is spent. 

- **Hyperpolarization:** when positive ions flow out, the membrane potential becomes more negative.

- **Depolarization:** when negative ions flow out, the membrane potential becomes more postive.

- **Action Potentials** (signal spikes) occurs when membrane voltages increase to threshold value to sufficiently trigger neuro-transmitter responses. They're almost 1ms wide! E.g. K+ rushes out of a suffieicntly positive voltage to restore the potential, then pumps restore ion concentration. Actually, the Na+ - K+ pump is the most expensive component of the neuron system. 

Neurotransmitters, e.g. GABA, diffuse across the cleff and bind to the dendrite receptors in the post-psynaptic neuron. The cell wall has a net internal negative charge that builds up in the membrane and a positive charge around the outside (separated by a lipid bilayer). These end up looking like capacitors! They store charge that are used later when only specific ions are allowed to pass. Channels are gated by voltage (like a pipe with a valve), intra-cellular ions, and extracellular neurotransmitters.

![](/Images/ionchannels.png)

Ion channels open and close stochastically due to thermal noise, where the probability is determined by the biophysics of the channel, the membrane potential and concentrations of messages!

![](/Images/psynapticcleff.png)

---

## Electrical Modelling of Neurons

An electronically compact neuron is simplified to a uniform capacitor (dV = Ie.Rm, Q = CV, C = cA, c ~10nF/mm2). We inject small external currents through membrane resistance over the voltage difference. The difference in charge creates capacitance spread over the surface area. 

As a reality check, to generate 70 mV for an action potential with C = 1 nF, we need 10^9 neurons! To move 1 nA takes 100ms, which is the integration time for a neuron to produce a spike. I = dQ/dT = Cm dV/dT so the capacitance determines the requisite current to change the membrane potential.

Concentration and voltage gated flows balance out to adjust signal generation. The ***Equilibrium Potential*** (aka Reversal Potential) is the potential at which currents of electrical current flows will be cancelled by the concentration gradients. This energy is VQ. The energy comes from thermal energy where the ions are jossling over time — this requisite energy is e^(3V/Vt) where Vt = kT/q. 

Ion flow in = flow out across concentration gradients in this situation so the concentration outside = concentration inside multiplied by the probability of jossling inside. This becomes E = Vt/z ln(outside/inside).

Membrane current, im, is the current from ion channels and pumps and is the sum of individual ion charges multiplied by the voltage difference of the membrane potential and the field across. The leak current comes from the ion pumps where conductance is constant.

Single compartments are modelled at the same conductance and potential but multiple compartments are broken down into smaller single components.

## Integrate and Fine Model

In this model, the entire cell membrane is assumed to have the same potential. The current depends on the specific membrane capacitance multipled by the rate of change of membrane potential. The membrane current that flows spontaneously through the cells and the external current (divided by the area) is the total current generated, which is equal to the aforementioned voltage derivative. We assume there is a linear response (we ignore the non-linear response during the actual firing) and so can connect this to the conductance across the neuron to create first order ODEs to solve. 

This is used below the spike threshold (and we reset it as we consider it a full action potential). If the external current is constant, we see a uniform curve shape for each cycle, which we modelled in HW1. 

![](/Images/iafmodel_constant.png)

## The Hodgkin-Huxley Model

A much more sophisticated description of neural properties of ion channels, this model goes to the more theoretical depiction of neurons as electrical systems. Non-linearities in conductance occur because of active membrane conductances (change shape, open, block etc.). Ion channels open and close randomly (Pn(open)) set by membrane potential and messenger concentration. The actual conductance depends on channel conductance, channel density, and probability it is open (we will focus on potassium and sodium channels). 

![](/Images/membraneequation.png)

![](/Images/electrical.png)

![](/Images/conductance.png)

Voltage-gated ion channels have two gates: activation and inactivation gates. We draw it like a little ball and chain (see below).

![](/Images/voltagegated.png)

Persistent conductance only have activation gates (e.g. K+). There are k independent, identical subgates that synchronously open for the ion to pass through (picked for functional definitoins e.g. for K+, k = 4). This is not necessarily a literal definition of physical structure. We can describe this process in a Markov like manner with Pn = n^k. Below, a(n) and b(n) are opening and closing probability functions.

![](/Images/probabilityk.png)

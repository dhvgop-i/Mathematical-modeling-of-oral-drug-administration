
# Mathematical Modeling of Oral Drug Administration

This project simulates the pharmacokinetic process of drug distribution in the body after oral administration. It analyzes how drug concentration in the bloodstream changes over time, considering absorption and elimination processes.

### 1. Problem Definition

After taking a dose \( D \), the drug enters the gastrointestinal tract, where it gradually **absorbs into the bloodstream** and eventually **eliminates** from the body. The process is modeled using a one-compartment model, accounting for absorption and elimination rates:

\[
egin{cases}
rac{dA}{dt} = -k_a \cdot A \
rac{dC}{dt} = k_a \cdot A - k_e \cdot C
\end{cases}
\]

Where:
- \( A(t) \) — amount of drug in the gastrointestinal tract at time \( t \)
- \( C(t) \) — amount of drug in the bloodstream
- \( k_a \) — absorption rate constant
- \( k_e \) — elimination rate constant
- Initial conditions: \( A(0) = D \), \( C(0) = 0 \)

### 2. Numerical Solution

The system is nonlinear and solved numerically using the `solve_ivp` function from the `scipy` library in Python, which provides values of \( A(t) \) and \( C(t) \) at discrete time intervals.

### 3. Results

The simulation generates a graph demonstrating the system’s behavior:
- The drug amount in the stomach decreases exponentially.
- The concentration in the bloodstream rises initially (due to absorption), reaches a peak, and then decreases (due to elimination).

This behavior matches the pharmacokinetic profile of oral drugs.

### 4. Practical Significance

This model can be used to:
- Estimate the optimal time for the next dose.
- Compare the effectiveness of different formulations of the same drug.
- Predict blood drug concentration to avoid toxicity.

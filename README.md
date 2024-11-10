# Random-Walk-Simulation

This repository explores the **Central Limit Theorem (CLT)** through the lens of random walks. Over the fall, I conducted a three-part seminar on the Central Limit Theorem. As part of the second session, I proved the **Laplace-De Moivre Theorem**, which establishes the CLT in the context of Bernoulli random variables. These variables can be interpreted as steps in a random walk.

To enhance intuition about the theorem, this repository includes three scripts demonstrating different aspects of random walks and their connection to the CLT.

---

## **Files and Functionality**

### 1. **`Random Walk Simulation.py`**  
   This script simulates a simple random walk and visualizes its trajectory.  
   - Observe the movement of a random walk over time.
   - Useful for understanding how random walks behave step-by-step.

### 2. **`heatmap.py`**  
   This script generates a heatmap of outcomes from several random walk realizations.  
   - Simulates multiple random walks and aggregates their results.
   - Provides a visual representation of the distribution of endpoints and paths.

### 3. **`approximation.py`**  
   This script approximates the distribution of the random walk.  
   - Normalizes the results and overlays the theoretical Gaussian distribution.
   - Demonstrates how the random walk's distribution converges to a normal curve, as predicted by the Central Limit Theorem.

---

## **Theoretical Background**

### **1. Central Limit Theorem (CLT)**  
The CLT states that the sum (or average) of a large number of independent and identically distributed (i.i.d.) random variables, when properly normalized, approaches a normal distribution. This holds regardless of the original distribution of the variables.

### **2. Laplace-De Moivre Theorem**  
This specific case of the CLT demonstrates that the distribution of sums of Bernoulli random variables converges to a normal distribution as the number of trials increases. This is analogous to how the distribution of endpoints in a random walk converges to a Gaussian.

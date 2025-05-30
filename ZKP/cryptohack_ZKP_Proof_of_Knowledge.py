# Cryptohack ZKP Introduction

"""
A zero-knowledge proof (ZKP) is a technique that enables one party (the prover) to demonstrate to another party (the verifier) the truth of a certain statement without revealing any additional information besides the fact that the statement is true. The core idea behind zero-knowledge proofs is that while it's straightforward to prove you have certain knowledge by disclosing it, the real challenge lies in proving you have that knowledge without actually revealing the knowledge itself or any details about it.

Properties

At a high-level, effective zero-knowledge proof algorithms embody three critical properties, "Completeness", "Soundness", and "Zero-Knowledge", which we will be exploring in detail over the following challenges.


Interactions

In a basic setting, meaningful zero-knowledge proofs require some form of interaction between the prover and the verifier. Typically, this interaction involves the verifier asking the prover one or more random questions. The randomness of these questions, coupled with the prover's correct responses, convinces the verifier of the prover's knowledge. Without this interaction, a verifier could potentially share the proof with a third party, falsely implying that they also possess the secret knowledge.

"""

# Note: In specific models it's possible to have non-interactive zero-knowledge proofs thanks to the Fiat–Shamir heuristic, which we'll look at later.

"""
Example

An example which is often used to intuitively understand the principle of zero-knowledge proof:

You need to prove to your color-blind friend Victor that two identically shaped balls—one red, one green—are distinct without revealing which is which, you use a specific proof system. You show him the balls, and he, unable to distinguish their colors, tests you. Victor hides the balls, shows one, and either switches it or not before showing one again. You must identify if he switched the ball. Repeating this process enough times (e.g., 50 times), and since you can reliably identify switches due to seeing colors, Victor becomes convinced the balls are different without learning which is red or green. This demonstration doesn't reveal any additional information, and so, is an example of a zero-knowledge proof.

"""

# The flag is crypto{...} with ... completed with the year that Goldwasser et al published "The Knowledge Complexity of Interactive Proof Systems"

print(" The flag is: crypto{1985}")
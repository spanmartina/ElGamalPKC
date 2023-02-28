# ElGamalPKC
Implementation of the ElGamal cryptosystem mimicking the conversation between Alice (receiver) and Bob (sender). 


Three basic steps in using ElGamal PKC:
  - Key Generation
  - Encryption
  - Decryption
  
Alice publishes the public key to facilitate communication between them. Bob is the one who sends the encrypted message M.

Key Generation:
  The receiver (Alice) creates and publishes a key in advance. Steps in the key pair generation process:
  - Random generation of p and g - large prime number p (large enough that p-1 is "impossible" to achieve) and a generator g of a multiplicative group Zp* of integers mod p.
  - Selection of a private key - selection of an integer x that represents the private exponent, an integer from group Z that respects the condition 1<= x <=p-2.
  - Assembling the public key is done by computing g^x mod p.
  - Publish the triple public key (p, g, g^b) as (p, g, h) on the unsecured communication channel.
  
The encryption process:
  The process of encrypting a message M by the receiver of the key is accomplished by obtaining the triple public key (p, g, h). There is no security problem in this data transmission.
  The message M is encrypted using the following steps:
  - The message M is prepared for encoding by writing it as a set of integers (m1, m2, ...), belonging to {1,...,p-1}. 
  - The sender of the message chooses a random exponent k - the other private key
  - The second public key is calculated: C1 = g^k mod p
  - The message M is encrypted as the ciphertext C, where ci = mi∗ (g^x )^k =  mi∗ h^k
  - The encrypted message C is sent together with the second public key as a pair (C1, C2)
  
Decryption process:
  After receiving the encrypted message C and the second public key, it is necessary to use the decryption algorithm to make possible the conversion from ciphertext to clear text to read the message M.
The key shared by both people involved in the communication is sent through the second public key. This common secret is the combination of the private exponent x chosen by the Alice (receiver of the message) and the exponent k chosen by Bob (the sender)
Equation: ( g^k )^(p-1-x) = (g^k)(-x) 
The decryption of the message:
mi = (g^k)(-x) ∗ ci mod p
 

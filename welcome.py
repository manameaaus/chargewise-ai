import time
import random
import sys

banner = r"""
   ██████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ███████╗██╗    ██╗██╗███████╗███████╗
  ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝ ██╔════╝██║    ██║██║██╔════╝██╔════╝
  ██║     ███████║███████║██████╔╝██║  ███╗█████╗  ██║ █╗ ██║██║███████╗█████╗  
  ██║     ██╔══██║██╔══██║██╔══██╗██║   ██║██╔══╝  ██║███╗██║██║╚════██║██╔══╝  
  ╚██████╗██║  ██║██║  ██║██║  ██║╚██████╔╝███████╗╚███╔███╔╝██║███████║███████╗
   ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝ ╚══╝╚══╝ ╚═╝╚══════╝╚══════╝
"""

for char in banner:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.002)  # speed control

time.sleep(0.5)

messages = [
    "turning it off and on again...",
    "searching stack overflow...",
    "npm install (just in case)...",
    "fixing bugs you haven't written yet...",
    "compiling coffee into code...",
    "negotiating with semicolons...",
    "dividing by zero...",
    "removing console.log statements...",
    "adding console.log statements back...",
    "checking if it works on my machine...",
    "downloading more RAM...",
    "convincing ai to behave...",
    "summoning senior developer...",
    "pushing to production on Friday...",
    "blaming DNS...",
    "sacrificing a rubber duck...",
    "realizing it was a missing bracket...",
    "googling the error message...",
]

print("\nstarting chargewise ai...\n")
time.sleep(1)

for msg in random.sample(messages, 6):
    print(f"{msg} ", end="", flush=True)
    time.sleep(random.uniform(0.7, 1.4))
    print(" done")

time.sleep(0.5)

print("\nsystem ready.")
print("welcome to chargewise ai.")
print("may your bugs be shallow and your coffee strong.\n")
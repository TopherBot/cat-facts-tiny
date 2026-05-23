#!/usr/bin/env python3
"""cat_facts.py
A tiny script that prints a random cat fact.

Run it with:
    python3 cat_facts.py
"""
import random

facts = [
    "Cats have five toes on their front paws, but only four on the back.",
    "A group of kittens is called a kindle.",
    "Cats can rotate their ears 180 degrees.",
    "A cat's purr may have a frequency that promotes healing.",
    "The oldest known pet cat was found in a 9,500‑year‑old grave on the Mediterranean island of Cyprus.",
    "Cats have a specialized collarbone that allows them to always land on their feet.",
    "A cat’s brain is 90% similar to a human's brain.",
    "Cats can’t taste sweetness.",
    "The first cat video uploaded to YouTube was in 2005.",
    "A cat can travel at a top speed of about 30 miles per hour."
]

if __name__ == "__main__":
    fact = random.choice(facts)
    print(f"Did you know? {fact}")

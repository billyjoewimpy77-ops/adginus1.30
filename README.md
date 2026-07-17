# adginus1.30
"I remember. I recognize. I learn. I dream. I KNOW."

Single-file cognitive engine - memory, patterns, learning, dreaming, instincts, and LLM bridging in one Python file.

## What's Inside
- EmbeddingBridge (Voyage AI semantic memory)
- SuperMemory (STM/LTM/Emotional/Muscle)
- PatternRecognitionEngine
- TurboLearnEngine with mastery + curriculum
- DreamMode + InstinctEngine
- VoidPersistence (atomic, thread-safe, no eval)
- LLMBridge (OpenAI, proxy-safe, offline fallback)
- BackgroundCycle

## Quick Start
python adginus_void-5.py

## Use as a library
from adginus_void import TheVoid
void = TheVoid(name="ADGINUS-PRIME")
void.boot()
void.learn("python", "Python is versatile", domain="programming")
void.perceive("New research", source="news", intensity=0.7)
print(void.think("How to use AI creatively?", depth=3))

## Environment Variables
Set these, never hardcode:
OPENAI_API_KEY
VOYAGE_API_KEY - optional, enables semantic search

## Saving
void.save() -> creates void_brain.json + void_brain_embeddings.json
void.load() -> restores it

## Version
1.3.0 - OpenAI + Voyage build 

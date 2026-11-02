# Inference

Inference is when you send an input to a trained Gen-AI model and it generates output. 

What happens when performing inference?

1. Message added to conversation history
2. Conversation send to the model
3. GPU processes billions of calculations in parallel
4. Model generates response based on patterns learned in training
5. Response comes back

This is how AI chatbots work.

# System Prompts

System prompts are special instructions that tell the AI how to behave.

System prompts are why some bots are polite, some are better at writing code, and how they have different personalities.

# Behavior Parameters

There are three key parameters:

Temperature: controls creativity and randomness

max_tokens: Controls response length

top_p: controls word choice diversity

## Parameter Guide

### temperature (0.0 to 1.0):

-- 0.1-0.3: Predictable, consistent, factual (good for Q&A, facts)
-- 0.5-0.7: Balanced (good for general chatting)
-- 0.8-1.0: Creative, varied, surprising (good for storytelling, brainstorming)

### max_tokens

-- 50-100: Short, concise answers
-- 150-300: Medium responses (good default)
-- 500+: Long, detailed explanations

### top_p (0.0 to 1.0)

-- 0.1-0.5: Conservative word choices
-- 0.7-0.9: Balanced (good default is 0.9)
-- 0.95-1.0: Maximum diversity

# Key Concepts

1. Inference means using a trained ai model to generate outputs.
2. System prompts tell the ai how to behave
3. Parameters adjust output

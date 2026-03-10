# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  Bug 1: The secret number was 92 but when I guess 5, it says go lower which is contradictory to the secret number. The hints are backwards.
  Bug 2: I cannot restart the game
  Bug 3: All levels were showing the same 1 - 100 range for possible numbers.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  AI suggested to swap the "go higher" with the "go lower" which is correct, and it fixed the bug1.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  There was none.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I tested it manually of all the bugs Claude pointed out.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I asked Claude to fix all the bugs in all files and run the tests. It added more tests and all passed.
- Did AI help you design or understand any tests? How?
  All the tests were clear to me as the naming and function is straigh forward.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  The original app called `random.randint(1, 100)` at the top level of the script with no protection. Every time the user clicked a button, Streamlit re-ran the entire script from top to bottom, so a brand new random number got generated on every interaction. The secret had no memory between reruns.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Imagine every time you click a button on a webpage, the entire page reloads from scratch and forgets everything it knew. That's Streamlit and every button click reruns your whole Python script. Session state is like a sticky note that survives those reloads. You write a value to `st.session_state` once, and it stays there no matter how many times the page reruns.

- What change did you make that finally gave the game a stable secret number?
  I wrapped the secret number generation in a `if "secret" not in st.session_state:` check. This means the first time the app loads it picks a number and saves it to session state, but every rerun after that skips the generation and reuses the saved value instead.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  Running `pytest` after every round of fixes. It gave me immediate confidence that a change didn't break something else, and the test names made it easy to see exactly what was passing or failing without having to manually play through every scenario.

- What is one thing you would do differently next time you work with AI on a coding task?
  I would ask the AI to explain each bug before applying the fix, rather than just accepting the change. Understanding the root cause helped me write better code, and I want to make that a deliberate habit instead of just reviewing after the fact.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project showed me that AI-generated code can look completely correct at a glance while hiding subtle logic bugs that only show up when you actually play with the app. I now treat AI output as a solid first draft that still needs careful human review, not finished code I can ship without testing.

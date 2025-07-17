# Avatar Processing Service - Interviewer Guide

## Overview
This is a 35-minute backend coding challenge designed to assess a candidate's ability to design and implement a service that integrates with external APIs, handles errors gracefully, and demonstrates practical engineering judgment.

**Time Allocation:**
- Problem introduction: 3-5 minutes
- Coding: 25-28 minutes  
- Discussion/Review: 5-7 minutes

---

## Problem Presentation

### Initial Setup (3 minutes)
1. **Share the `problem.txt` file** with the candidate
2. **Share the `template.py` file** for structure reference
3. **Clarify expectations:**
   - "You have about 30 minutes to implement this service"
   - "Focus on the core functionality - we're not looking for production-perfect code"
   - "Feel free to ask questions as you go"
   - "You can use any resources, including AI assistants"

### Key Point to Emphasize
**"The moderation API endpoint in the problem description doesn't actually exist - you'll need to handle this appropriately for the demo."**

---

## Expected Candidate Questions & Responses

### Common Questions and How to Respond:

**Q: "The API doesn't exist - how should I handle this?"**
✅ **Good Response:** "Great question! How would you approach this in a real interview scenario?"
- Look for: Mock implementation, simulation, or asking about test environment

**Q: "Should I use a specific framework (Flask, FastAPI, etc.)?"**
✅ **Good Response:** "For this challenge, focus on the core logic. A simple class-based approach is fine."

**Q: "How detailed should the error handling be?"**
✅ **Good Response:** "Cover the main scenarios - API timeouts, invalid responses, network issues. Don't over-engineer."

**Q: "Should I implement database persistence?"**
✅ **Good Response:** "In-memory storage is perfectly fine for this demo."

**Q: "What about authentication/security?"**
✅ **Good Response:** "Assume the API token handling is sufficient for now."

**Q: "Should I write tests?"**
✅ **Good Response:** "Tests are great but focus on the core implementation first. If you have time, add a simple test."

---

## What to Look For

### 🟢 **Excellent Candidates**
- **Immediately recognizes the API issue** and proposes a reasonable solution
- **Implements mock functionality** with realistic logic (not just returning `True`)
- **Proper error handling** for timeouts, network issues, invalid responses
- **Clean code structure** following the provided template
- **Handles edge cases** (empty input, validation)
- **Uses appropriate data structures** (dataclasses, enums, etc.)
- **Thinks about production concerns** ("In production, I would...")

### 🟡 **Good Candidates** 
- **Recognizes the API issue** but needs some guidance
- **Basic mock implementation** (simple keyword filtering)
- **Some error handling** (at least try/catch blocks)
- **Follows the template structure** reasonably well
- **Gets core functionality working** within time limit
- **Asks clarifying questions** when stuck

### 🔴 **Concerning Signs**
- **Doesn't notice the API issue** and tries to make real HTTP calls
- **No error handling** or very basic (`pass` in except blocks)
- **Completely ignores the template** structure
- **Can't get basic functionality working** in 30 minutes
- **Doesn't ask any questions** or ask for help when clearly stuck
- **Writes overly complex code** for the time constraints

---

## Guidance to Provide

### If Candidate is Stuck (5-10 minutes in):
**"Let me give you a hint about the API issue - what would you do in a real interview if an external dependency wasn't available?"**

### If They're Overengineering (15 minutes in):
**"You're on the right track! For this challenge, focus on getting the core flow working first."**

### If They're Making Good Progress (20 minutes):
**"Nice work! If you have time, consider adding some error handling or edge cases."**

### If They're Running Out of Time:
**"You have about 5 minutes left. What's the most important thing to complete?"**

---

## Technical Evaluation Criteria

### Core Requirements (Must Have)
- [ ] Job creation with unique IDs
- [ ] Mock avatar URL generation  
- [ ] Some form of content moderation (even basic)
- [ ] Job status tracking
- [ ] Basic error handling

### Nice to Have (Bonus Points)
- [ ] Realistic mock moderation logic
- [ ] Comprehensive error handling  
- [ ] Input validation
- [ ] Clean, readable code
- [ ] Edge case handling
- [ ] Configuration options (mock vs real API)

### Code Quality Indicators
- [ ] Follows provided template structure
- [ ] Appropriate use of type hints
- [ ] Meaningful variable/function names
- [ ] Proper separation of concerns
- [ ] Comments where helpful (not obvious code)

---

## Common Implementation Approaches

### Approach 1: Simple Mock Mode (Most Common)
```python
def call_moderation_api(self, content, user_id):
    if self.mock_mode:
        return self._simulate_moderation(content)
    # Real API call here...
```
**Evaluation:** ✅ Perfect for this challenge

### Approach 2: Mock Server
Candidate might suggest running a local Flask server
**Evaluation:** 🟡 Shows full-stack thinking but overkill for 30 minutes

### Approach 3: HTTP Mocking Library
```python
@responses.activate
def test_service():
    responses.add(...)
```
**Evaluation:** ✅ Shows testing awareness, good approach

### Approach 4: Configuration-Based
```python
if config.use_real_api:
    # real implementation
else:
    # mock implementation  
```
**Evaluation:** ✅ Production-minded thinking

---

## Discussion Questions (Final 5 minutes)

### Code Review Questions:
1. **"Walk me through your solution - what does the flow look like?"**
2. **"How would you deploy this in production?"**
3. **"What would you change if this needed to handle 1000 requests per second?"**
4. **"How would you monitor this service in production?"**
5. **"What edge cases did you consider?"**

### System Design Follow-ups:
1. **"How would you handle retries for the moderation API?"**
2. **"What if the moderation API was very slow (10+ seconds)?"**
3. **"How would you handle different types of content (images vs text)?"**
4. **"What metrics would you track for this service?"**

---

## Red Flags During Interview

### Immediate Concerns:
- **Doesn't read the problem carefully** before starting to code
- **Refuses to ask questions** or dismisses guidance  
- **Writes code without any plan** or structure
- **Can't explain their approach** when asked
- **Gets frustrated with the API constraint** instead of problem-solving

### Code Quality Issues:
- **No error handling whatsoever**
- **Hard-coded values everywhere** 
- **Functions doing too many things**
- **No consideration of edge cases**
- **Copying code without understanding** (if using AI tools)

---

## Sample Evaluation Rubric

| Criteria | Weight | Excellent (4) | Good (3) | Fair (2) | Poor (1) |
|----------|--------|---------------|----------|----------|----------|
| **Problem Understanding** | 20% | Immediately grasps API issue and proposes solution | Understands with minimal guidance | Needs explanation but gets it | Doesn't understand constraints |
| **Core Implementation** | 30% | All functionality working smoothly | Most features work with minor issues | Basic functionality works | Significant functionality missing |
| **Error Handling** | 20% | Comprehensive error scenarios covered | Basic error handling present | Minimal error handling | No error handling |
| **Code Quality** | 20% | Clean, readable, well-structured | Generally good structure | Acceptable but could be cleaner | Poor structure/readability |
| **Problem Solving** | 10% | Creative solutions, handles edge cases | Solid problem-solving approach | Basic problem-solving | Struggles with unexpected issues |

**Scoring:**
- **16-20 points:** Strong hire - excellent technical skills
- **12-15 points:** Hire - solid technical abilities  
- **8-11 points:** Borderline - additional evaluation needed
- **Below 8 points:** No hire - significant technical gaps

---

## Post-Interview Notes

### Document:
- [ ] Candidate's approach to the mock API problem
- [ ] Quality of error handling implemented
- [ ] Questions asked and problem-solving approach
- [ ] Code structure and readability
- [ ] Time management and prioritization
- [ ] Response to guidance and feedback

### Follow-up Considerations:
- **Strong performers:** Consider more complex system design questions
- **Borderline candidates:** Focus on debugging existing code or collaborative problem-solving
- **Technical gaps:** Document specific areas for skill development discussions 
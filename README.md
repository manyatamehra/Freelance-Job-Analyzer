# Freelance Job Analyzer

A Python-based tool that analyzes freelance job opportunities and helps users decide whether a job is worth considering based on budget, deadline, required skills, workload, job description, and potential red flags.

##  Problem

When searching for freelance work, it can be difficult to quickly compare multiple opportunities.

A job may offer a good budget but require skills you don't have, while another may have a better skill match but an unrealistic deadline or several warning signs.

The Freelance Job Analyzer helps organize these factors and provides a simple recommendation for each job.

##  Features

* Analyze freelance job details
* Validate budget and deadline inputs
* Score jobs based on budget and deadline
* Detect skills mentioned in job descriptions
* Compare detected skills with the user's skills
* Calculate skill-match percentage
* Identify potential red flags
* Analyze workload
* Evaluate the level of detail in a job description
* Generate an overall job score
* Provide an `APPLY`, `MAYBE`, or `DON'T APPLY` recommendation
* Compare multiple jobs
* Identify the highest-scoring job
* Export results to a CSV file

##  Technologies Used

* Python
* CSV
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* String processing
* File handling

##  How It Works

The program asks the user to enter information about a freelance job, including:

* Job title
* Job description
* Budget
* Deadline

It then analyzes the job using several factors:

### 1. Budget

Higher-paying jobs receive a higher budget score.

### 2. Deadline

Jobs with more reasonable deadlines receive a higher deadline score.

### 3. Skill Detection

The program searches the job description for supported skills such as:

`Python`, `SQL`, `Excel`, `Data Analysis`, `Canva`, `Social Media`, `JavaScript`, `React`, `Node.js`, and others.

### 4. Skill Matching

Detected job skills are compared with the user's current skills to calculate a skill-match percentage.

### 5. Red Flags

The analyzer looks for potential warning signs such as:

 Very low budget
 Very tight deadline
 Urgent projects
 Requests for free work
 Exposure instead of proper payment
 Unlimited revisions

### 6. Workload

The program checks for workload indicators such as daily work, multiple posts, long-term work, or full-time availability.

### 7. Recommendation

The final recommendation is based on the overall score and the user's skill match.

## Example

For a Data Analyst Intern position requiring Python, SQL, and Excel:

```text
Score: 10 /10
Recommendation: APPLY
Skill Match: 100 %
```

For a React Developer position requiring JavaScript, React, and Node.js:

```text
Score: 8 /10
Recommendation: DON'T APPLY
Skill Match: 0 %
```

This demonstrates that a higher budget does not automatically result in an `APPLY` recommendation when the required skills do not match the user's skills.

##  Output

After analyzing multiple jobs, the program saves the results to:

```text
jobs_analysis.csv
```

The CSV file contains information such as:

 Job title
 Budget
 Deadline
 Score
 Detected skills
 Matching skills
 Skill-match percentage
 Workload
 Red flags
 Recommendation

##  How to Run

Make sure Python is installed on your computer.

Run:

```bash
python job_analyzer.py
```

Then select:

```text
1. Analyze Jobs
```

and enter the requested job information.

##  Learning Outcomes

This project helped me practice:

* Breaking a problem into reusable functions
* Working with dictionaries and lists
* Validating user input
* Processing text using Python
* Designing scoring logic
* Comparing multiple data points
* Working with CSV files
* Building a complete command-line application

##  Future Improvements

Possible future improvements include:

* Support for more skills and job categories
* Better workload detection
* More advanced text analysis
* Custom scoring preferences
* A graphical user interface
* Job data import from CSV files
* Visualization of job comparisons

##  Current Limitation

The project currently uses keyword-based skill detection rather than advanced NLP or AI models.

This keeps the project simple, free to run, and easy to understand while providing a foundation for future improvements. 

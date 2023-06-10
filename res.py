import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Resume data
resume_text = '''
John Doe
Software Engineer

Skills:
- Python
- Java
- Machine Learning

Experience:
- Software Engineer at ABC Inc.
- Internship at XYZ Corp.

Education:
- Bachelor's Degree in Computer Science

Contact:
- Email: john.doe@email.com
- Phone: 123-456-7890
'''

# Job requirements
job_keywords = ['Python', 'Machine Learning']

# Preprocess resume text
resume_text = resume_text.lower()
tokens = word_tokenize(resume_text)
tokens = [token for token in tokens if token.isalpha()]
tokens = [token for token in tokens if token not in stopwords.words('english')]

# Match job keywords with resume
matches = [token for token in tokens if token in job_keywords]

# Calculate match score
match_score = len(matches) / len(job_keywords)

# Determine if candidate is suitable
if match_score >= 0.5:
    suitability = "Suitable candidate"
else:
    suitability = "Not suitable candidate"

# Print results
print("Matched keywords:", matches)
print("Match score:", match_score)
print("Candidate suitability:", suitability)

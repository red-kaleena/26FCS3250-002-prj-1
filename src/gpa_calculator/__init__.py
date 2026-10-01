'''
CS3250 - Software Development Methods and Tools
Instructor: Thyago Mota
Student(s):
Description: Project 1 - GPA Calculator
'''

# grade points for the traditional college letter grade scale, A+ included (so GPA can exceed 4.0)
GRADE_POINTS = {
    'A+': 4.3, 'A': 4.0, 'A-': 3.7,
    'B+': 3.3, 'B': 3.0, 'B-': 2.7,
    'C+': 2.3, 'C': 2.0, 'C-': 1.7,
    'D+': 1.3, 'D': 1.0, 'D-': 0.7,
    'F': 0.0
}

def calculate_gpa(enrollments):
    '''
    Computes the credit-weighted GPA from a list of Enrollment objects.
    Each enrollment should have a 'grade' and access to course.credits.
    Enrollments with no grade yet, or an unrecognized grade, are ignored.
    Returns 0 when there are no graded credits to average.
    '''
    total_points = 0.0
    total_credits = 0
    for e in enrollments or []:
        try:
            grade = getattr(e, 'grade', None)
            if not grade:
                continue
            gp = GRADE_POINTS.get(grade)
            if gp is None:
                continue
            credits = 0
            course = getattr(e, 'course', None)
            if course is not None:
                credits = getattr(course, 'credits', 0) or 0
            if credits <= 0:
                continue
            total_points += gp * credits
            total_credits += credits
        except Exception:
            continue
    if total_credits <= 0:
        return 0
    return round(total_points / total_credits, 3)

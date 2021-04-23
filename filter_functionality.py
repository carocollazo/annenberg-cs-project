#!/usr/bin/python

# FILTER FUNCTIONS
def filter_afterSchool(program) :
    if(program["time"] == "afterSchool") : # change once access program data
        return True
    else :
        return False

def filter_inSchool(program) :
    if(program["time"] == "inSchool") : # change once access program data
        return True
    else :
        return False

def filter_academicYear(program) :
    if(program["period"] is "academicYear") : # change once access program data
        return True
    else :
        return False

def filter_summer(program) :
    if(program["period"] is "summer") : # change once access program data
        return True
    else :
        return False

def filter_shortTerm(program) :
    if(program["term"] is "shortTerm") : # change once access program data
        return True
    else :
        return False

def filter_longTerm(program) :
    if(program["term"] is "longTerm") : # change once access program data
        return True
    else :
        return False

def filter_studentLed(program) :
    if(program["lead"] is "studentLed") : # change once access program data
        return True
    else :
        return False

def filter_staffLed(program) :
    if(program["lead"] is "staffLed") : # change once access program data
        return True
    else :
        return False

def filter_facultyLed(program) :
    if(program["lead"] is "facultyLed") : # change once access program data
        return True
    else :
        return False

def filter_grantFunded(program) :
    if(program["funding"] is "grantFunded") : # change once access program data
        return True
    else :
        return False

def filter_sustained(program) :
    if(program["funding"] is "sustained") : # change once access program data
        return True
    else :
        return False

def filter_active(program) :
    if(program["isActive"]) : # change once access program data
        return True
    else :
        return False

def filter_inactive(program) :
    if(program["isActive"]) : # change once access program data
        return False
    else :
        return True



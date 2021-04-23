#!/usr/bin/python
from filter_functionality import *

# EXAMPLE DATA
p1 = {
    "pName": "project1",
    "time": "inSchool",
    "period": "academicYear",
    "term": "shortTerm",
    "lead": "staffLed",
    "funding": "sustained",
    "isActive": False
}

p2 = {
    "pName": "project2",
    "time": "afterSchool",
    "period": "summer",
    "term": "longTerm",
    "lead": "studentLed",
    "funding": "grantFunded",
    "isActive": True
}

p3 = {
    "pName": "project3",
    "time": "afterSchool",
    "period": "academicYear",
    "term": "longTerm",
    "lead": "facultyLed",
    "funding": "sustained",
    "isActive": True
}

programs = [p1, p2, p3]


# TEST FUNCTIONS
def test_afterSchool() :
    filtered_programs = filter(filter_afterSchool, programs)
    print("After School Programs: ")
    for program in filtered_programs :
        print(program["pName"])
    print("\n");

def test_inSchool() :
    filtered_programs = filter(filter_inSchool, programs)
    print("In School Programs: ")
    for program in filtered_programs :
        print(program["pName"])
    print("\n");

def test_academicYear() :
    filtered_programs = filter(filter_academicYear, programs)
    print("Academic Year Programs: ")
    for program in filtered_programs :
        print(program["pName"])
    print("\n");

def test_summer() :
    filtered_programs = filter(filter_summer, programs)
    print("Summer Programs: ")
    for program in filtered_programs :
        print(program["pName"])
    print("\n");

def test_shortTerm() :
    filtered_programs = filter(filter_shortTerm, programs)
    print("Short Term Programs: ")
    for program in filtered_programs :
        print(program["pName"])
    print("\n");

def test_longTerm() :
    filtered_programs = filter(filter_longTerm, programs)
    print("Long Term Programs: ")
    for program in filtered_programs :
        print(program["pName"])
    print("\n");

def test_studentLed() :
    filtered_programs = filter(filter_studentLed, programs)
    print("Student Led Programs: ")
    for program in filtered_programs :
        print(program["pName"])
    print("\n");

def test_staffLed() :
    filtered_programs = filter(filter_staffLed, programs)
    print("Staff Led Programs: ")
    for program in filtered_programs :
        print(program["pName"])
    print("\n");

def test_facultyLed() :
    filtered_programs = filter(filter_facultyLed, programs)
    print("Faculty Led Programs: ")
    for program in filtered_programs :
        print(program["pName"])
    print("\n");

def test_grantFunded() :
    filtered_programs = filter(filter_grantFunded, programs)
    print("Grant Funded Programs: ")
    for program in filtered_programs :
        print(program["pName"])
    print("\n");

def test_sustained() :
    filtered_programs = filter(filter_sustained, programs)
    print("Sustained Programs: ")
    for program in filtered_programs :
        print(program["pName"])
    print("\n");

def test_active() :
    filtered_programs = filter(filter_active, programs)
    print("Active Programs: ")
    for program in filtered_programs :
        print(program["pName"])
    print("\n");

def test_inactive() :
    filtered_programs = filter(filter_inactive, programs)
    print("Inactive Programs: ")
    for program in filtered_programs :
        print(program["pName"])
    print("\n");

test_afterSchool()
test_inSchool()
test_academicYear()
test_summer()
test_shortTerm()
test_longTerm()
test_studentLed()
test_staffLed()
test_facultyLed()
test_grantFunded()
test_sustained()
test_active()
test_inactive()

from fastapi import APIRouter
from backend.data import students
from backend.schemas import (StudentCreate,StudentResponse,StudentUpdate,StudentPatch)

routes = APIRouter()

@routes.get("/students")
def showStudents():
    return students


@routes.get("/students/{stdID}")
def getByID(stdID: int):
    for student in students:
        if student["id"] == stdID:
            return student

@routes.post("/student",response_model=StudentResponse)
def createStudent(std:StudentCreate):
  newUser ={
            "id":len(students)+1,
            "name":std.name,
            "age":std.age,
            }
    
  students.append(newUser)
  return newUser

  return {"message": "Not found"}

@routes.put("/student/{studentId}")
def updateStudent(studentId:int,student:StudentUpdate):
    for existing_Student in students:
        if existing_Student["id"]== studentId:
            existing_Student["name"]=student.name
            existing_Student["age"]=student.age
            return existing_Student

@routes.patch("/student/{userId}")
def partial_update(userId: int, student: StudentPatch):
    for existingStudent in students:
        if existingStudent["id"] == userId:

            if student.name is not None:
                existingStudent["name"] = student.name

            if student.age is not None:
                existingStudent["age"] = student.age

            return existingStudent
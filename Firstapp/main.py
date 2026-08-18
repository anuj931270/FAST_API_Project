from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
import requests
from database import SessionLocal, engine, Base
import models,schema
import json
from typing import Optional
from pydantic import BaseModel

Base.metadata.create_all(bind=engine)

app = FastAPI(description="This is My first FastAPI app")
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check(db:Session=Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return{"status":"ok","db":"connected✅"}
    except Exception as e:
        raise HTTPException(status_code=503,detail=f"DB connection failed : {str(e)} ❌")



@app.get("/")
def test():
    return {"message": "Hello to FastAPI"}


@app.get("/product")
def get_product():
    resp = requests.get("https://dummyjson.com/products")
    data = resp.json()
    return data

@app.get("/cart")
def get_cart():
    resp = requests.get("https://dummyjson.com/carts")
    data = resp.json()
    return data


@app.post("/staff")
def create(staff: schema.StaffCreate, db: Session = Depends(get_db)):
    new_staff = models.Staff(
        emp_name=staff.emp_name,
        emp_age=staff.emp_age,
        emp_city=staff.emp_city
    )

    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)

    return new_staff


@app.get("/staff")
def get_all_staff(db: Session = Depends(get_db)):
    staff = db.query(models.Staff).all()
    return staff

@app.get("/staff/{staff_id}")
def get_all_staff(staff_id: int, db: Session = Depends(get_db)):
    staff = db.query(models.Staff).filter(models.Staff.id == staff_id).first()
    return staff


@app.post("/staff/bulk-upload")
def bulk_upload_staff(db: Session = Depends(get_db)):
    try:
        with open("staff.json", "r") as f:
            staff_list = json.load(f)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    created = []

    for item in staff_list:

        new_staff = models.Staff(
            emp_name=item["emp_name"],
            emp_age=item["emp_age"],
            emp_city=item["emp_city"]
        )

        db.add(new_staff)
        created.append(new_staff)

    db.commit()

    for staff in created:
        db.refresh(staff)

    return {
        "Inserted": len(created),
        "staff": created
    }

@app.delete("/staff/{staff_id}")
def delete_staff(staff_id:int, db: Session=Depends(get_db)):
    staff=db.query(models.Staff).filter(models.Staff.id==staff_id).first()
    if not staff:
        raise HTTPException(status_code=404)
    db.delete(staff)
    db.commit()
    return {"Message":f"Start with id: {staff_id} has been Deleted ✅"}

@app.delete("/staff")
def delete_all_staff(confirm:bool=False, db: Session=Depends(get_db)):
    if not confirm:
        raise HTTPException(status_code=400, detail="This will delete All Staff records.")

    staff=db.query(models.Staff).delete()
    db.commit()
    return {"Message":f"Deleted {staff} ✅"}

#update and partial update
@app.put("/staff/{staff_id}")
def update_staff(
    staff_id: int,
    updated_staff: schema.StaffCreate,
    db: Session = Depends(get_db)
):

    staff = db.query(models.Staff).filter(models.Staff.id == staff_id).first()

    if not staff:
        raise HTTPException(status_code=404, detail="Staff Not Found")

    staff.emp_name = updated_staff.emp_name
    staff.emp_age = updated_staff.emp_age
    staff.emp_city = updated_staff.emp_city

    db.commit()
    db.refresh(staff)

    return {
        "Message": "Staff Updated Successfully ✅",
        "staff": staff
    }
@app.patch("/staff/{staff_id}")
def update_staff(staff_id: int, staff: schema.StaffUpdate, db: Session = Depends(get_db)):
    emp = db.query(models.Staff).filter(models.Staff.id == staff_id).first()

    if not emp:
        raise HTTPException(status_code=404, detail="Staff Not Found")

    if staff.emp_name is not None:
        emp.emp_name = staff.emp_name

    if staff.emp_age is not None:
        emp.emp_age = staff.emp_age

    if staff.emp_city is not None:
        emp.emp_city = staff.emp_city

    db.commit()
    db.refresh(emp)

    return {
        "Message": "Staff Updated Successfully ✅",
        "staff": emp
    }   
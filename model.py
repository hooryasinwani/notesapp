from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Note(Base):
	__tablename__ = "notes"

	id = Column(Integer, primary_key= True, index = True)
	title = Column(String, nullable = False)
	content = Column(String, nullable = False)
	user_id = Column(Integer, ForeignKey("users.id"), nullable = False)

	owner= relationship(
		"User",
		back_populates = "notes"
		)
	class Config:
		from_attributes = True



class User(Base):
	__tablename__ ="users"
	id = Column(Integer, primary_key=True, index=True)
	username = Column(String,unique=True, nullable=False)
	hashed_password = Column(String, nullable=False)


	notes = relationship(
        "Note",
        back_populates="owner"
    )
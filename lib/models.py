from sqlalchemy import ForeignKey, Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm  import declarative_base

Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    character_name = Column(String(), nullable=False)

    #One to Many Relationship with Audition
    auditions = relationship('Audition', backref=backref('role', lazy=True), cascade="all, delete-orphan")

def actors(self):
    #Returns a list of actors associated with their respective roles
    return[audition.actor for audition in self.auditions]

def locations(self):
    #Returns a list of locations for auditions associated with its role
    return[audition.location for audition in self.auditions]

def lead(self):
    #Returns the first hired auditions for this role or a string if no actors are hired
    hired_audtions = [audition for audition in self.auditions if audition.hired]
    return hired_audtions[0] if hired_audtions else "no actor has been hired"

def understudy(self):
    #Returns the second hired audition for this role or a string if no understudy is hired
    hired_auditions = [audition for audition in self.auditions if audition.hired ]
    return hired_auditions[1] if len(hired_auditions) > 1 else "no actor has been hired for this audition"

def __repr__(self):
    return f"<Role(id={self.id}, character_name='{self.character_name}')>"


class Audition(Base):
    __tablename__ = 'auditions'
    id = Column(Integer, primary_key = True, autoincrement=True)
    actor = Column(String(), nullable = False)
    location = Column(String(), nullable = False)
    phone_number = Column(Integer, nullable=False )
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)

   #Many-to-one relationship with Role
role = relationship('Role',back_populates='auditions')

def call_back(self):
     #Sets the hired attribute to true
     self.hired = True

def __repr__(self):
        return f"<Audition(id={self.id}, actor='{self.actor}', location='{self.location}', hired={self.hired})>"
    
#Create, Read, Update, Delete Operation
def create_role(session, character_name):
     role = Role(character_name = character_name)
     session.add(role)
     session.commit()
     return role

def create_audition(session, actor, location, phone_number):
     audition = Audition(actor=actor, location=location, phone_number=phone_number)
     session.add(audition)
     session.commit()
     return audition

def get_roles(session):
     roles = session.query(Role).all()
     return roles

def get_auditions(session):
     auditions=  session.query(Audition).all()
     return auditions

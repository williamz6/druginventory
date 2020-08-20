
class Drug(db.Model):
    __tablename__= "drugs"
    id = db.Column(db.Integer, primary_key=True)
    drug_name = db.Column(db.String(100), unique=True)
    quantity= db.Column(db.Integer, nullable=False)

    def __init__(self, drug_name, quantity):

        self.drug_name = drug_name
        self.quantity = quantity

class Movement(db.Model):
  __tablename__ = 'movements'
  id = db.Column(db.Integer(), primary_key=True)
  drug_name = db.Column(db.String(100), unique=True) 
  destination= db.Column(db.String(100))
  quantity = db.Column(db.Integer)
  status= db.Column(db.String(20))  #transaction_in or transaction_out
  movement_time = db.Column(db.DateTime, default=datetime.utcnow)

  drugs = relationship("Drug", secondary="drugmovements")

  def __init__(self, quantity=None):
   
    self.quantity = quantity

  def __repr__(self):
    return '<Movement {}>'.format(self.drug.drug_name)


class Drugmovement(db.Model):
    __tablename__= "drugmovements" #associative table
    id = db.Column(db.Integer, primary_key=True)
    drug_id = db.Column(db.Integer(), db.ForeignKey('drugs.id'))
    move_id = db.Column(db.Integer(), db.ForeignKey('movements.id')) 
    drug_name = Column(String(256)) #extra data
    quantity= db.Column(db.Integer, nullable=False)    
   
    drug = relationship("Drug", backref=backref("transactions", cascade="all, delete-orphan" ))
    transaction = relationship("Transaction", backref=backref("transactions", cascade="all, delete-orphan" ))
    


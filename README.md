# druginventory
A database for a drug inventory system


class Drug(db.Model):
    __tablename__= "drugs"
    id = db.Column(db.Integer, primary_key=True)
    drug_name = db.Column(db.String(100), unique=True)
    quantity= db.Column(db.Integer, nullable=False)
    
    def __init__(self, drug_name, quantity):

        self.drug_name = drug_name
        self.quantity = quantity

class Transaction(db.Model):
    __tablename__= "transactions"
    id = db.Column(db.Integer, primary_key=True)
    drug_id = db.Column(db.Integer(), db.ForeignKey('drugs.id'))
    quantity= db.Column(db.Integer, nullable=False)
    transaction_time = db.Column(db.DateTime, default=datetime.utcnow)

    drugs = relationship("Drug", secondary="movements")

class Movement(db.Model):
  __tablename__ = 'movements'
  id = db.Column(db.Integer(), primary_key=True)
  drug_id = db.Column(db.Integer, db.ForeignKey('drugs.id'), primary_key=True)
  t_id = db.Column(db.Integer, db.ForeignKey('transactions.id'), primary_key=True)
  quantity = db.Column(db.Integer)

  drug = relationship("Drug", backref=backref("movements", cascade="all, delete-orphan" ))
  transaction = relationship("Transaction", backref=backref("movements", cascade="all, delete-orphan" ))

  def __init__(self, drug=None, quantity=None):
    
    self.drug = drug
   
    self.quantity = quantity

  def __repr__(self):
    return '<Movement {}>'.format(self.drug.name)

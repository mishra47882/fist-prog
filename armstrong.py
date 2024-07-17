import pandas as pd

studett_id=[[1,15],[2,65],[3,11],[4,65]]

def Dataframe(studett_id):
    pd.DataFrame(studett_id)
    colunm_name=("student id","age")
    R=pd.DataFrame(studett_id,columns=colunm_name)
    return R
print(Dataframe(studett_id))
